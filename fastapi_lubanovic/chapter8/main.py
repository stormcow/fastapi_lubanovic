from fastapi import FastAPI
import uvicorn

from web import explorer, creature

app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)


@app.get("/")
def top() -> str:
    return "top here"

@app.get('/echo/{thing}')
def echo(thing:str) -> str:
    return f"echoing {thing}"

