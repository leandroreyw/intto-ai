from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Define request model
class InterviewRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: InterviewRequest):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert in startup customer discovery. Guide the user to ask open-ended, non-leading questions that reveal real customer pain points."},
            {"role": "user", "content": request.question}
        ]
    )
    return {"response": response["choices"][0]["message"]["content"]}