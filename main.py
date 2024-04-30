from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai_engine.open_ai import generate_questions 
from typing import Dict


class QuestionRequest(BaseModel):
    typesWithQuantities: Dict[str, int]
    difficulty: str
    content: str
    

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate")
async def generate_questions_api(request_data: QuestionRequest):
    types_with_quantities = request_data.typesWithQuantities
    difficulty = request_data.difficulty
    content = request_data.content
    generated_questions = generate_questions(content=content, difficulty=difficulty, types_of_questions=types_with_quantities)
    return generated_questions


@app.get("/test")
async def test_api():
    return {"data": "this is the test API"}
