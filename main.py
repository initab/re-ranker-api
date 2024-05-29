import json
import os

from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import cross_encoder


config_path = os.getenv("RE_RANKER_API_CONF", "config.json")
with open(config_path, "r") as f:
    config = json.load(f)

app = FastAPI(root_path=config["root"])

encoder = cross_encoder.CrossEncoder(model_name=config["model"],
                                     num_labels=1,
                                     max_length=512,
                                     )


class Input(BaseModel):
    question: str
    documents: list[str]


@app.post(config["endpoint"])
async def rank(data: Input):
    ranks = encoder.rank(data.question, data.documents)
    for irank in ranks:
        irank['score'] = str(irank['score'])

    return ranks
