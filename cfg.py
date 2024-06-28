import torch
import tqdm
import glob
import os
import shutil

from ultralytics import YOLOv10

config = {
    "yaml_path": r"Safety_Helmet_Dataset/data.yaml",
    "model_path" : r"weights/yolov10s.pt" , 
    "epochs": 100,
    "img_size": 640,
    "batch_size":16
}

device = torch.device("cuda" if torch.cuda.is_available() else "cpu"); print(f"device: {device}")

MODEL_PATH = "weights/yolov10l.pt"
MODEL_HELMET_PATH = "custom_weights/best.pt"
RESULT_PATH = "result/"