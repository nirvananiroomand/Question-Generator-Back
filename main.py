from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine.open_ai import generate_questions

class Item(BaseModel):
    content: str
    difficulty: str
    types_of_questions: dict
    

app = FastAPI()


@app.post("/generate")
async def create_item(item: Item):
    print(item)
    questions = generate_questions(item.content, item.difficulty, item.types_of_questions)
    print("QUESTIONS:")
    print(questions)
    return {"questions": questions}


@app.get("/test")
async def test_api():
    return {"data": "this is the test API"}