from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "../templates"))

@router.get("/vision/network", response_class=HTMLResponse)
async def get_network(request: Request):
    return templates.TemplateResponse("network.html", {"request": request})
