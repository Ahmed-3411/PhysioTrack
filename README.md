# PhysioTrack

**Group Number:** W0223002  
**Team:** PhysioTrack Team  

---

## 📌 Abstract
PhysioTrack is an intelligent, integrated system designed to improve the home rehabilitation experience for knee injury patients through accurate monitoring, interactivity, and motivation. Statistics show that nearly 50% of patients struggle with adhering to home exercise routines, and over 70% of knee injuries require consistent physiotherapy. Additionally, more than 60% of patients face psychological challenges such as anxiety or depression during recovery.  

The system uses IMU and pressure sensors to track movements in real time, with AI providing instant audio feedback for correction. Through virtual reality, patients engage with a virtual trainer in a gym-like environment. To boost motivation and mental well-being, users earn points to customize a virtual character, making therapy both effective and engaging.

---

## 🎯 Key Features
- Real-time motion tracking using **IMU & pressure sensors**  
- **AI-powered feedback** for accurate exercise correction  
- **Virtual Reality trainer** in an interactive 3D environment  
- Gamified reward system (points & avatar customization)  
- Progress tracking with performance reports  
- Designed for both patients and physiotherapists  

---

## 🛠️ Methods & Materials
### Hardware Components
- MPU-6050 (Accelerometer + Gyroscope)  
- FSR-402 (Force Sensitive Resistor)  
- Raspberry Pi  
- Display Screen  
- Development Laptop/PC  

### Software Components
- AI Algorithms for movement analysis  
- VR Environment (Unity & Oculus)  
- 3D Virtual Trainer  
- Reward Points System  

---

## 📊 Results
- **96% accuracy** in exercise tracking  
- **80% increase** in user satisfaction due to VR + AI integration  
- High patient engagement and improved psychological well-being  

---

## 🚀 Recommendations
1. Expand injury database (knee, shoulder, spine, ankle).  
2. Collaborate with physiotherapists for personalized plans.  
3. Partner with clinics and hospitals for integration.  
4. Add chatbot/virtual assistant for live guidance.  
5. Improve UI/UX based on patient feedback.  
6. Offer device versions for different age groups.  
7. Build a community feature for progress sharing.  

---

## 💼 Business Model Canvas
- **Key Partners:** Physiotherapy centers, hospitals, sensor tech companies, cloud providers.  
- **Value Proposition:** Smart, interactive, safe, and motivational physiotherapy at home.  
- **Customer Segments:** Knee injury patients (18–50), rehabilitation clinics, medical institutions.  
- **Revenue Streams:** Device sales, monthly subscriptions, loyalty incentives.  

---

## 📈 Cost & Revenue Model
- **Cost per product:** ~EGP 3500  
- **Selling price:** ~EGP 4400 (+20% margin)  
- **Monthly profit (15 devices):** ~EGP 13,500  
- **Annual profit:** ~EGP 162,000  
- **Subscription revenue:** ~EGP 27,000 yearly  

---

## 🔮 Future Work
- Personalized treatment plans  
- AI-powered smart virtual trainer  
- Advanced VR interaction  
- Multi-injury rehabilitation support  

---

## 📚 References
1. Alalou, Dr. Samar Sassi (2024). *Difficulties faced by the patient for not adhering to his treatment sessions in physiotherapy centers.*  
2. Ali, M. (n.d.). *The chaos of physiotherapy in Egypt.*  
3. Harvard Health. *Health information and medical information.*  
4. TigaHealth. *Mobithera - Physical Therapy and Telemedicine App.*  
5. Physiapp. *VisiApp®: Personalized Physical Therapy and Telehealth Platform.*  

---

## 🔧 Dependencies
### Python Libraries
```txt
```
# Core scientific libraries
numpy
pandas
scipy
scikit-learn
```
```
# Deep learning frameworks
tensorflow
torch
torchvision
```
```
# ONNX model support
onnx
onnxruntime
```
```
# Computer vision
opencv-python
mediapipe
```
```
# Visualization & data analysis
matplotlib
seaborn
notebook
```
```
# Hardware / IoT communication
pyserial
smbus2   # for I2C sensors on Raspberry Pi
RPi.GPIO # if using Raspberry Pi GPIO pins
```
```
# Game engine / VR interaction (Python side)
pygame
```
