from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os

app = FastAPI(title="Antigravity Portfolio")

# Ensure static and templates dirs exist
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Mount the static directory to serve JS, images, and videos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up the templates directory for Jinja2
templates = Jinja2Templates(directory="templates")

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
