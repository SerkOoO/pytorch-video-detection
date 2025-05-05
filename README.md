# 🙂 Pytorch Video Detection

**Pytorch Video Detection** is a small project that allows you to upload a video, and a pre-trained model will predict the action occurring in the video.

---

## 🛠️ Technologies Used

### Backend
- 🐍 Python
- ⚡ FastAPI
- 🎥 OpenCV
- 🔥 PyTorch

### Frontend
- ⚛️ Next.js

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/SerkOoO/pytorch-video-detection.git
cd pytorch-video-detection
```

## 🐳 Running with Docker
```bash
docker-compose build
docker-compose up
```
---

## Without Docker

### Backend
```bash
cd Backend
python3 -m  venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
fastapi dev
```

### Frontend
```bash
cd Frontend
npm install
npm run dev
```



