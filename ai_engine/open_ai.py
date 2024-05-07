import os
from openai import OpenAI


def generate_questions(content: str, difficulty: str, types_of_questions: dict):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY2"))

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": "You are an expert teaching assistant who can make great questions out of a given context."},
            {"role": "user", "content": f"""please provide {types_of_questions} {difficulty} question(s) from this text:{content}"""}  
        ]
    )

    return completion.choices[0].message.content
