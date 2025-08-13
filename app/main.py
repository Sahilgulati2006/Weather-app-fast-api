from fastapi import FastAPI, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud
from .database import engine, Base, get_db
from .weather_api import get_weather_for_location
from datetime import date

# Create DB tables
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(title="Weather App Backend")

# -------------------- CREATE --------------------
@app.post("/weather/", response_model=schemas.Weather)
def create_weather_record(weather: schemas.WeatherCreate, db: Session = Depends(get_db)):
    # Date validation
    today = date.today()
    if weather.start_date < today:
        raise HTTPException(status_code=400, detail="Start date cannot be in the past")
    if weather.end_date < weather.start_date:
        raise HTTPException(status_code=400, detail="End date must be after start date")

    # Fetch live weather data for the given location
    temp, desc = get_weather_for_location(weather.location)
    weather_with_data = schemas.WeatherCreate(
        location=weather.location,
        start_date=weather.start_date,
        end_date=weather.end_date,
        temperature=temp,
        description=desc
    )
    return crud.create_weather(db, weather_with_data)

# -------------------- READ (ALL) --------------------
@app.get("/weather/", response_model=List[schemas.Weather])
def read_weather_records(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_weather_records(db, skip, limit)

# -------------------- READ (SINGLE) --------------------
@app.get("/weather/{weather_id}", response_model=schemas.Weather)
def read_weather(weather_id: int, db: Session = Depends(get_db)):
    record = crud.get_weather_record(db, weather_id)
    if not record:
        raise HTTPException(status_code=404, detail="Weather record not found")
    return record

# -------------------- UPDATE --------------------
@app.put("/weather/{weather_id}", response_model=schemas.Weather)
def update_weather_record(weather_id: int, updates: schemas.WeatherUpdate, db: Session = Depends(get_db)):
    updated = crud.update_weather(db, weather_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Weather record not found")
    return updated

# -------------------- DELETE --------------------
@app.delete("/weather/{weather_id}")
def delete_weather_record(
    weather_id: int = Path(..., description="The ID of the weather record to delete"),
    db: Session = Depends(get_db)
):
    deleted = crud.delete_weather(db, weather_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Weather record not found")
    return {"message": f"Weather record with ID {weather_id} deleted successfully"}
