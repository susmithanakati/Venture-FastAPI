from fastapi import FastAPI,Depends,HTTPException
from database import Base,engine,SessionLocal
import crud
from schemas import StateSchema,DistrictSchema,CitySchema,VentureSchema,VentureResponse
from models import Venture
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Welcome To The NOKABZAA  Ventures"}

@app.post("/ventures/",response_model = VentureResponse)
def create_venture(venture:VentureSchema,db:Session = Depends(get_db)):
    return crud.create_venture(db,venture)

@app.get("/ventures/",response_model = list[VentureResponse])
def get_venture(db:Session = Depends(get_db)):
    return crud.get_venture(db)

@app.get("/ventures/{venture_id}",response_model = VentureResponse)
def get_venture_(venture_id:int,db:Session = Depends(get_db)):
    venture = crud.get_venture(db,venture_id)
    if not venture:
        raise HTTPException(status_code=404,detail="Venture Not Found")
    return venture

@app.put("/ventures/{venture_id}",response_model = VentureResponse)
def update_venture(venture_id=int,db:Session = Depends(get_db)):
    venture = crud.update_venture(db,venture_id)
    if not venture:
        raise HTTPException(status_code=404,detail="Venture Not Found")
    return venture


@app.delete("/ventures/{venture_id}",response_model=VentureResponse)
def delete_venture(venture_id=int,db:Session = Depends(get_db)):
    venture = crud.delete_venture(db,venture_id)
    if not venture:
        raise HTTPException(status_code=404,detail="Venture Not Found")
    return venture


