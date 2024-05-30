from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date


def get_city(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.id == city_id).first()


def get_cities(db: Session):
    return db.query(models.City).all()


def create_city(db: Session, city: schemas.CityCreate):
    db_city = models.City(name=city.name)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def create_prediction(db: Session, prediction: schemas.PredictionCreate):
    db_prediction = models.Prediction(**prediction.dict())
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction


def create_weather(db: Session, weather: schemas.WeatherCreate):
    db_weather = models.Weather(**weather.dict())
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather


def get_weather_by_city_and_date(db: Session, city_id: int, date: date):
    return (db.query(models.Prediction.id, models.Prediction.city_id, models.Prediction.weather_id, models.Prediction.date, models.Prediction.time, models.Weather.temperature, models.Weather.cloud).join(models.Weather, models.Prediction.weather_id == models.Weather.id).filter(models.Prediction.city_id == city_id, models.Prediction.date == date).all())


def update_weather(db: Session, weather_id: int, weather: schemas.WeatherCreate):
    db_weather = db.query(models.Weather).filter(models.Weather.id == weather_id).first()
    if db_weather:
        for key, value in weather.dict().items():
            setattr(db_weather, key, value)
        db.commit()
        db.refresh(db_weather)
    return db_weather


def delete_prediction(db: Session, prediction_id: int):
    db_prediction = db.query(models.Prediction).filter(models.Prediction.id == prediction_id).first()
    if db_prediction:
        db.delete(db_prediction)
        db.commit()
    return db_prediction
