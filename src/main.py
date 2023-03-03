from fastapi import Depends, FastAPI
import uvicorn
import services
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
page_name = "bbcnews"

app = FastAPI()

@app.post("/create/")
async def create_posts(db:Session=Depends(get_db)):
    services.get_fb_page_data(db, page_name)
    return {"message" : "posts created" }

@app.get("/data/")
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts

