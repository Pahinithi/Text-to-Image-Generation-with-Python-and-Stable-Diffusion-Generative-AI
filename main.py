from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from generate import generate_image  # Import the generate function from the generate.py file

# Initialize FastAPI app
app = FastAPI()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Serve the frontend (index.html)
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint for generating images based on prompt
@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, prompt: str = Form(...), negative_prompt: str = Form(...)):
    # Call the generate_image function and pass the prompt and negative prompt
    image_path = generate_image(prompt, negative_prompt)
    
    # Return the page with the generated image
    return templates.TemplateResponse("index.html", {"request": request, "image_path": image_path})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    

 # Example usage
# prompt = "Cricket player MS Dhoni shaking hands with cricket player Virat Kohli on a cricket field."
# negative_prompt = "Avoid including any other people or unnecessary background details."
# generate_image(prompt, negative_prompt)
