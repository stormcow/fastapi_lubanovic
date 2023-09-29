from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials


app = FastAPI()
basic = HTTPBasic()

secret_user = "newphone"
secret_password = "whodis?"

@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    if (creds.username == secret_user and creds.password == secret_password):
        return {
            "username":creds.username,
            "password":creds.password
        }
    raise HTTPException(status_code=401, detail="Hey!")
