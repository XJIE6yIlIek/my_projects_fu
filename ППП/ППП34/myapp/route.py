from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas, models
from .database import SessionLocal, engine
from datetime import datetime
from datetime import date

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/city/", response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db)):
    return crud.create_city(db=db, city=city)


@router.get("/city/", response_model=List[schemas.City])
def read_cities(db: Session = Depends(get_db)):
    return crud.get_cities(db)


@router.get("/city/{city_id}")
def read_last_weather(city_id: int, db: Session = Depends(get_db)):
    city = crud.get_city(db, city_id=city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return crud.get_weather_by_city_and_date(db, city_id=city_id, date=datetime.today().date())


@router.get("/city/{city_id}/predictions/")
def read_weather_predictions(city_id: int, date: Optional[date] = None, db: Session = Depends(get_db)):
    if date:
        rs = crud.get_weather_by_city_and_date(db, city_id=city_id, date=date)
        return [{"weather_id": res[2], "prediction_id": res[0], "prediction_on_date": res[3], "prediction_on_time": res[4], "date": res[3], "temperature": res[5], "cloud": res[6] } for res in rs]
    return crud.get_weather_by_city_and_date(db, city_id=city_id, date=datetime.today().date())


@router.post("/predictions/{city_id}")
def create_prediction(city_id: int, weather: schemas.WeatherFetch, db: Session = Depends(get_db)):
    weather_c = schemas.WeatherCreate(
        temperature=weather.temperature,
        cloud=weather.cloud
    )
    weather_d = crud.create_weather(db=db, weather=weather_c)
    prediction = schemas.PredictionCreate(
        weather_id=weather_d.id,
        city_id=city_id,
        date=weather.date,
        time="12:00"
    )
    result = crud.create_prediction(db=db, prediction=prediction)
    return {'prediction_id': result.id, 'date': result.date, 'time': result.time}


@router.put("/predictions/{prediction_id}/{weather_id}", response_model=schemas.Weather)
def update_weather(prediction_id: int, weather_id: int, weather: schemas.WeatherCreate, db: Session = Depends(get_db)):
    return crud.update_weather(db=db, weather_id=weather_id, weather=weather)


@router.delete("/predictions/{prediction_id}", response_model=schemas.Prediction)
def delete_prediction(prediction_id: int, db: Session = Depends(get_db)):
    return crud.delete_prediction(db=db, prediction_id=prediction_id)
