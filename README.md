# PhysioTrack: An Intelligent AI and IoT System for Smart Physical Rehabilitation

![Logo](Figers/logo8.png)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](#)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?logo=tensorflow&logoColor=white)](#)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?logo=pytorch&logoColor=white)](#)
[![ONNX](https://img.shields.io/badge/ONNX-Interoperability-005CED?logo=onnx&logoColor=white)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white)](#)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Pose%20Estimation-FF6F00?logo=google&logoColor=white)](#)
[![Unity](https://img.shields.io/badge/Unity-Game%20Engine-000000?logo=unity&logoColor=white)](#)
[![C%23](https://img.shields.io/badge/C%23-Unity%20Scripts-239120?logo=c-sharp&logoColor=white)](#)
[![Barracuda](https://img.shields.io/badge/Unity-Barracuda%20ONNX-FF4154?logo=unity&logoColor=white)](#)
[![Oculus](https://img.shields.io/badge/Oculus-VR%20Integration-1C1E20?logo=oculus&logoColor=white)](#)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-IoT%20Integration-A22846?logo=raspberrypi&logoColor=white)](#)

---

##  Abstract

Physical rehabilitation is essential for restoring mobility and improving the quality of life after knee injuries. However, patient adherence remains a major challenge due to monotony, lack of motivation, and absence of real-time corrective feedback.

**PhysioTrack** is an intelligent system that integrates **AI**, **IoT sensors**, and **Virtual Reality (VR)** to transform rehabilitation into an interactive, adaptive, and data-driven process.

The system uses IMU and pressure sensors to capture real-time motion data, which is processed by an ONNX-converted MLP model running on the edge. VR gamification provides audiovisual guidance and boosts patient motivation.

Experimental results show:
- **96.2% accuracy** in squat classification  
- **80% improvement in user satisfaction** vs traditional methods  

This study demonstrates the potential of AI-driven, home-based physiotherapy systems to enhance accessibility, engagement, and recovery outcomes.

---

##  Key Features
- Real-time motion tracking via **IMU + FSR sensors**  
- **AI-powered feedback** for exercise correction  
- **Virtual Reality coach** in an interactive 3D environment  
- Gamified avatar customization system  
- Performance tracking and progress reports  
- Designed for both patients & physiotherapists  

---

##  Methods & Materials

### Hardware Components
- **MPU-6050** (Accelerometer + Gyroscope)  
- **FSR-402** (Force Sensor)  
- **Raspberry Pi**  
- Display Screen  
- Laptop/PC (Unity + AI Development)

### Software Stack
- AI Motion Analysis (TensorFlow / PyTorch → ONNX)  
- Unity VR Environment + Oculus Integration  
- Real-time feedback system  
- Gamification mechanics  

### System Pipeline  
![Pipeline](Figers/pipeline_1%20(1).png)

---

##  Experimental Results

### Confusion Matrix  
![Confusion Matrix](Figers/confusion_matrix.jpg)

### Feature Heatmap  
![Feature Heatmap](Figers/feature_heatmap.jpg)

### ROC Curve  
![Operating Characteristic](Figers/Fig5_ROC.png)

---

##  VR Scenes & Visualization

### VR Scene Samples
![Scene 1](Figers/vr_scene1.jpg)  
![Scene 2](Figers/vr_scene2.jpg)  
![Scene 3](Figers/vr_scene3.jpg)

---

##  Future Work
- Personalized rehab plans  
- Advanced VR interaction  
- Full-body motion tracking  
- AI-driven smart virtual trainer  

---

## 📚 Citation

If you use **PhysioTrack** in your research, please cite:

```
Ahmed Talaat Mersal, Awab Mostafa, Salsabil Mostafa, Farha Farghaly, Arwa Eisa.
PhysioTrack: An Intelligent AI and IoT System for Smart Physical Rehabilitation.
TechRxiv, 2025.
DOI: 10.36227/techrxiv.176238015.59132608/v1
```

---
