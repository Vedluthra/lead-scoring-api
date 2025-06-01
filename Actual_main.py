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

def score_lead_custom_logic(lead: LeadInput) -> dict:
    
    score = 0

    # Example scoring logic (basic, customizable):
    if "demo" in lead.inquiry_message.lower():
        score += 40
    if lead.title.lower() in ["ceo", "cto", "founder"]:
        score += 30
    if lead.source_channel.lower() in ["website", "referral", "linkedin"]:
        score += 20
    if lead.industry.lower() in ["saas", "software", "tech"]:
        score += 10

    # Clamp score between 0 and 100
    score = max(0, min(score, 100))

    # Categorize the score
    if score >= 80:
        category = "Hot"
    elif score >= 60:
        category = "Warm"
    else:
        category = "Cold"

    return {
        "score": score,
        "category": category
    }

@app.post("/score_custom_lead")
def score_custom_lead(lead: LeadInput):
    return score_lead_custom_logic(lead)
