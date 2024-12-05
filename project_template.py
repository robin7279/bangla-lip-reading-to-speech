# Project structure
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "BanglaLip2Speech"

list_of_files =[
    ".github/workflows/.gitkeep",
    # Data
    "data/raw/", # Raw videos
    "data/frames/", # Extracted frames from videos
    "data/labels/", # YOLO annotations (train/test)
    "data/images/", # Organized images for YOLO (train/test)
    "data/yolov11_model/", # YOLOv11 trained model
    "data/processed/", # Preprocessed data for lip reading
    # ML Model
    "ml_model/preprocess.py", # Data preprocessing for lip-reading model
    "ml_model/train.py", # Train lip-reading model
    "ml_model/infer.py", # Inference for lip reading
    # YOLOv11 
    "yolov11/train.py", # Training YOLOv11 for lip detection
    "yolov11/config.yaml", # Configuration for YOLO dataset
    "yolov11/detect.py", # YOLO detection script
    # Text to Speech
    "tts/text_to_speech.py", # Converts predicted text to speech
    "tts/real_time/real_time_inference.py", # End-to-end real-time system
    "requirements.txt",
    "notebook/BngLip2Speech.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with  open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists.")