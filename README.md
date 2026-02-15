# Mini Resume Collector API

A REST API built using FastAPI that allows uploading resumes and managing candidate metadata.

---

## Python Version

Python 3.10

---

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/miniresume-anfas-kk.git

2. Navigate into the project folder:

   cd miniresume-anfas-kk

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   Windows:
   venv\Scripts\activate

   Mac/Linux:
   source venv/bin/activate

5. Install dependencies:

   pip install -r requirements.txt

---

## Run the Application

uvicorn main:app --reload

Server will run at:

http://127.0.0.1:8000

API Documentation:

http://127.0.0.1:8000/docs

---

## API Endpoints

### 1. Health Check

GET /health

Response:

{
  "status": "healthy"
}

---

### 2. Upload Candidate

POST /candidates

Form Data Required:

- full_name
- dob (YYYY-MM-DD)
- contact_number
- contact_address
- education_qualification
- graduation_year
- experience_years
- skill_set (comma separated)
- resume_file (PDF/DOC/DOCX)

Response:

{
  "id": "uuid",
  "full_name": "Anfas KK",
  ...
}

---

### 3. List Candidates

GET /candidates

Optional Filters:

- skill
- experience
- graduation_year

Example:

GET /candidates?skill=Python&experience=2

---

### 4. Get Candidate by ID

GET /candidates/{candidate_id}

---

### 5. Delete Candidate

DELETE /candidates/{candidate_id}

Returns 204 No Content
