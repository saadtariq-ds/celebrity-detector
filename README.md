# 🌟 Celebrity Detector and Q&A

Celebrity Detector and Q&A is a **computer vision–powered AI application** that detects celebrities from uploaded images and allows users to ask natural-language questions about the detected individual. The system combines **image processing**, **vision-enabled LLM reasoning**, and a **cloud-native deployment pipeline**.

The project is designed to demonstrate **end-to-end AI application development**, from image preprocessing and inference to CI/CD automation and Kubernetes-based cloud deployment.

---

## 🚀 Key Features

- 📸 Celebrity detection from images
- 🧠 Vision-enabled LLM reasoning for contextual Q&A
- 🖼️ Image preprocessing using OpenCV
- 🌐 Flask-based backend APIs
- 🎨 Lightweight HTML/CSS frontend
- 🐳 Fully containerized using Docker
- 🔁 Automated CI/CD pipelines using CircleCI
- ☁️ Deployed on Google Kubernetes Engine (GKE)
- 📦 Docker images stored in Google Artifact Registry (GAR)
- 🔐 Cloud-ready and scalable architecture

---

## 🧱 System Architecture (High-Level)

1. User uploads an image via the web UI  
2. Flask backend receives and validates the image  
3. OpenCV preprocesses the image (resize, format conversion, etc.)  
4. Image is sent to **Groq Vision LLM (Llama-4 Vision Transformer)**  
5. Celebrity identity is detected  
6. User asks follow-up questions (Q&A)  
7. Groq LLM generates contextual answers  
8. CI/CD builds and deploys the app to GKE  

---

## 🛠️ Tech Stack

| Tool | Description |
|--------|------|
| Groq | Vision-enabled LLM (Llama-4 Vision Transformer) |
| OpenCV (Python) | Image preprocessing and manipulation |
| Flask | REST API for detection and Q&A workflows |
| HTML / CSS | Lightweight web interface |
| Docker | Application containerization |
| CircleCI | CI/CD pipeline automation |
| Google Artifact Registry (GAR) | Docker image storage |
| Google Kubernetes Engine (GKE) | Scalable cloud deployment |
| GitHub | Source code management (SCM) |

# ⚙️ Local Setup
## 1️⃣ Clone the Repository
```bash
git clone https://github.com/saadtariq-ds/celebrity-detector.git
cd celebrity-detector
```

## 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

## 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 4️⃣ Run the App
```bash
python app.py
```

