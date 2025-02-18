from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    username: Optional[str] = None
    lastlogin: Optional[datetime] = None
    is_superuser: Optional[str] = None
    e_staff: Optional[str] = None
    e_active: Optional[str] = None
    date_of_join: Optional[datetime] = None

    class Config:
        from_attributes = True

class StateSchema(BaseModel):
    id: Optional[int] = None
    state: Optional[str] = ""
    status: int = 0
    created_at: Optional[datetime] = None
    updated_date: Optional[datetime] = None

    class Config:
        from_attributes = True


class DistrictSchema(BaseModel):
    id: Optional[int] = None
    state_id: int
    district_code: Optional[int] = 0
    district: Optional[str] = ""
    status: int = 0
    created_at: Optional[datetime] = None
    updated_date: Optional[datetime] = None

    class Config:
        from_attributes = True


class CitySchema(BaseModel):
    id: Optional[int] = None
    city: Optional[str] = ""
    state_id: Optional[int] = None
    district_id: Optional[int] = None
    status: int = 0
    created_at: Optional[datetime] = None
    updated_date: Optional[datetime] = None

    class Config:
        from_attributes = True


class VentureSchema(BaseModel):
    id: Optional[int] = None
    venture_name: Optional[str] = ""
    email: Optional[EmailStr] = None
    phone: Optional[str] = ""
    venture_type: Optional[str] = ""
    venture_status: Optional[int] = None
    venture_facing: Optional[str] = ""
    venture_length: Optional[int] = 0
    venture_breadth: Optional[int] = 0
    plot_area: Optional[str] = ""
    no_of_plots: Optional[int] = 0
    no_of_gates: Optional[int] = 0
    distance_info: Optional[str] = ""
    venture_address: Optional[str] = ""
    venture_state_id: Optional[int] = None
    venture_district_id: Optional[int] = None
    venture_city_id: Optional[int] = None
    is_rera_approved: Optional[bool] = False
    is_rera_registered: Optional[bool] = False
    is_featured: Optional[bool] = False
    status: int = 0
    created_date: Optional[datetime] = None
    updated_date: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_by: Optional[int] = None


class VentureResponse(BaseModel):
    id: Optional[int]

    class Config:
        from_attributes = True
