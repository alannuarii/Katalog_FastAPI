from fastapi import FastAPI
from database import SessionLocal, engine
import model
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
