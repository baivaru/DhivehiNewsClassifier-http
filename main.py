from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.middleware.cors import CORSMiddleware

from model import DhivehiNewsClassifier

classifier = DhivehiNewsClassifier()

app = FastAPI(
    title="Dhivehi News Classifier",
    description="Dhivehi News Classifier",
    version="0.0.1",
)

app.mount("/assets", StaticFiles(directory="templates/assets"), name="assets")

templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/classify/{news}")
async def multi_word(request: Request, news: str):
    category = classifier.predict(news)
    return category
