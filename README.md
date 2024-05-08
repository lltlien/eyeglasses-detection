<!-- Banner -->
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: none;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<h1 align="center"><b>NHẬP MÔN THỊ GIÁC MÁY TÍNH</b></h>

## THÀNH VIÊN NHÓM
| STT    | MSSV          | Họ và Tên              |Chức Vụ    | Github                                                  | Email                   |
| ------ |:-------------:| ----------------------:|----------:|--------------------------------------------------------:|-------------------------:
| 1      | 21522282      | Lê Thị Liên            |Nhóm trưởng|[lltlien   ](https://github.com/lltlien)                 |21522282@gm.uit.edu.vn   |
| 2      | 21522883      | Võ Thị Phương Anh      |Thành viên |[vtpanh](https://github.com/vtpanh)                      |21522883@gm.uit.edu.vn   |


## GIỚI THIỆU MÔN HỌC
* **Tên môn học:** Nhập môn thị giác máy tính
* **Mã môn học:** CS231
* **Mã lớp:** CS231.N21.KHTN
* **Năm học:** HK2 (2022 - 2023)
* **Giảng viên**: TS.Mai Tiến Dũng

## OVERVIEW
This repository contains the source code for an eyeglasses detection system developed as part of the CS231 Computer Vision course. The project focuses on implementing algorithms and techniques for detecting eyeglasses in images.


### DEMO
Input                           | Output
:-------------------------:|:-------------------------:
<img src="image/lop1.jpg" alt="drawing" width="600"/>|<img src="image/353881009_1418968438868360_6477163176620041733_n.png" alt="drawing" width="600"/>

Installation
---------------
```
git clone https://github.com/lltlien/eyeglasses-detection.git
cd eyeglasses-detection
```

Dependencies
---------------
```
deepface==0.0.68
opencv-python==4.5.5.62
numpy==1.24.3
imutils==0.5.4
tensorflow==2.0.1
scikit-learn==0.24.1
matplotlib==3.5.1
```

Training
---------------
- To train the eyeglasses detection model using MobileNetV2.
 ```
python train_mobilenetv2_model.py
```
- To train the eyeglasses detection model using ResNet101V2.
```
python train_resnetv2.py
```
- Save trained model to predict.

Prediction
---------------
To detect all faces in an image and then predict eyeglasses using the trained models.
```
python image_prediction_using_deep_face.py
```
