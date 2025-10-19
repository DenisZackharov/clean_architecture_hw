from domain.entities.order import Order, Product
from interface_adapters.repositories.order_repository import OrderRepository


class CreateOrderService:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    def __call__(self, products: list[Product]) -> Order:
        order = Order(id=None, products=products)
        self.order_repo.add(order)
        return order
