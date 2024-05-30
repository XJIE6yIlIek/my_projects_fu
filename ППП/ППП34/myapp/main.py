from fastapi import FastAPI
from myapp.route import router as route_app

app = FastAPI()

app.mount("/", route_app)
