from sqlalchemy import select
from repositories.base_repository import BaseRepository
from database.models import User


class UsersRepository(BaseRepository):

    model = User

    REQUIRED_FIELDS = {
        "name",
        "last_name",
        "email",
        "password",
        "role"
    }

    ALLOWED_FIELDS = {
        "name",
        "last_name",
        "email",
        "password",
        "role",
        "registration_date"
    }

    def insert_user(self, data: dict):

        try:

            self._validate_dict(data)

            self._validate_required_fields(
                data,
                self.REQUIRED_FIELDS
            )

            self._validate_allowed_fields(
                data,
                self.ALLOWED_FIELDS
            )

            user = User(**data)

            self.session.add(user)

            self._commit()

            self._refresh(user)

            return user

        except Exception:
            raise

    def get_user(self, email: str, password: str):

        try:

            statement = (
                select(User)
                .where(
                    User.email == email,
                    User.password == password
                )
            )

            return self.session.scalar(statement)

        except Exception:
            raise

    def get_user_by_id(self, user_id: int):

        try:

            return self._get_by_id(user_id)

        except Exception:
            raise

    def get_user_role_by_id(self, user_id: int) -> str:
        try:

            statement = (
                select(User.role)
                .where(User.id == user_id)
            )

            role = self.session.scalar(statement)

            if role is None:
                raise ValueError(
                    f"User with id {user_id} not found."
                )

            return role

        except Exception:
            raise