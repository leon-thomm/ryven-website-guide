# This file is for development purposes only.

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()

tmplts = Jinja2Templates(directory='templates')

app.mount("/resources/img", StaticFiles(directory="resources/img"), name="img")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    with open('index.html') as f:
        return f.read()


@app.get('/guide_markdown', response_class=PlainTextResponse)
async def guide_readme(request: Request):

    return tmplts.TemplateResponse(
        "guide.md",
        {
            "request": request,
        }
    )



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=3200)