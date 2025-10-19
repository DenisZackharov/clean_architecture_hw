from domain.entities.product import Product, CreateProduct
from interface_adapters.repositories.product_repository import ProductRepository


class CreateProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def __call__(self, name: str, quantity: int, price: float) -> Product:
        product = CreateProduct(name=name, quantity=quantity, price=price)
        self.product_repo.add(product)
        return product
