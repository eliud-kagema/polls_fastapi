from fastapi import FastAPI, HTTPException, Response, Depends
import schema
from typing import List

from sqlalchemy.orm import Session

import crud
from database import SessionLocal, engine
from models import Base


# Creates the databse tables by using th SQLAlchemy models defined in models.py file
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


## Question

@app.post("/questions/", response_model=schema.QuestionInfo)
def create_question(question: schema.QuestionCreate, db: Session = Depends(get_db)):
    """
    Create a polls question
    """
    return crud.create_question(db=db, question=question)


@app.get("/questions/", response_model=List[schema.Question])
def get_questions(db: Session = Depends(get_db)):
    """
    List all questions
    """
    return crud.get_all_questions(db=db)



def get_question_obj(db, qid):
    obj = crud.get_question(db=db, qid=qid)
    if obj is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return obj



@app.get("/questions/{qid}", response_model=schema.QuestionInfo)
def get_question(qid: int, db: Session = Depends(get_db)):
    """
    Retrive a question
    """
    return get_question_obj(db=db, qid=qid)
	
@app.put("/questions/{qid}", response_model=schema.QuestionInfo)
def edit_question(qid: int, question: schema.QuestionCreate, db: Session = Depends(get_db)):
    """
    Edit a question
    """
    get_question_obj(db=db, qid=qid)
    obj = crud.edit_question(db=db, qid=qid, question=question)
    return obj

@app.delete("/questions/{qid}")
def delete_question(qid: int, db: Session = Depends(get_db)):

    """
    Delete a question
    """
    get_question_obj(db=db, qid=qid)
    crud.delete_question(db=db, qid=qid)
    return {"detail": "Question deleted", "status_code": 204}