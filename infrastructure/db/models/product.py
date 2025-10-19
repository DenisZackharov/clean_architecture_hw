from sqlalchemy import Column, Integer, String, Float
from infrastructure.db.models import Base


class ProductORM(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
