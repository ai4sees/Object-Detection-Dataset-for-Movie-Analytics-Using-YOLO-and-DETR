# Object-Detection-Dataset-for-Movie-Analytics-Using-YOLO-and-DETR

This repository provides tools for automated movie analytics by detecting and analyzing objects in keyframes extracted from movies. It utilizes both YOLO (You Only Look Once) and DETR (DEtection TRansformer) models for object detection, with a focus on combining their strengths.

---

## Features

- **Keyframe Extraction**: Extracts keyframes from videos for analysis.
- **Object Detection**: Combines YOLO and DETR detections for enhanced accuracy.
- **Bounding Box Union**: Merges detections of the same object from both models.
- **Confidence Filtering**: Filters results with a confidence score greater than 0.5.
- **OOP Design**: Implements object detection using a modular, class-based approach.

---

## Repository Structure

| File/Folder         | Description                                                                           |
|---------------------|---------------------------------------------------------------------------------------|
| `.gitignore`        | Specifies files and folders to be ignored by Git to maintain a clean repository.     |
| `Detect_Object.py`  | Contains the primary logic for object detection using YOLO and DETR models.          |
| `LICENSE`           | Contains the MIT license for the repository.                                         |
| `README.md`         | Provides an overview and instructions for using the repository.                      |
| `Url_to_Frame.py`   | Script for extracting keyframes from video URLs.                                      |
| `main.py`           | Orchestrates the pipeline, from keyframe extraction to object detection.             |
| `requirements.txt`  | Lists all required Python libraries for the project.                                 |

---

## Installation

### Prerequisites

- Python 3.8 or later
- Required Python libraries (listed in `requirements.txt`)
- YOLO weights (`yolov8n.pt`) and DETR model files (downloaded automatically by the scripts)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ai4sees/Object-Detection-Dataset-for-Movie-Analytics-Using-YOLO-and-DETR.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Object-Detection-Dataset-for-Movie-Analytics-Using-YOLO-and-DETR
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. Extract Keyframes

Run `Url_to_Frame.py` to extract keyframes from a video URL or local video file. Keyframes will be stored in the specified directory.

### 2. Perform Object Detection

Run the main detection script `main.py`:
```bash
python main.py
```

Replace `"YourMovieTitle"` in the `main()` function call with the name of the movie you're analyzing. The results will be saved in the `results` folder under the specified movie title.

### 3. Outputs

- **Detection Results**: Each processed frame generates a text file in the `results` folder. Each line contains:
  ```
  class_id,x_min,y_min,x_max,y_max
  ```
- **Unified Boxes**: Bounding boxes from YOLO and DETR are merged when they detect the same object.

---

## Example Result File

A result file (`frame_001_boxes.txt`) will look like:
```
1,50,60,200,300
2,400,350,500,450
```
Here, `1` and `2` represent class IDs, followed by the bounding box coordinates.

---

## Technologies Used

- **YOLOv8**: Efficient object detection.
- **DETR**: Transformer-based detection for high accuracy.
- **OpenCV**: For reading and processing frames.
- **PyTorch Transformers**: For implementing DETR.

---

## Contributing

Contributions to enhance the detection pipeline or integrate additional models are welcome. Fork the repository, make your changes, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Let me know if you'd like to include anything else in the documentation!
