# Mini Resume Collector API

<<<<<<< HEAD
A REST API built using FastAPI that allows uploading resumes and managing candidate metadata.
=======
A REST API built using FastAPI to upload resumes, store candidate metadata, categorize candidates by experience level, and search/filter candidates.
>>>>>>> 4dc6df5 (Enhanced API with email validation, file size checks, categorization, and updated README)

---

## Python Version

<<<<<<< HEAD
Python 3.10
=======
Python 3.10+
>>>>>>> 4dc6df5 (Enhanced API with email validation, file size checks, categorization, and updated README)

---

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/miniresume-anfas-kk.git

<<<<<<< HEAD
2. Navigate into the project folder:

   cd miniresume-anfas-kk

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:
=======
2. Navigate into the project directory:

   cd miniresume-anfas-kk

3. Create virtual environment:

   python -m venv venv

4. Activate virtual environment:
>>>>>>> 4dc6df5 (Enhanced API with email validation, file size checks, categorization, and updated README)

   Windows:
   venv\Scripts\activate

   Mac/Linux:
   source venv/bin/activate

5. Install dependencies:

   pip install -r requirements.txt

---

## Run the Application

uvicorn main:app --reload

<<<<<<< HEAD
Server will run at:
=======
Server runs at:
>>>>>>> 4dc6df5 (Enhanced API with email validation, file size checks, categorization, and updated README)

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
<<<<<<< HEAD
=======
- email
>>>>>>> 4dc6df5 (Enhanced API with email validation, file size checks, categorization, and updated README)
- dob (YYYY-MM-DD)
- contact_number
- contact_address
- education_qualification
- graduation_year
- experience_years
<<<<<<< HEAD
- skill_set (comma separated)
- resume_file (PDF/DOC/DOCX)

Response:
=======
- skill_set (comma separated values)
- resume_file (PDF/DOC/DOCX)

Response Example:
>>>>>>> 4dc6df5 (Enhanced API with email validation, file size checks, categorization, and updated README)

{
  "id": "uuid",
  "full_name": "Anfas KK",
<<<<<<< HEAD
=======validation, file size checks, categorization, and updated README)
  ...
}

---

### 3. List Candidates

GET /candidates

Optional Filters:

- skill
- experience
- graduation_year
<<<<<<< HEAD

Example:

GET /candidates?skill=Python&experience=2
=======
- limit (default 10)
- offset (default 0)

Example:

GET /candidates?skill=Python&experience=3
>>>>>>> 4dc6df5 (Enhanced API with email validation, file size checks, categorization, and updated README)

---

### 4. Get Candidate by ID

GET /candidates/{candidate_id}

---

### 5. Delete Candidate

DELETE /candidates/{candidate_id}

Returns 204 No Content
