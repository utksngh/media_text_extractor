# Django Media Text Extraction API

## Overview
This project is a **Django REST Framework-based OCR (Optical Character Recognition) API** that extracts text from uploaded **PDFs and images (PNG, JPG, JPEG)** using **Tesseract OCR** and **pdf2image**.

## Features
Upload PDF and image files via API
Extract text using **Tesseract OCR**
Supports multiple languages (e.g., English, Hindi, etc.)
Stores extracted text in the database
REST API response with extracted text

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/django-ocr-project.git
cd media_api
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install System Dependencies
Make sure **Tesseract OCR** and **Poppler** are installed:

#### **For Ubuntu/Debian**
```bash
sudo apt install tesseract-ocr poppler-utils
```

#### **For macOS**
```bash
brew install tesseract poppler
```

#### **For Windows**
- Download & install **Tesseract OCR**: [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
- Download **Poppler**: [Poppler Windows](https://blog.alivate.com.au/poppler-windows/)

### 5. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Django Server
```bash
python manage.py runserver
```

---

## API Endpoints

### **1. Upload File & Extract Text**
**Endpoint:** `POST /upload/`

#### **Request:**
```
curl -X POST http://127.0.0.1:8000/api/upload/ -F "file=@news2.jpg"
```

#### **Response:**
```json
{"message":"File processed successfully","data":{"id":9,"file_name":"news2.jpg","content":"content","uploaded_at":"2025-02-23T21:13:57.377028Z"}}%
```

---

