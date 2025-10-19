from domain.entities.product import Product
from pydantic import BaseModel


class Order(BaseModel):
    id: int
    products: list[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)
