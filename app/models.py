from sqlalchemy import Column, Integer, String, DateTime, Float
from .database import Base
from datetime import datetime

class WeatherRecord(Base):
    __tablename__ = "weather_records"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    start_date = Column(String)  # Keep as string for simplicity
    end_date = Column(String)
    temperature = Column(Float)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

