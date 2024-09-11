from database import db 
from models.employee import Employee
from models.product import Product  # Import the Product model
from models.employee import employee
from sqlalchemy import select
from datetime import date

def save(employee_data):
    
    employee_output = Employee(date=date.today(), employee_id = employee_data["employee_id"])

    for item_id in employee_data['products_ids']:
        query = select(Product).filter(Product.id == item_id)
        item = db.session.execute(query).scalar()
        print(item)
        employee_output.products.append(item)

    db.session.add(employee_output)
    db.session.commit()

    db.session.refresh(employee_output)
    return employee_output

def find_all():
    query = select(Employee)
    all_output = db.session.execute(query).scalars().all()

    for employee_output in all_output:
        for product in employee_output.productions:
            print(f"Product ID: {product.id}, Product Name: {product.name}")
  
    return all_output


def find_by_employee_id(id):
    query = select(Employee).where(Employee.id == id)
    employee = db.session.execute(query).scalars().all()
    return employee

def 



