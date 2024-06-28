# Safety-Helmet-Detection-Project ⚠️
-  Author: Mai Trung Kien AIO-2024
-  Project1-Module1-AIO2024: Safety-Helmet_Detection

# How to run 🚀 
### 1. Clone source yolov10
```
git clone https://github.com/THU-MIG/yolov10.git 
```
### 2. Download pretrained model via command line
```
HOME = os.getcwd()
!mkdir -p {HOME}/weights
!wget -P {HOME}/weights -q https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt
!wget -P {HOME}/weights -q https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10s.pt
!wget -P {HOME}/weights -q https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10m.pt
!wget -P {HOME}/weights -q https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10b.pt
!wget -P {HOME}/weights -q https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10x.pt
!wget -P {HOME}/weights -q https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10l.pt
!ls -lh {HOME}/weights
```
### 3. Download pretrained via link (Performace on COCO)
| Model | Test Size | #Params | FLOPs | AP<sup>val</sup> | Latency |
|:---------------|:----:|:---:|:--:|:--:|:--:|
| [🔗 YOLOv10-N ](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt) |   640  |     2.3M    |   6.7G   |     38.5%     | 1.84ms |
| [🔗 YOLOv10-S](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10s.pt) |   640  |     7.2M    |   21.6G  |     46.3%     | 2.49ms |
| [🔗 YOLOv10-M](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10m.pt) |   640  |     15.4M   |   59.1G  |     51.1%     | 4.74ms |
| [🔗 YOLOv10-B](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10b.pt) |   640  |     19.1M   |  92.0G |     52.5%     | 5.74ms |
| [🔗 YOLOv10-L](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10l.pt) |   640  |     24.4M   |  120.3G   |     53.2%     | 7.28ms |
| [🔗 YOLOv10-X](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10x.pt) |   640  |     29.5M    |   160.4G   |     54.4%     | 10.70ms |

* [🔗 Click here to download yolov10n.pt](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt)
* [🔗 Click here to download yolov10s.pt](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10s.pt)
* [🔗 Click here to download yolov10x.pt](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10x.pt)
* [🔗 Click here to download yolov10x.pt](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10x.pt)
* [🔗 Click here to download yolov10l.pt](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10l.pt)

### 3. Clone this repositories
```
git clone https://github.com/VayneMai020301/Safety-Helmet-Detection-Project.git
```

### 4. Download Dataset 
[Click here to download Helmet Dataset](https://drive.usercontent.google.com/u/0/uc?id=1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R&export=download)

# Dependencies installation 🛠️
1. Conda Enviroment 
`conda` virtual enviroment is recommended. 
```
conda create -n yolov10 python=3.10.0
conda activate yolov10
pip install -r requirements.txt
pip install -e .
```
2. Install torch, torchvision, torchaudio
```
pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu118
```
3. Install ultralytics via git 
```
pip install -q git+https://github.com/THU-MIG/yolov10.git
```
# How to training 🛠️
```
cd .\Safety-Helmet-Detection-Project\
python \train.py
```
# Training Process, Validation ✳️
<body>
   <div style="display: flex; justify-content: left; align-items: left;">
  <figure style="margin: 10px;">
    <img src="imgs\results.png" alt="Image 1" style="width: 500px; height: auto;">
    <figcaption style="font-size: 18px; text-align: center;">Training Results</figcaption>
  </figure>
  <figure style="margin: 10px;">
    <img src="imgs\train_batch4322.jpg" alt="Image 2" style="width: 250px; height: auto;">
    <figcaption style="font-size: 18px; text-align: center;">Train batch (i)</figcaption>
  </figure>
  <figure style="margin: 10px;">
    <img src="imgs\val_batch2_pred.jpg" alt="Image 3" style="width: 250px; height: auto;">
    <figcaption style="font-size: 18px; text-align: center;">Validation batch (i)</figcaption>
  </figure>
</div>
</body>


# How to inference🛠️
```
cd .\Safety-Helmet-Detection-Project\
python \inference.py
```

# Helmet Detection Results ✳️
<body>
    <div class="center">
        <img src="imgs\helmet_detection_0.png" alt="Image 1" width="300" height="300">
        <img src="imgs\helmet_detection_25.png" alt="Image 2" width="300" height="300">
        <img src="imgs\helmet_detection_29.png" alt="Image 3" width="300" height="300">
        <img src="imgs\helmet_detection_35.png" alt="Image 4" width="300" height="300">
    </div>
</body>