from base_repository import BaseRepository
from models import Car, User
from sqlalchemy import select

class AdressRepository(BaseRepository):

    model = Car

    REQUIRED_FIELDS = {
        "brand",
        "model",
        "year"
    }

    ALLOWED_FIELDS = {
        "brand",
        "model",
        "year",
        "user_id"
    }

    def get_all_cars(self) -> list[Car]:

        statement = select(Car)

        result = self.session.execute(statement)

        return result.scalars().all()

    def create_car(self, data):

        self._validate_dict(data)

        self._validate_required_fields(data, self.REQUIRED_FIELDS)

        self._validate_allowed_fields(data, self.ALLOWED_FIELDS)

        new_entity = self.model(**data)

        self.session.add(new_entity)

        self._commit()

        self._refresh(new_entity)

        return new_entity
    
    def update_car(self, car_id, data):

        self._validate_dict(data)

        self._validate_allowed_fields(data, self.ALLOWED_FIELDS)

        car = self._get_by_id(car_id)

        for key, value in data.items():
            setattr(car, key, value)

        self._commit()

        self._refresh(car)

        return car
    
    def delete_car(self, car_id):

        car = self._get_by_id(car_id)

        self.session.delete(car)

        self._commit()

    def assign_user(self, car_id: int, user_id: int) -> Car:

        try:

            car = self.session.get(Car, car_id)

            if car is None:
                raise ValueError(
                    f"Car with ID {car_id} not found."
                )

            user = self.session.get(User, user_id)

            if user is None:
                raise ValueError(
                    f"User with ID {user_id} not found."
                )

            car.user = user

            self.session.commit()
            self.session.refresh(car)

            return car

        except Exception:
            self.session.rollback()
            raise

    def get_cars_with_no_users_associated(self) -> list[Car]:
            try:

                statement = select(Car).where(
                    Car.user_id.is_(None)
                )

                result = self.session.execute(statement)

                return result.scalars().all()

            except Exception:
                self.session.rollback()
                raise

    def get_cars_with_users_associated(self) -> list[Car]:
            try:

                statement = select(Car).where(
                    Car.user_id.is_not(None)
                )

                result = self.session.execute(statement)

                return result.scalars().all()

            except Exception:
                self.session.rollback()
                raise