from fastapi import APIRouter, HTTPException
from model.explorer import Explorer
import service.explorer as service
from errors import Duplicate, Missing

router = APIRouter(prefix="/explorer", tags=["explorer"])


@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()


@router.get("/{name}")
def get_one(name: str) -> Explorer:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=400, detail=exc.msg)


@router.post("/", status_code=201)
@router.post("", status_code=201)
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.patch("/")
@router.patch("")
def modify(explorer: Explorer) -> Explorer:
    try:
        return service.modify(explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.put("/")
def replace(name:str,explorer: Explorer) -> Explorer:
    return service.replace(name,explorer)


@router.delete("/{name}", status_code=204)
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
