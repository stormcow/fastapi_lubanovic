from fastapi import FastAPI, Response
from pathlib import Path
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

top = str(Path(__file__).parent) + '/static'

print(top)
app.mount('/static',
          StaticFiles(directory=top, html=True),
          name='abc')
# print(f"{top}/static")

@app.get('/static')
async def static():
    with open(os.path.join(top,'abc.txt')) as fh:
        data = fh.read()
    return Response(content=data, media_type='text/html')