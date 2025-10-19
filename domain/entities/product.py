from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int


class CreateProduct(BaseModel):
    name: str | None = None
    price: float | None = None
    quantity: int | None = None
