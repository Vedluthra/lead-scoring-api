from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LeadInput(BaseModel):
    name: str
    email: str
    company: str
    title: str
    inquiry_message: str
    source_channel: str
    industry: str

# logic
def score_lead_custom_logic(lead: LeadInput) -> dict:
    score = 85  # Dummy score
    explanation = "High intent, relevant role, came via demo request"
    return {"score": score, "category": "Hot", "explanation": explanation}

@app.post("/score_custom_lead")
def score_custom_lead(lead: LeadInput):
    return score_lead_custom_logic(lead)






