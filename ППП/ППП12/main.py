from fake_useragent import UserAgent
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session
from pydantic import BaseModel
import parser
import logging
import os
from dotenv import load_dotenv


load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()

logging.basicConfig(
    level=logging.INFO,
    format=os.getenv("LOGGER_FORMAT"),
    datefmt=os.getenv("LOGGER_DATEFMT"),
    filename=os.getenv("LOGGER_FILENAME"),
    filemode="a"
)
logger = logging.getLogger(os.getenv("LOGGER_NAME"))


class Cities(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Predictions(Base):
    __tablename__ = 'predictions'
    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    weather_id = Column(Integer, ForeignKey('weathers.id'))
    date = Column(String)


class Weathers(Base):
    __tablename__ = 'weathers'
    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Integer)
    cloud = Column(String)


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
    date: str


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
    date: str
    pass


class Weather(WeatherBase):
    id: int

    class Config:
        orm_mode = True


def create_city(db: Session, city: CityCreate):
    try:
        logger.info("Запрос create_city отправлен")
        db_city = Cities(name=city.name)
        db.add(db_city)
        db.commit()
        db.refresh(db_city)
        return db_city
    except Exception as e:
        logger.error(f"Запрос create_city не выполнен. Ошибка: {e}")


def create_prediction(db: Session, prediction: PredictionCreate):
    try:
        logger.info("Запрос create_prediction отправлен")
        db_prediction = Predictions(**prediction.dict())
        db.add(db_prediction)
        db.commit()
        db.refresh(db_prediction)
        return db_prediction
    except Exception as e:
        logger.error(f"Запрос create_prediction не выполнен. Ошибка: {e}")


def create_weather(db: Session, weather: WeatherCreate):
    try:
        logger.info("Запрос create_weather отправлен")
        db_weather = Weathers(**weather.dict())
        db.add(db_weather)
        db.commit()
        db.refresh(db_weather)
        return db_weather
    except Exception as e:
        logger.error(f"Запрос create_weather не выполнен. Ошибка: {e}")


def get_weather_by_city(db: Session, city_id: int):
    try:
        logger.info("Запрос get_weather_by_city отправлен")
        return (db.query(Predictions, Weathers).join(Weathers, Predictions.weather_id == Weathers.id).filter
            (Predictions.city_id == city_id).all())
    except Exception as e:
        logger.error(f"Запрос get_weather_by_city не выполнен. Ошибка: {e}")


def get_cities_id(db: Session):
    try:
        logger.info("Запрос get_cities_id отправлен")
        return db.query(Cities).all()
    except Exception as e:
        logger.error(f"Запрос get_cities_id не выполнен. Ошибка: {e}")


try:
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session_loc = SessionLocal()
    logger.info("База данных успешно подключена/создана")
except Exception as e:
    logger.error(f"База данных не подключена/не создана. Ошибка: {e}")

base_url_ya = "https://yandex.ru"
url_ya = "https://yandex.ru/pogoda/region/225?via=moc"
user_agent = UserAgent()
headers = {"User-Agent": user_agent.random}

try:
    dct_data_ya = parser.get_data_ya(base_url_ya, url_ya, headers=headers)
    logger.info("Парсер успешно завершил свою работу")
except Exception as e:
    logger.error(f"Парсер завершил свою работу с ошибкой: {e}")

for city in dct_data_ya.keys():
    if dct_data_ya[city]:
        try:
            c = create_city(session_loc, CityCreate(name=city))
            logger.info(f"Строка данных с id {c.id} успешно создана")
        except Exception as e:
            logger.error(f"Строка данных с содержанием {city} не создана. Ошибка: {e}")
        for fc in dct_data_ya[city]:
            try:
                w = create_weather(session_loc, WeatherCreate(temperature=fc[1], cloud=fc[2]))
                logger.info(f"Строка данных с id {w.id} успешно создана")
            except Exception as e:
                logger.error(f"Строка данных с содержанием {fc[1:]} не создана. Ошибка: {e}")
            try:
                p = create_prediction(session_loc, PredictionCreate(city_id=c.id, weather_id=w.id, date=fc[0]))
                logger.info(f"Строка данных с id {p.id} успешно создана")
            except Exception as e:
                logger.error(f"Строка данных с содержанием {c.id} {w.id} {fc[0]} не создана. Ошибка: {e}")

#  ВСЕ ГОРОДА, ТЕМПЕРАТУРА В КОТОРЫХ МОНОТОННО ИЗМЕНЯЕТСЯ
dct_c = {}
for data in get_cities_id(session_loc):
    dct_c[data.id] = data.name

day = 0
dct_t = {}

for city_id in dct_c.keys():
    lst_t = []
    for t in get_weather_by_city(session_loc, city_id):
        lst_t.append(t.Weathers.temperature)
    dct_t[dct_c[city_id]] = lst_t

result = []
for city_name in dct_t.keys():
    if dct_t[city_name] == sorted(dct_t[city_name]) or dct_t[city_name] == list(reversed(sorted(dct_t[city_name]))):
        result.append(city_name)

for city_name in result:
    print(city_name)
#  ВСЕ ГОРОДА, ТЕМПЕРАТУРА В КОТОРЫХ МОНОТОННО ИЗМЕНЯЕТСЯ

#  ГРАФИКИ
c_id = get_cities_id(session_loc)
cities_dct = {}
cities_dct[c_id[4].id] = c_id[4].name
cities_dct[c_id[434].id] = c_id[434].name
cities_dct[c_id[967].id] = c_id[967].name

name_t = {}
for city_id in cities_dct.keys():
    lst_t = []
    for t in get_weather_by_city(session_loc, city_id):
        lst_t.append(t.Weathers.temperature)
    name_t[cities_dct[city_id]] = lst_t

for city_name in name_t.keys():
    plt.plot(name_t[city_name], label=city_name)
plt.legend()
plt.xlabel("day")
plt.ylabel("temperature")
plt.show()
#  ГРАФИКИ
