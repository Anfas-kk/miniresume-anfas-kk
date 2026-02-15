# Mini Resume Collector API

A RESTful API built using FastAPI to upload resumes, store candidate metadata, categorize candidates based on experience, and filter/search candidates via API.  

This project demonstrates backend API design, file handling, validation, filtering, and basic frontend integration.

---

## 🚀 Features

- Upload resumes (PDF/DOC/DOCX)
- Store candidate metadata in memory
- Prevent duplicate email submissions
- File type and file size validation (Max 5MB)
- Automatic candidate categorization (Junior / Mid / Senior)
- Filter candidates by:
  - Skill
  - Experience
  - Graduation Year
- Pagination support (limit & offset)
- Delete candidate by ID
- Simple frontend UI for uploading resumes
- REST-compliant endpoints

---

## 🐍 Python Version

Python 3.10+

---

## 📦 Installation

1. Clone the repository:

   git clone https://github.com/your-username/miniresume-anfas-kk.git

2. Navigate into the project:

   cd miniresume-anfas-kk

3. Create virtual environment:

   python -m venv venv

4. Activate virtual environment:

   Windows:
   venv\Scripts\activate

   Mac/Linux:
   source venv/bin/activate

5. Install dependencies:

   pip install -r requirements.txt

---

## ▶️ Run the Application

uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000

Interactive API Docs:

http://127.0.0.1:8000/docs

Frontend UI:

http://127.0.0.1:8000/

---

## 📌 API Endpoints

### 1️⃣ Health Check

GET /health

Response:

{
  "status": "healthy"
}

---

### 2️⃣ Upload Candidate

POST /candidates

Form Fields:

- full_name
- email
- dob (YYYY-MM-DD)
- contact_number
- contact_address
- education_qualification
- graduation_year
- experience_years
- skill_set (comma separated values)
- resume_file (PDF/DOC/DOCX)

Example Response:

{
  "id": "uuid",
  "full_name": "Anfas KK",
  "email": "anfas@example.com",
  "experience_years": 3,
  "level": "Mid",
  "created_at": "2026-02-15T10:00:00"
}

---

### 3️⃣ List Candidates

GET /candidates

Optional Query Parameters:

- skill
- experience
- graduation_year
- limit (default: 10)
- offset (default: 0)

Example:

GET /candidates?skill=Python&experience=3

---

### 4️⃣ Get Candidate by ID

GET /candidates/{candidate_id}

---

### 5️⃣ Delete Candidate

DELETE /candidates/{candidate_id}

Returns: 204 No Content

---

## 🏗 Project Structure

miniresume-anfas-kk/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── static/
    └── index.html

---

## 🧠 Design Decisions

- In-memory storage used as per assignment requirement.
- File uploads stored locally in `uploads/` directory.
- Validation handled using Pydantic.
- Business logic separated using utility functions.
- Pagination implemented for scalability.
- Duplicate email prevention to ensure data integrity.
