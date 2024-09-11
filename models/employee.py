from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from models.role import Role

class Employee(Base):
    __tablename__ = 'Employees'
    employee_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(db.String(20), nullable=False)
    username: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    
    role: Mapped["Role"] = db.relationship("Role")
    productions: Mapped[List["production"]] = db.relationship(back_populates="employee")