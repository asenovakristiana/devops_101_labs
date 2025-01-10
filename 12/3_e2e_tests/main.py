from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Storage for todo items
todo_items = []


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html.j2", {"request": request, "todo_items": todo_items})


@app.post("/add-item", response_class=HTMLResponse)
async def add_item(request: Request, todo: str = Form(...)):
    todo_items.append(todo)
    return templates.TemplateResponse("index.html.j2", {"request": request, "todo_items": todo_items})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)