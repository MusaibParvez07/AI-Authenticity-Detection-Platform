# 🧠 AI Authenticity Detection Platform

**A full-stack AI platform for detecting AI-generated and manipulated content across text and images — powered by transformer-based NLP, computer vision, and a secure FastAPI backend.**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/🤗%20Transformers-NLP%20%26%20ViT-FFD21E)](https://huggingface.co/transformers/)
[![Status](https://img.shields.io/badge/Status-Ongoing-yellow)]()

---

## 📖 Overview

Generative AI can now produce text and images convincing enough to pass as human-made — which makes telling authentic content from synthetic or manipulated content a growing, real-world problem for platforms, publishers, and moderators.

This project tackles that problem head-on: a **full-stack authenticity detection platform** that unifies **NLP and Vision Transformer models** into a single pipeline to flag AI-generated or manipulated **text and images**, backed by a secure, production-shaped **FastAPI** service and a web interface for submitting content and reviewing results.

> 🚧 **Status: Actively in development.** Core detection pipelines, authentication, and evaluation tooling are functional; model accuracy, multimodal detection, and the frontend experience are being actively refined.

---

## ✨ Key Features

### 🤖 AI-Based Detection
- Dedicated inference pipelines for **image** and **text** authenticity analysis
- Prediction results returned with **confidence scores**
- Modular preprocessing pipelines per content type
- Centralized model loading and inference services

### 🖼️ Image Analysis
- CNN / Vision Transformer-based image classification pipeline
- Image preprocessing and normalization before inference
- Flags likely-manipulated or AI-generated images

### 📝 Text Analysis
- Transformer-based NLP pipeline for text classification
- Tokenization and max-length handling for long-form input
- Distinguishes human-written from AI-generated text

### 🔐 Authentication & Security
- JWT-based access tokens with expiry and validation
- Password hashing and verification
- Protected API endpoints via authentication dependencies
- No secrets committed to source control — environment-variable-driven config

### 🌐 REST API (FastAPI)
- Modular route structure: **auth**, **detection**, **app operations**, **health/status**
- Auto-generated interactive API docs via FastAPI's OpenAPI integration
- Pydantic-validated request/response schemas

### 📊 Evaluation
- Dedicated evaluation module for benchmarking model performance
- Structured backend test suite for pipeline reliability

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend Framework | FastAPI |
| Language | Python 3.9+ |
| Deep Learning | PyTorch |
| NLP / Text Models | 🤗 Transformers, LLMs |
| Vision Models | CNN, Vision Transformers, OpenCV |
| Data Validation | Pydantic |
| Numerical Processing | NumPy |
| Authentication | JWT, password hashing |
| Frontend | JavaScript, HTML, CSS |

---

## 🏗️ Architecture

```
User Input
    │
    ▼
Frontend (Web UI)
    │
    ▼
FastAPI Backend
    │
    ▼
Input Preprocessing  ──▶  Text Pipeline (Transformers/NLP)
    │                 └─▶ Image Pipeline (CNN / ViT)
    ▼
Model Inference
    │
    ▼
Prediction + Confidence Score
    │
    ▼
Frontend (Results Display)
```

Authentication runs in parallel: credentials → password verification → JWT issuance → protected-route validation on every subsequent request.

---

## 📸 Screenshots

> _Screenshots coming soon — this section will showcase the detection UI, prediction results, and dashboard once available._

<!--
| Home / Upload | Detection Result |
|---|---|
| ![Home](Screenshots/home.png) | ![Result](Screenshots/result.png) |
-->

---

## 📁 Project Structure

```
AI-Authenticity-Detection-Platform/
├── backend/
│   ├── ai/
│   │   ├── image/          # Image preprocessing, CNN/ViT inference
│   │   └── text/           # Tokenization, transformer inference
│   ├── api/                # FastAPI routes (auth, detection, health)
│   ├── app/                # Application entry point
│   ├── database/           # Database components
│   ├── evaluation/         # Model evaluation & benchmarking
│   ├── security/           # JWT, password hashing, auth deps
│   ├── services/           # Shared application services
│   └── tests/               # Backend test suite
├── frontend/                # Web interface
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Requirements
- Python 3.9+
- Git
- A modern web browser
- (Additional system dependencies may be required for AI/ML libraries)

### 1. Clone the repository
```bash
git clone https://github.com/MusaibParvez07/AI-Authenticity-Detection-Platform.git
cd AI-Authenticity-Detection-Platform
```

### 2. Create a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the application
Review the configuration files inside `backend/` before starting the app. **Never commit** API keys, passwords, JWT secrets, or database credentials — supply them via environment variables.

### 5. Start the backend
```bash
uvicorn backend.app.main:app --reload
```
- API: `http://127.0.0.1:8000`
- Interactive docs: `http://127.0.0.1:8000/docs`

### 6. Start the frontend
```bash
cd frontend
npm install
```
Then run the project's configured frontend dev command.

---

## 🔐 Authentication Flow

1. User submits credentials to the auth API
2. Password is verified via the project's hashing implementation
3. A JWT access token is issued on success
4. Protected endpoints validate the token on every request
5. Invalid or expired tokens are rejected

Core components live under `backend/api/` and `backend/security/`.

---

## 🔭 Roadmap

- [ ] Additional AI-generated content detection models
- [ ] Improved multimodal detection (combined text + image signals)
- [ ] Detailed confidence/explainability analysis
- [ ] Model evaluation dashboards
- [ ] Support for additional media formats
- [ ] Detection history and audit trail
- [ ] Improved frontend visualization
- [ ] Automated model benchmarking
- [ ] Production deployment configuration

---

⭐ If you find this project interesting, consider giving it a star!
