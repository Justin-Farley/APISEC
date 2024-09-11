from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from models.role import Role

class User(Base):
    __tablename__ = 'Customers'
    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)    
    role_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('Roles.id'), nullable=False)
    role: Mapped["str"] = db.relationship("Role")
    