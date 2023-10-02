from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request


app = FastAPI()
top = Path(__file__).resolve().parent

template_obj = Jinja2Templates(directory=f"{top}/template")


@app.get("/list")
def explorer_list(request: Request):
    return template_obj.TemplateResponse(
        "list.html", {"request": request, "explorers": None, "creatures": None}
    )
