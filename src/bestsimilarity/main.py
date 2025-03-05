import typing
import pydantic

from fastapi import FastAPI, HTTPException
from src.bestsimilarity.bestSimilarityFinder import findBestSimilarity

api = FastAPI()

class InputTitles(pydantic.BaseModel):
    reference: str
    other: typing.List[str]

@api.post("/bestSimilarity/")
def getBestSimilarity(titles: InputTitles):
    if not titles.reference:
        raise HTTPException(status_code=400, detail="No reference title in the request")
    if not titles.other:
        raise HTTPException(status_code=400, detail="No titles to match against the reference in the request")
    return {"top_result": findBestSimilarity(titles.reference, titles.other)}
