from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/temperature")
def get_temperature(location: str = None):
    # Возвращаем случайное значение температуры
    temperature = round(random.uniform(-20.0, 40.0), 2)
    return {"location": location, "temperature": temperature}

@app.get("/sensors")
def get_sensors():
    return [
        {"id": 1, "name": "Thermostat 1", "location": "Living Room"},
        {"id": 2, "name": "Outdoor Sensor", "location": "Garden"}
        ]

@app.get("/")
def root():
    return {"message": "Temperature API is running"}
