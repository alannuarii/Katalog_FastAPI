from fastapi import Depends, Request
import model
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from config import app, get_database_session, templates

@app.get("/", response_class=HTMLResponse)
async def index(request:Request, db:Session = Depends(get_database_session)):
    datas = db.query(model.Catalog).all()

    return templates.TemplateResponse("pages/index.html", {"request":request, "datas":datas, "title":"ECatalog"})

@app.get("/detail/{id}", response_class=HTMLResponse)
async def detail(request:Request, id:int, db:Session = Depends(get_database_session)):
    datas = db.query(model.Catalog).all()
    data = db.query(model.Catalog).filter(model.Catalog.id==id).first()

    return templates.TemplateResponse("pages/detail.html", {"request":request, "datas":datas, "data":data, "title":"Product Information"})