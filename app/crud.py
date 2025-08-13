from sqlalchemy.orm import Session
from . import models, schemas

def create_weather(db: Session, weather: schemas.WeatherCreate):
    """Create a new weather record."""
    db_weather = models.WeatherRecord(**weather.dict())
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather

def get_weather_records(db: Session, skip: int = 0, limit: int = 10):
    """Fetch multiple weather records with pagination."""
    return db.query(models.WeatherRecord).offset(skip).limit(limit).all()

def get_weather_record(db: Session, weather_id: int):
    """Fetch a single weather record by ID."""
    return db.query(models.WeatherRecord).filter(models.WeatherRecord.id == weather_id).first()

def update_weather(db: Session, weather_id: int, updates: schemas.WeatherUpdate):
    """Update an existing weather record."""
    record = db.query(models.WeatherRecord).filter(models.WeatherRecord.id == weather_id).first()
    if not record:
        return None
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(record, key, value)
    db.commit()
    db.refresh(record)
    return record

def delete_weather(db: Session, weather_id: int):
    """Delete a weather record."""
    record = db.query(models.WeatherRecord).filter(models.WeatherRecord.id == weather_id).first()
    if not record:
        return None
    db.delete(record)
    db.commit()
    return record
