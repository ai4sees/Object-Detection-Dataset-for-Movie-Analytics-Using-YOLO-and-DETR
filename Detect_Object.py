import os
import cv2
import torch
from ultralytics import YOLO
from transformers import DetrImageProcessor, DetrForObjectDetection

class ObjectDetectionProcessor:
    def __init__(self, title):
        self.main_folder = "Movie Frame"
        self.title = title
        self.results_folder = os.path.join(self.main_folder, self.title, "results")
        self.input_folder = os.path.join(self.main_folder, self.title, "Key_Frame")

        # Load YOLO model
        self.yolo_model = YOLO("yolov8n.pt")

        # Load DETR model and processor
        self.detr_processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
        self.detr_model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

        # Ensure output folder exists
        os.makedirs(self.results_folder, exist_ok=True)

    @staticmethod
    def union_boxes(box1, box2):
        """Compute the union of two bounding boxes."""
        x1 = min(box1[0], box2[0])
        y1 = min(box1[1], box2[1])
        x2 = max(box1[2], box2[2])
        y2 = max(box1[3], box2[3])
        return [x1, y1, x2, y2]

    def detect_objects(self, frame_path):
        """Perform object detection on a single frame."""
        image = cv2.imread(frame_path)
        original_shape = image.shape[:2]  # Height, Width

        # YOLO inference
        yolo_results = self.yolo_model(frame_path)
        yolo_boxes, yolo_labels, yolo_class_ids = [], [], []
        for box in yolo_results[0].boxes:
            if box.conf.tolist()[0] > 0.5:  # Filter by confidence
                x_min, y_min, x_max, y_max = box.xyxy.tolist()[0]
                yolo_boxes.append([x_min, y_min, x_max, y_max])
                yolo_labels.append(self.yolo_model.names[int(box.cls.tolist()[0])].lower())
                yolo_class_ids.append(int(box.cls.tolist()[0]))

        # DETR inference
        inputs = self.detr_processor(images=image, return_tensors="pt")
        outputs = self.detr_model(**inputs)
        target_sizes = torch.tensor([original_shape])
        detr_results = self.detr_processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.5)[0]

        detr_boxes, detr_labels, detr_class_ids = [], [], []
        for box, label, score in zip(detr_results["boxes"], detr_results["labels"], detr_results["scores"]):
            if score.item() > 0.5:  # Filter by confidence
                detr_boxes.append(box.tolist())
                detr_labels.append(self.detr_model.config.id2label[label.item()].lower())
                detr_class_ids.append(label.item())

        # Combine YOLO and DETR detections
        unified_boxes = self.combine_detections(yolo_boxes, yolo_labels, yolo_class_ids, detr_boxes, detr_labels, detr_class_ids)

        return unified_boxes

    def combine_detections(self, yolo_boxes, yolo_labels, yolo_class_ids, detr_boxes, detr_labels, detr_class_ids):
        """Combine YOLO and DETR detections by merging boxes of the same label."""
        unified_boxes = []
        for yolo_box, yolo_label, yolo_class_id in zip(yolo_boxes, yolo_labels, yolo_class_ids):
            merged = False
            for detr_box, detr_label, detr_class_id in zip(detr_boxes, detr_labels, detr_class_ids):
                if yolo_label == detr_label:  # Same label
                    union_box = self.union_boxes(yolo_box, detr_box)
                    unified_boxes.append((yolo_class_id, union_box))
                    merged = True
                    break
            if not merged:
                unified_boxes.append((yolo_class_id, yolo_box))

        for detr_box, detr_label, detr_class_id in zip(detr_boxes, detr_labels, detr_class_ids):
            if not any(detr_label == yolo_label for yolo_label in yolo_labels):
                unified_boxes.append((detr_class_id, detr_box))

        return unified_boxes

    def process_frames(self):
        """Process all frames in the keyframes folder."""
        for frame_file in sorted(os.listdir(self.input_folder)):
            frame_path = os.path.join(self.input_folder, frame_file)
            unified_boxes = self.detect_objects(frame_path)
            self.save_results(frame_file, unified_boxes)

    def save_results(self, frame_file, unified_boxes):
        """Save detection results for a frame to a text file."""
        result_path = os.path.join(self.results_folder, f"{os.path.splitext(frame_file)[0]}.txt")
        with open(result_path, "w") as f:
            for class_id, box in unified_boxes:
                box_str = ", ".join(map(str, map(int, box)))
                f.write(f"{class_id},{box_str}\n")
        print(f"Results saved: {result_path}")


def main2(title):
    processor = ObjectDetectionProcessor(title)
    processor.process_frames()


# Example usage
if __name__ == "__main2__":
    main2("YourMovieTitle")  # Replace with your movie title
