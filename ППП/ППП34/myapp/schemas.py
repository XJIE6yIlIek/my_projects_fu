from pydantic import BaseModel
import datetime


class CityBase(BaseModel):
    name: str


class CityCreate(CityBase):
    pass


class City(CityBase):
    id: int

    class Config:
        orm_mode = True


class PredictionBase(BaseModel):
    city_id: int
    weather_id: int
    date: datetime.date
    time: datetime.time


class PredictionCreate(PredictionBase):
    pass


class Prediction(PredictionBase):
    id: int

    class Config:
        orm_mode = True


class WeatherBase(BaseModel):
    temperature: int
    cloud: str


class WeatherCreate(WeatherBase):
    pass


class WeatherFetch(WeatherBase):
    date: datetime.datetime
    pass


class Weather(WeatherBase):
    id: int

    class Config:
        orm_mode = True
