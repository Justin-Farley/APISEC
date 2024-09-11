from sqlalchemy.orm import Mapped, mapped_column
from database import db, Base
from datetime import date

class Production(Base):
    __tablename__ = 'productions'
    product_id: Mapped[int] = mapped_column(primary_key=True)
    employee_id: Mapped[int] = mapped_column(db.ForeignKey('Products.id'), nullable=False)
    quantity_produced: Mapped[int] = mapped_column(db.Integer, nullable=False)
    date_produced: Mapped[date] = mapped_column(db.Date, nullable=False)
    product: Mapped["Product"] = db.relationship("Product", back_populates="productions")
    employees: Mapped["Employee"] = db.relationship("Employee", back_populates="productions")