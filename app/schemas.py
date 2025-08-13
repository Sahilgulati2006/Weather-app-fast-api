from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from datetime import date

class WeatherBase(BaseModel):
    location: str
    start_date: str
    end_date: str
    temperature: Optional[float] = None
    description: Optional[str] = None

class WeatherCreate(WeatherBase):
    pass

class WeatherUpdate(BaseModel):
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    temperature: Optional[float] = None
    description: Optional[str] = None

class Weather(WeatherBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class WeatherUpdate(BaseModel):
    location: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

