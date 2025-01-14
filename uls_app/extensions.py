from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from sqlalchemy.orm import DeclarativeBase

api = Api(prefix="/api/v1")

class Base(DeclarativeBase):
    __abstract__ = True

db = SQLAlchemy(model_class=Base)