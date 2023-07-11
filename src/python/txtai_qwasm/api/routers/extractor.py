from fastapi import APIRouter, Body
import spacy

from .. import application

router = APIRouter()
nlp = spacy.load("en_core_web_sm")

@router.post("/qwasm")
def qwasm_handler(text: str = Body(...)):
    doc = nlp(text)
    analyzed_data = {
        "question_word": None,
        "auxiliary_verb": None,
        "subject": None,
        "main_verb": None
    }

    for token in doc:
        if token.dep_ == "aux":
            analyzed_data["auxiliary_verb"] = token.text
        elif token.dep_ == "nsubj":
            analyzed_data["subject"] = token.text
        elif token.dep_ == "ROOT":
            analyzed_data["main_verb"] = token.text
        elif token.dep_ == "punct" and token.text == "?":
            analyzed_data["question_word"] = doc[token.i - 1].text if token.i > 0 else None

    return [{"name": "qwasm", "result": analyzed_data}]
