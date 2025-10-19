from pydantic import BaseModel
from domain.entities.product import Product


class Order(BaseModel):
    id: int
    products: list[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)
