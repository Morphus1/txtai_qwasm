from fastapi import APIRouter, Body
from typing import List, Optional
import spacy

from .. import application

router = APIRouter()
nlp = spacy.load("en_core_web_sm")

@router.post("/qwasm")
def qwasm_handler(queue: List[dict] = Body(...), texts: Optional[List[str]] = Body(default=None)):
    analyzed_texts = []
    for text in texts:
        doc = nlp(text)
        analyzed_data = [token.text for token in doc]
        analyzed_texts.append(analyzed_data)
    
    return application.get().qwasm_handler(analyzed_texts)