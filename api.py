from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import find

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/search", response_class=HTMLResponse)
async def search(request: Request):
    form_data = await request.form()
    user_query = form_data['option']
    response = find.select_query(user_query)
    return templates.TemplateResponse("index.html", {"request": request, "user_query": user_query, "response": response})
if __name__ == '__main__':
    app.run(debug=True)