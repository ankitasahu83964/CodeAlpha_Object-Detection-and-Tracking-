# CodeAlpha Object Detection & Tracking 🎯

## 📌 Description
This project is an Object Detection and Tracking system developed during the CodeAlpha AI Internship.  
It uses YOLOv8 for real-time object detection and SORT algorithm for tracking objects with unique IDs.

The system includes both backend processing (Python) and frontend interface (HTML, CSS, JavaScript).

---

## 🚀 Features
- Real-time object detection using YOLOv8  
- Object tracking using SORT algorithm  
- Unique ID assigned to each detected object  
- Live video streaming in browser  
- Simple and interactive frontend UI  

---

## 🧠 How It Works
- The backend (`app.py`) uses YOLOv8 model (`yolov8n.pt`) to detect objects  
- SORT algorithm (`sort.py`) tracks objects across frames  
- Processed video frames are sent to frontend  
- Frontend displays results with bounding boxes and object count  

---

## 🛠️ Technologies Used
- Python  
- OpenCV  
- YOLOv8  
- SORT Algorithm  
- HTML  
- CSS  
- JavaScript  



## 📂 Project Structure

ObjectDetection/
│
├── backend/
│   ├── app.py
│   ├── sort.py
│  
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── model/
│   └── yolov8n.pt
│
├── data/
│   └── data.csv
│
├── output/
│   └── (optional: output videos)
│
├── README.md
└── .gitignore
