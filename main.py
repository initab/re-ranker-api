from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import cross_encoder

app = FastAPI(root_path="/api")

encoder = cross_encoder.CrossEncoder(model_name="KBLab/megatron-bert-base-swedish-cased-600k",
                                     num_labels=1,
                                     max_length=512,
                                     )


class Input(BaseModel):
    question: str
    documents: list[str]


@app.post("/rank")
async def rank(data: Input):
    ranks = encoder.rank(data.question, data.documents)
    for irank in ranks:
        irank['score'] = str(irank['score'])

    return ranks
