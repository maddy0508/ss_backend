from fastapi import FastAPI, Form
from schemas import SewingProject
from openai_client import client
from prompts import SYSTEM_PROMPT, garment_prompt

app = FastAPI()

@app.post("/generate", response_model=SewingProject)
async def generate(
    description: str = Form(""),
    sizing: str = Form(...)
):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": garment_prompt(description, sizing)},
        ],
        temperature=0.4,
    )

    return SewingProject.model_validate_json(
        response.choices[0].message.content
    )
