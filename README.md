# Safety-Helmet-Detection-Project
-  Author: MaiTrungKien
-  Project1-Module1-AIO2024: Safety-Helmet_Detection

# How to run
### 1. Clone source yolov10
```
git clone https://github.com/THU-MIG/yolov10.git 
```
### 2. Download pretrained model via cmd
```
!mkdir -p {HOME}/weights
!wget -P {HOME}/weights -q https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt
!wget -P {HOME}/weights -q https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10s.pt
!wget -P {HOME}/weights -q https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10m.pt
!wget -P {HOME}/weights -q https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10b.pt
!wget -P {HOME}/weights -q https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10x.pt
!wget -P {HOME}/weights -q https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10l.pt
!ls -lh {HOME}/weights
```
### 3. Download pretrained via link
* [Click here to download yolov10n.pt](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt)
* [Click here to download yolov10s.pt](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10s.pt)
* [Click here to download yolov10x.pt](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10x.pt)
* [Click here to download yolov10x.pt](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10x.pt)
* [Click here to download yolov10l.pt](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10l.pt)

### 4. Clone this repositories
```
git clone https://github.com/VayneMai020301/Safety-Helmet-Detection-Project.git
```
# Dependencies installation
1. Create Conda Enviroment 
```
conda create -p env python=3.10
conda activate env
pip install -r requirement.txt
```
2. Install torch, torchvision, torchaudio
```
pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu118
```
3. Install ultralytics via git 
```
pip install -q git+https://github.com/THU-MIG/yolov10.git
```
# How to training 
```
python \train.py

```
# Training Process

# How to inference
```
python \inference.py
```

# Helmet Detection Results
<body>
    <div class="center">
        <img src="result\helmet_detection_0.png" alt="Image 1" width="300" height="300">
        <img src="result\helmet_detection_0.png" alt="Image 2" width="300" height="300">
        <img src="result\helmet_detection_0.png" alt="Image 3" width="300" height="300">
        <img src="result\helmet_detection_0.png" alt="Image 4" width="300" height="300">
    </div>
</body>