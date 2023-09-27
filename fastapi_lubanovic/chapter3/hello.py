from fastapi import FastAPI, Header
import uvicorn

app = FastAPI()

@app.get('/hi')
def greet():
    return 'hi'

@app.get('/hi/{who}')
def greet_specific(who):
    return f"hi {who}"

@app.post('/hi/header')
def greet_header(who:str=Header()):
    return who

@app.get('/happy', status_code=203)
def happy():
    return ':3'
if __name__=='__main__':
    uvicorn.run(app='hello:app', reload=True)