from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from .database import Base


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Prediction(Base):
    __tablename__ = 'prediction'
    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey('city.id'))
    weather_id = Column(Integer, ForeignKey('weather.id'))
    date = Column(Date)
    time = Column(Time)


class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Integer)
    cloud = Column(String)