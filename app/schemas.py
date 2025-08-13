from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

# -------------------- BASE SCHEMA --------------------
class WeatherBase(BaseModel):
    latitude: float = Field(..., ge=-90, le=90, description="Latitude between -90 and 90 degrees")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude between -180 and 180 degrees")
    start_date: date
    end_date: date
    temperature: Optional[float] = None
    description: Optional[str] = None

# -------------------- CREATE --------------------
class WeatherCreate(WeatherBase):
    pass

# -------------------- UPDATE --------------------
class WeatherUpdate(BaseModel):
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    temperature: Optional[float] = None
    description: Optional[str] = None

# -------------------- READ --------------------
class Weather(WeatherBase):
    id: int

    class Config:
        orm_mode = True
