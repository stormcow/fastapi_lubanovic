from .data.data import get_creatures
from .models.creature import Creature
from fastapi import FastAPI

app = FastAPI()


@app.get("/creature")
def get_all() -> list[Creature]:

    return get_creatures()
