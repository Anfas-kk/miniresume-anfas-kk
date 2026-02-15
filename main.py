from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from uuid import uuid4
from datetime import date, datetime
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import os
# import shutil

app = FastAPI(
    title="Mini Resume Collector API",
    description="API to upload and manage candidate resumes",
    version="2.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory storage
candidates = []

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Response Model
class CandidateResponse(BaseModel):
    id: str
    full_name: str
    email: EmailStr
    dob: date
    contact_number: str
    contact_address: str
    education_qualification: str
    graduation_year: int
    experience_years: int
    skill_set: List[str]
    level: str
    created_at: datetime
    resume_file: str

# Utility Function
def categorize_candidate(experience: int) -> str:
    if experience >= 5:
        return "Senior"
    elif experience >= 2:
        return "Mid"
    else:
        return "Junior"

# Home Route
@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r") as file:
        return file.read()

# Health Check
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Upload Candidate
@app.post("/candidates", response_model=CandidateResponse, status_code=201)
async def upload_candidate(
    full_name: str = Form(...),
    email: EmailStr = Form(...),
    dob: date = Form(...),
    contact_number: str = Form(...),
    contact_address: str = Form(...),
    education_qualification: str = Form(...),
    graduation_year: int = Form(...),
    experience_years: int = Form(...),
    skill_set: str = Form(...),  
    resume_file: UploadFile = File(...)
):

    # Duplicate email check
    for candidate in candidates:
        if candidate["email"] == email:
            raise HTTPException(
                status_code=400,
                detail="Candidate with this email already exists"
            )

    # Validate file extension
    allowed_extensions = [".pdf", ".doc", ".docx"]
    file_ext = os.path.splitext(resume_file.filename)[1].lower()

    if file_ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # File size validation (5MB max)
    MAX_FILE_SIZE = 5 * 1024 * 1024
    contents = await resume_file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 5MB limit"
        )

    # Generate ID
    candidate_id = str(uuid4())
    file_path = os.path.join(
        UPLOAD_FOLDER,
        f"{candidate_id}_{resume_file.filename}"
    )

    # Save file
    with open(file_path, "wb") as buffer:
        buffer.write(contents)

    # Process skills
    skills_list = [skill.strip() for skill in skill_set.split(",")]

    # Categorization
    level = categorize_candidate(experience_years)

    # Create candidate object
    candidate_data = {
        "id": candidate_id,
        "full_name": full_name,
        "email": email,
        "dob": dob,
        "contact_number": contact_number,
        "contact_address": contact_address,
        "education_qualification": education_qualification,
        "graduation_year": graduation_year,
        "experience_years": experience_years,
        "skill_set": skills_list,
        "level": level,
        "created_at": datetime.utcnow(),
        "resume_file": file_path
    }

    candidates.append(candidate_data)

    return candidate_data

# List Candidates (with filters + pagination)
@app.get("/candidates", response_model=List[CandidateResponse])
def list_candidates(
    skill: Optional[str] = None,
    experience: Optional[int] = None,
    graduation_year: Optional[int] = None,
    limit: int = 10,
    offset: int = 0
):

    results = candidates

    if skill:
        results = [
            c for c in results
            if skill.lower() in [s.lower() for s in c["skill_set"]]
        ]

    if experience is not None:
        results = [
            c for c in results
            if c["experience_years"] == experience
        ]

    if graduation_year is not None:
        results = [
            c for c in results
            if c["graduation_year"] == graduation_year
        ]

    return results[offset: offset + limit]

# Get Candidate by ID
@app.get("/candidates/{candidate_id}", response_model=CandidateResponse)
def get_candidate(candidate_id: str):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate

    raise HTTPException(status_code=404, detail="Candidate not found")

# Delete Candidate
@app.delete("/candidates/{candidate_id}", status_code=204)
def delete_candidate(candidate_id: str):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            candidates.remove(candidate)

            # Optional: remove file from disk
            if os.path.exists(candidate["resume_file"]):
                os.remove(candidate["resume_file"])

            return

    raise HTTPException(status_code=404, detail="Candidate not found")
