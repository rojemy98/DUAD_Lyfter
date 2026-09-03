from sqlalchemy import select
from repositories.base_repository import BaseRepository
from database.models import Product


class ProductsRepository(BaseRepository):

    model = Product

    REQUIRED_FIELDS = {
        "name",
        "price",
        "entry_date",
        "quantity"
    }

    ALLOWED_FIELDS = REQUIRED_FIELDS

    def insert_product(self, data: dict):

        self._validate_dict(data)
        self._validate_required_fields(data, self.REQUIRED_FIELDS)
        self._validate_allowed_fields(data, self.ALLOWED_FIELDS)

        product = Product(**data)

        self.session.add(product)
        self._commit()
        self._refresh(product)

        return product

    def get_products(self):

        statement = (
            select(Product)
            .order_by(Product.id)
        )

        return self.session.scalars(statement).all()

    def get_product_by_id(self, product_id: int):

        return self._get_by_id(product_id)

    def update_product(self, product_id: int, data: dict):

        self._validate_dict(data)

        self._validate_allowed_fields(
            data,
            self.ALLOWED_FIELDS
        )

        product = self._get_by_id(product_id)

        for field, value in data.items():
            setattr(product, field, value)

        self._commit()

        self._refresh(product)

        return product

    def delete_product(self, product_id: int):

        product = self._get_by_id(product_id)

        self.session.delete(product)

        self._commit()

        return {
            "message": f"Product '{product.name}' deleted successfully."
        }