from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# CRITICAL: Allow your phone to talk to your computer/server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Flashcard(BaseModel):
    question: str
    answer: str

# Your "Source of Truth" for the app
study_data = [
    {"question": "What is Backpropagation?", "answer": "The primary algorithm for training neural networks by calculating gradients."},
    {"question": "What is a Tensor?", "answer": "A multi-dimensional array, the main data structure in AI frameworks."},
]

@app.get("/cards")
def get_cards():
    return study_data

@app.post("/add-card")
def add_card(card: Flashcard):
    study_data.append(card.dict())
    return {"message": "Success"}