from fastapi import FastAPI
from pydantic import BaseModel
from question_generator import (
    generate_questions
)
from scorer import score_answer
from followup import generate_followup
from database import (
    get_leaderboard
)
from database import (
    get_user_profile
)
from database import (
    get_all_records
)

class AnswerRequest(BaseModel):

    question:str

    answer:str

app = FastAPI()

@app.get("/questions/{job}")
def get_questions(job):

    return generate_questions(job)

@app.post("/score")
def score(data:AnswerRequest):

    score, feedback = score_answer(
        data.question,
        data.answer
    )

    return {
        "score":score,
        "feedback":feedback
    }

@app.post("/followup")
def followup(data:AnswerRequest):

    return {
        "followup":
        generate_followup(
            data.question,
            data.answer
        )
    }

@app.get("/leaderboard")
def leaderboard():

    return get_leaderboard()

@app.get("/profile/{username}")
def profile(username):

    return get_user_profile(
        username
    )

@app.get("/history")
def history():

    return get_all_records()