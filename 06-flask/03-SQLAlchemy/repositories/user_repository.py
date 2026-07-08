from base_repository import BaseRepository
from models import User
from sqlalchemy import select

class UserRepository(BaseRepository):

    model = User

    REQUIRED_FIELDS = {
        "name",
        "email"
    }

    ALLOWED_FIELDS = {
        "name",
        "email"
    }

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)


    def get_all_users(self) -> list[User]:

        statement = select(User)

        result = self.session.execute(statement)

        return result.scalars().all()

    def create_user(self, data):

        self._validate_dict(data)

        self._validate_required_fields(data, self.REQUIRED_FIELDS)

        self._validate_allowed_fields(data, self.ALLOWED_FIELDS)

        new_entity = self.model(**data)

        self.session.add(new_entity)

        self._commit()

        self._refresh(new_entity)

        return new_entity
    
    def update_user(self, user_id, data):

        self._validate_dict(data)

        self._validate_allowed_fields(data, self.ALLOWED_FIELDS)

        user = self._get_by_id(user_id)

        for key, value in data.items():
            setattr(user, key, value)

        self._commit()

        self._refresh(user)

        return user
    
    def delete_user(self, user_id):

        user = self._get_by_id(user_id)

        self.session.delete(user)

        self._commit()