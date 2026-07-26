from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os

app = FastAPI(title="Antigravity Portfolio")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(BASE_DIR, "static")
templates_dir = os.path.join(BASE_DIR, "templates")

os.makedirs(static_dir, exist_ok=True)
os.makedirs(templates_dir, exist_ok=True)

# Mount the static directory to serve JS, images, and videos
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Set up the templates directory for Jinja2
templates = Jinja2Templates(directory=templates_dir)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the main index.html template on the root route.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/contact")
async def handle_contact(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    """
    Handles the POST request from the contact form.
    """
    return {
        "status": "success", 
        "message": f"Contact form submitted successfully by {name}."
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
