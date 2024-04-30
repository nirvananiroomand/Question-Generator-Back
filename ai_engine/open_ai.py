import os
from openai import OpenAI
from dotenv import load_dotenv


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


if __name__ == '__main__':
    load_dotenv()
    generate_questions(content, quantity, difficulty, types_of_questions)

