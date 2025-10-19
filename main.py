from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.db.models import Base
from infrastructure.db.repositories.product import SqlAlchemyProductRepository
from infrastructure.db import DATABASE_URL
from use_cases.create_product import CreateProductService

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def main():
    session = SessionFactory()
    product_repo = SqlAlchemyProductRepository(session)

    create_product_service = CreateProductService(product_repo=product_repo)
    new_product = create_product_service(name="test1", quantity=1, price=100)
    print(f"create product: {new_product}")


if __name__ == "__main__":
    main()
