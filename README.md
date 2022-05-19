# TrackTick
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_tc20aOIdlAza0szHfwP7wQ09QDnhk7z?usp=sharing)

This is the repository of our academic project of the course CSE 4622. In this project, we have tried to propose a `Pedestrian Tracker` to track the movement of the pedestrian captured by videos. 
<p align="center"> <img src="sample.gif" class="center"/>

## Installation 

1. Clone the repository and enter the right path:
```bash
    git clone https://github.com/SamiaShashmi/TrackTick
    cd TrackTick
```
2. Necessary requirements can be imported by running the corresponding `requirements.txt` files.

## Inference
    
To see a demo, simply just run the [Google Colab Notebook](https://colab.research.google.com/drive/1_tc20aOIdlAza0szHfwP7wQ09QDnhk7z?usp=sharing). All the necessary are guideline are given here.

## Training
1. To train the `Person Detection` model using [YOLOv5](https://github.com/ultralytics/yolov5), follow [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1M8I_SeZJO4_96ryfJdZhqp5H7qstRNw1?usp=sharing)
2. To train the `Person ReID` model with [Torchreid](https://github.com/KaiyangZhou/deep-person-reid), go [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1UWBYe1BZnIFNvfQWJNDf2OZSEbd3SuYd#scrollTo=cRZ9exEO4WBP)

### Contributors
1. Fariha Fairoz `180041214`<br>
2. Samia Islam `180041237`<br>
3. M. K. Bashar `180041238`

### References
1. [YOLOv5](https://github.com/mikel-brostrom/Yolov5_DeepSort_OSNet.git)
2. [DeepSORT](https://github.com/nwojke/deep_sort)
3. [Tracktor](https://github.com/phil-bergmann/tracking_wo_bnw)
