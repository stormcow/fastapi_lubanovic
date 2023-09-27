from fastapi import FastAPI, Depends, APIRouter


def user_dep(name: str, password: str):
    return {"name": name, "valid": True}


def check_dep(name: str, password: str):
    if not name:
        raise


def depfunc1():
    pass


def depfunc2():
    pass


app = FastAPI(dependencies=[Depends(depfunc1), Depends(depfunc2)])


@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user


@app.get("/check_user", dependencies=Depends(check_dep))
def check_user() -> bool:
    return True
