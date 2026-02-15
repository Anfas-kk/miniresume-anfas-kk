from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from uuid import uuid4
import os
import shutil
from datetime import date

app = FastAPI(
    title="Mini Resume Collector API",
    description="API to upload and manage candidate resumes",
    version="2.0.0"
)

# In-memory storage
candidates = []

# Create uploads directory
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Response Model
class CandidateResponse(BaseModel):
    id: str
    full_name: str
    dob: date
    contact_number: str
    contact_address: str
    education_qualification: str
    graduation_year: int
    experience_years: int
    skill_set: List[str]
    resume_file: str


# Health Check
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Upload Resume
@app.post("/candidates", response_model=CandidateResponse, status_code=201)
async def upload_candidate(
    full_name: str = Form(...),
    dob: date = Form(...),
    contact_number: str = Form(...),
    contact_address: str = Form(...),
    education_qualification: str = Form(...),
    graduation_year: int = Form(...),
    experience_years: int = Form(...),
    skill_set: str = Form(...),  # comma-separated
    resume_file: UploadFile = File(...)
):

    # Validate file type
    allowed_extensions = [".pdf", ".doc", ".docx"]
    file_ext = os.path.splitext(resume_file.filename)[1].lower()

    if file_ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Invalid file type")

    candidate_id = str(uuid4())

    file_path = os.path.join(UPLOAD_FOLDER, f"{candidate_id}_{resume_file.filename}")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume_file.file, buffer)

    candidate_data = {
        "id": candidate_id,
        "full_name": full_name,
        "dob": dob,
        "contact_number": contact_number,
        "contact_address": contact_address,
        "education_qualification": education_qualification,
        "graduation_year": graduation_year,
        "experience_years": experience_years,
        "skill_set": [skill.strip() for skill in skill_set.split(",")],
        "resume_file": file_path
    }

    candidates.append(candidate_data)

    return candidate_data


# List Candidates with Filters
@app.get("/candidates", response_model=List[CandidateResponse])
def list_candidates(
    skill: Optional[str] = None,
    experience: Optional[int] = None,
    graduation_year: Optional[int] = None
):

    results = candidates

    if skill:
        results = [c for c in results if skill.lower() in [s.lower() for s in c["skill_set"]]]

    if experience is not None:
        results = [c for c in results if c["experience_years"] == experience]

    if graduation_year is not None:
        results = [c for c in results if c["graduation_year"] == graduation_year]

    return results


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
            return
    raise HTTPException(status_code=404, detail="Candidate not found")
