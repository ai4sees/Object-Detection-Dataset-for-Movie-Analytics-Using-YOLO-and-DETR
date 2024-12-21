import os
from ultralytics import YOLO


class VideoProcessor:
    def __init__(self, title):
        self.main_folder = "Movie Frame"
        self.title = title
        self.results_folder = os.path.join(self.main_folder, self.title, "results")
        self.input_folder = os.path.join(self.main_folder, self.title, "Key_Frame")
        self.model = YOLO("yolov8n.pt")  # Load the YOLO model

        # Ensure the output folder exists
        os.makedirs(self.results_folder, exist_ok=True)

        # Initialize a set to keep track of all detected classes
        self.detected_classes = set()

    def process_frames(self):
        """Process each frame in the keyframes folder."""
        for frame_file in sorted(os.listdir(self.input_folder)):
            frame_path = os.path.join(self.input_folder, frame_file)
            detected_classes = self.detect_objects(frame_path, frame_file)
            self.detected_classes.update(detected_classes)

    def detect_objects(self, frame_path, frame_file):
        """Perform object detection on a single frame."""
        result = self.model(frame_path)  # Perform detection on the frame

        # Prepare to save bounding box data to a text file
        result_text_path = os.path.join(self.results_folder, f"{os.path.splitext(frame_file)[0]}.txt")
        
        detected_classes = set()

        with open(result_text_path, 'w') as f:
            for box in result[0].boxes:
                x, y, w, h = box.xywhn.tolist()[0]  # Normalized x, y, width, height
                class_id = int(box.cls.tolist()[0])  # Class ID
                confidence = box.conf.tolist()[0]  # Confidence score
                
                if confidence > 0.5:
                    object_name = self.model.names[class_id]  # Get object name from model
                    f.write(f"{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")
                    detected_classes.add(object_name)

        print(f"Bounding box data saved: {result_text_path}")
        
        return detected_classes

    def save_class_summary(self):
        """Save a summary of all classes detected across all images in text format."""
        class_summary_path = os.path.join(self.results_folder, "classes.txt")
        class_dict = {int(i): self.model.names[i] for i in range(len(self.model.names))}

        # Write the class dictionary to a text file
        with open(class_summary_path, "w") as f:
            for class_id, class_name in class_dict.items():
                f.write(f"{class_id}: '{class_name}'\n")  # Format each line as "ID: 'Name'"

        print(f"Class names written to {class_summary_path}")


def main2(Title):
    processor = VideoProcessor(Title)
    processor.process_frames()
    processor.save_class_summary()


# Example usage
if __name__ == "__main__":
    main2("YourMovieTitle")  # Replace with your movie title
