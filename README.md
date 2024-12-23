## **Object-Detection-Dataset-for-Movie-Analytics-Using-YOLO-and-ViT**

### **Overview**
This repository contains the code and resources for building an automated movie analytics system using **YOLO (You Only Look Once)** for object detection and **Vision Transformers (ViT)** for advanced image analysis. The project focuses on detecting objects and analyzing keyframes extracted from movies.

### **Features**
- **Keyframe Extraction:** Automatically extracts keyframes from video files or YouTube URLs.
- **Object Detection:** Leverages YOLO for efficient object detection in extracted keyframes.
- **Advanced Analytics:** Utilizes Vision Transformers (ViT) for enhanced image analytics.
---

### **Repository Structure**
| **File/Folder Name**        | **Description**                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------|
| `.gitignore`                 | Specifies files and folders to be ignored by Git to maintain a clean repository.                |
| `Detect_Object.py`           | Python script to perform object detection on extracted keyframes using YOLO.                    |
| `LICENSE`                    | Contains the MIT license for the repository.                                                   |
| `README.md`                  | Provides an overview and instructions for using the repository.                                 |
| `Url_to_Frame.py`            | Script to extract keyframes from video URLs.                                                   |
| `Main.py`                    | A script that generates a dataset when provided with a YouTube movie URL.                      |
| `requirements.txt`           | Lists all required Python libraries for the project.                                           |
| `Automated-Movie-Key-Frame`  | Main directory that contains datasets, results, or related resources for the project.           |

---

### **Getting Started**
Follow these instructions to set up and run the project on your local system.

#### **Prerequisites**
- Python 3.8 or later
- Required Python libraries (install using `requirements.txt`)
- An internet connection to download YOLO weights and dependencies

#### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/iamdebasishdas123/Object-Detection-Dataset-for-Movie-Analytics-Using-YOLO-and-ViT.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Object-Detection-Dataset-for-Movie-Analytics-Using-YOLO-and-ViT
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### **Usage**

#### **1. Extract Keyframes and Save Results**
Run the `Main.py` script to extract keyframes and save the results:
```bash
python Main.py
```

---

### **Outputs**
- **Keyframes Folder:** The extracted keyframes from videos.
- **Detection Results:** Annotated images and JSON files indicating detected objects and their locations.

---

### **Technologies Used**
- **YOLOv8:** For efficient and accurate object detection.
- **Vision Transformers (ViT):** For advanced analytics of movie frames.
- **OpenCV:** For processing video frames and extracting images.

---
