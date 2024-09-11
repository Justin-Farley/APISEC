from database import db #need db be to serve incoming data to db
from models.user import User #need this to create user Objects
from utils.util import encode_token

from sqlalchemy import select

def login(username, password): #Login using unique info so we don't query multiple users
    query = select(User).where(User.username == username)
    user = db.session.execute(query).scalar_one_or_none() #Query user table for a user with the password and username

    if user and user.password == password:#if we have a user associated with the username, validated the password
        auth_token = encode_token(user.id, user.role.role_name)

        response = {
            "status":"success",
            "message":"Successfully Logged In",
            "auth_token": auth_token
        }
        return response
    else:
        response = {
            "status": "fail",
            "message": "Invalid username or password"
        }
        return response


def save(user_data):
    
    new_user = User(name=user_data['name'], email=user_data['email'], password=user_data['password'], phone=user_data['phone'], username=user_data['username'])
    db.session.add(new_user)
    db.session.commit()

    db.session.refresh(new_user)
    return new_user

def find_all():
    query = select(User)
    all_users = db.session.execute(query).scalars().all()
    return all_users

def find_all_paginate(page, per_page):
    users = db.paginate(select(User), page = page, per_page = per_page)
    return users