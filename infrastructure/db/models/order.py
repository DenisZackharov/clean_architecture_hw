from sqlalchemy import Column, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.db.models import Base


class OrderORM(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)


order_product_associations = Table(
    'order_product_associations', Base.metadata,
    Column('order_id', ForeignKey('orders.id')),
    Column('product_id', ForeignKey('products.id'))
)

OrderORM.products = relationship("ProductORM", secondary=order_product_associations)
