# Lead Scoring API with LLM

This FastAPI project uses OpenAI's GPT model to score leads based on their quality, intent, and fit.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY=your-api-key-here
```

3. Run the server:
```bash
uvicorn lead_scoring_api:app --reload
```

## Endpoints

- `GET /generate_lead`: Generates a random lead.
- `POST /score_lead`: Generates and scores a lead using GPT.
