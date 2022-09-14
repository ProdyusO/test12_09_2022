# pylint: disable=C0114, W3101
import requests

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from database import database, metadata, engine
import crud



app = FastAPI()

templates = Jinja2Templates(directory="templates")

metadata.create_all(bind=engine)

URL = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273"

html = requests.get(URL).text


@app.on_event("startup")
async def startup():
    """Start session."""
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """End session."""
    await database.disconnect()


@app.get("/{num}/", response_class=RedirectResponse)
async def read_item(num: int):
    """Get endpoint to write paginated data into database."""
    await crud.save_to_db(num, URL)
    return "/result"


@app.get("/result", response_class=HTMLResponse)
async def render_result(request: Request):
    """Get endpoint to show result."""
    context = await crud.read_from_db()
    return templates.TemplateResponse(
        "result.html", {"request": request, "context": context}
    )
