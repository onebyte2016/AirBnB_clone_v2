from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer

class User(BaseModel, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
