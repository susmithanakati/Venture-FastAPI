from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=True, default="")
    last_name = Column(String, nullable=True, default="")
    email = Column(String, nullable=True, default="")
    username = Column(String, nullable=True, default="")
    lastlogin = Column(DateTime, default="")
    is_superuser = Column(String, default="")
    e_staff = Column(String, default="")
    e_active = Column(String, default="")
    date_of_join = Column(DateTime, default="")

    ventures = relationship("Venture", back_populates="owner" ,foreign_keys="[Venture.created_by]")


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, index=True)
    state = Column(String, nullable=True, default="")
    status = Column(Integer, default=0, comment="0=active;1=cancelled;2=delete")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class District(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, index=True)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    district_code = Column(Integer, nullable=True, default=0)
    district = Column(String, nullable=True, default="")
    status = Column(Integer, default=0, comment="0=active;1=cancelled;2=delete")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    state = relationship("State")


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=True, default="")
    state_id = Column(Integer, ForeignKey("states.id"), nullable=True)
    district_id = Column(Integer, ForeignKey("districts.id"), nullable=True)
    status = Column(Integer, default=0, comment="0=active;1=cancelled;2=delete")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    state = relationship("State")
    district = relationship("District")


class Venture(Base):
    __tablename__ = "ventures"

    id = Column(Integer, primary_key=True, index=True)
    venture_name = Column(String, nullable=True, default="")
    email = Column(String, nullable=True, default="")
    phone = Column(String, nullable=True, default="")
    venture_type = Column(String, nullable=True, default="", comment="All, Residential, Commercial, Gated Community")
    venture_status = Column(Integer, nullable=True, comment="Ready To Move, Under Construction")
    venture_facing = Column(String, nullable=True, default="")
    venture_length = Column(Integer, nullable=True, default=0)
    venture_breadth = Column(Integer, nullable=True, default=0)
    plot_area = Column(String, nullable=True, default="")
    no_of_plots = Column(Integer, nullable=True, default=0)
    no_of_gates = Column(Integer, nullable=True, default=0)
    distance_info = Column(String, nullable=True, default="")
    venture_address = Column(String, nullable=True, default="")
    venture_state_id = Column(Integer, ForeignKey("states.id"), nullable=True)
    venture_district_id = Column(Integer, ForeignKey("districts.id"), nullable=True)
    venture_city_id = Column(Integer, ForeignKey("cities.id"), nullable=True)
    is_rera_approved = Column(Boolean, default=False)
    is_rera_registered = Column(Boolean, default=False)
    is_featured = Column(Boolean, default=False)
    status = Column(Integer, default=0, comment="0=active;1=inactive;2=delete")
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = Column( Integer,ForeignKey("users.id"))
    updated_by = Column(Integer,ForeignKey("users.id"), default="")

    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    updated_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    created_by_user = relationship("User", foreign_keys=[created_by])
    updated_by_user = relationship("User", foreign_keys=[updated_by])

    created_by_user = relationship("User", back_populates="ventures", foreign_keys=[created_by])
