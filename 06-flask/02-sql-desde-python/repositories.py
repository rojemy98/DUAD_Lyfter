import traceback

from utils import (
    rollback,
    format_results
)

class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "name": user_record[1],
            "last_name": user_record[2],
            "username": user_record[3],
            "email": user_record[4],
            "birthdate": user_record[5].isoformat(),
            "status": user_record[6],
        }
    
    def get_all(self, filters=None):

        try:

            query = """
                SELECT
                    id,
                    name,
                    last_name,
                    username,
                    email,
                    birthdate,
                    status
                FROM lyfter_car_rental.users
            """

            params = []

            if filters:

                conditions = []

                for key, value in filters.items():
                    conditions.append(f"{key} = %s")
                    params.append(value)

                query += " WHERE " + " AND ".join(conditions)

            results = self.db_manager.execute_query(
                query,
                *params
            )

            return format_results(
                results,
                self._format_user
            )

        except Exception:

            return rollback(self.db_manager)

    def create_user(self, user_data):

        name = user_data["name"]
        last_name = user_data["last_name"]
        username = user_data["username"]
        email = user_data["email"]
        password = user_data["password"]
        birthdate = user_data["birthdate"]
        
        try:

            result = self.db_manager.execute_query(
                """
                INSERT INTO lyfter_car_rental.users(name, last_name, username, email, password, birthdate)
                VALUES(%s,%s,%s,%s,%s,%s)
                RETURNING id, name, last_name, username, email, birthdate, status;
                """,
                name, last_name, username, email, password, birthdate
            )

            self.db_manager.commit()

            return self._format_user(result[0])

        except Exception:

            self.db_manager.rollback()

            traceback.print_exc()

            return None
        
    def bulk_create_users(self, users):
        """
        Insert multiple users into the database.

        Args:
            users (list): List of user tuples.

        Returns:
            bool
        """

        try:

            query = """
                INSERT INTO lyfter_car_rental.users
                (
                    name,
                    last_name,
                    username,
                    email,
                    password,
                    birthdate,
                    status
                )
                VALUES %s;
            """

            self.db_manager.begin_transaction()

            self.db_manager.execute_many(
                query,
                users
            )

            self.db_manager.commit()

            return True

        except Exception:

            return rollback(self.db_manager)
        
    def update_user_status(self, user_id, user_status):

        try:

            self.db_manager.begin_transaction()

            user = self.db_manager.execute_query(
                """
                SELECT id
                FROM lyfter_car_rental.users
                WHERE id = %s;
                """,
                user_id
            )

            if not user:
                raise Exception("User not found")

            updated_user = self.db_manager.execute_query(
                """
                UPDATE lyfter_car_rental.users
                SET status = %s
                WHERE id = %s
                RETURNING
                    id,
                    name,
                    last_name,
                    username,
                    email,
                    birthdate,
                    status;
                """,
                user_status,
                user_id
            )

            self.db_manager.commit()

            return self._format_user(updated_user[0])

        except Exception:

            self.db_manager.rollback()

            traceback.print_exc()

            return None
        
    def get_active_user_ids(self):
        """
        Return the IDs of all active users.
        """

        results = self.db_manager.execute_query(
            """
            SELECT id
            FROM lyfter_car_rental.users
            WHERE status = 'Active';
            """
        )

        return [row[0] for row in results]


class CarRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_cars(self, user_record):
        return {
            "id": user_record[0],
            "brand": user_record[1],
            "model": user_record[2],
            "manufacturing_year": user_record[3],
            "status": user_record[4],
        }

    def get_all(self, filters=None):

        try:

            query = """
                SELECT
                    id,
                    brand,
                    model,
                    manufacturing_year,
                    status
                FROM lyfter_car_rental.cars
            """

            params = []

            if filters:

                conditions = []

                for key, value in filters.items():
                    conditions.append(f"{key} = %s")
                    params.append(value)

                query += " WHERE " + " AND ".join(conditions)

            results = self.db_manager.execute_query(
                query,
                *params
            )

            return format_results(
                results,
                self._format_cars
            )

        except Exception:

            return rollback(self.db_manager)
        
    def get_available_car_ids(self):
        """
        Return the IDs of all available cars.
        """

        results = self.db_manager.execute_query(
            """
            SELECT id
            FROM lyfter_car_rental.cars
            WHERE status = 'Available';
            """
        )

        return [row[0] for row in results]
        
    def create_car(self, car_data):

        brand = car_data["brand"]
        model = car_data["model"]
        manufacturing_year = car_data["manufacturing_year"]
        
        try:

            result = self.db_manager.execute_query(
                """
                INSERT INTO lyfter_car_rental.cars(brand, model, manufacturing_year)
                VALUES(%s,%s,%s)
                RETURNING id, brand, model, manufacturing_year, status;
                """,
                brand, model, manufacturing_year
            )

            self.db_manager.commit()

            return self._format_cars(result[0])

        except Exception:

            self.db_manager.rollback()

            traceback.print_exc()

            return None
        
    def bulk_create_cars(self, cars):
        """
        Insert multiple cars into the database.

        Args:
            cars (list): List of car tuples.

        Returns:
            bool
        """

        try:

            query = """
                INSERT INTO lyfter_car_rental.cars
                (
                    brand,
                    model,
                    manufacturing_year,
                    status
                )
                VALUES %s;
            """

            self.db_manager.begin_transaction()

            self.db_manager.execute_many(
                query,
                cars
            )

            self.db_manager.commit()

            return True

        except Exception:

            return rollback(self.db_manager)
        
    def update_car_status(self, car_id, car_status):

        try:

            self.db_manager.begin_transaction()

            car = self.db_manager.execute_query(
                """
                SELECT id
                FROM lyfter_car_rental.cars
                WHERE id = %s;
                """,
                car_id
            )

            if not car:
                raise Exception("Car not found")

            updated_car = self.db_manager.execute_query(
                """
                UPDATE lyfter_car_rental.cars
                SET status = %s
                WHERE id = %s
                RETURNING
                    id,
                    brand,
                    model,
                    manufacturing_year,
                    status;
                """,
                car_status,
                car_id
            )

            self.db_manager.commit()

            return self._format_cars(updated_car[0])

        except Exception:

            self.db_manager.rollback()

            traceback.print_exc()

            return None


class RentalRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_rentals(self, rental_record):
        return {
            "id": rental_record[0],
            "user_id": rental_record[1],
            "car_id": rental_record[2],
            "rental_date": rental_record[3],
            "rental_status": rental_record[4],
        }

    def get_all(self, filters=None):

        try:

            query = """
                SELECT
                    id,
                    user_id,
                    car_id,
                    rental_date,
                    rental_status
                FROM lyfter_car_rental.rentals
            """

            params = []

            if filters:

                conditions = []

                for key, value in filters.items():
                    conditions.append(f"{key} = %s")
                    params.append(value)

                query += " WHERE " + " AND ".join(conditions)

            results = self.db_manager.execute_query(
                query,
                *params
            )

            return format_results(
                results,
                self._format_rentals
            )

        except Exception:

            return rollback(self.db_manager)

    def create_rental(self, rental_data):

        user_id = rental_data["user_id"]
        car_id = rental_data["car_id"]

        try:

            self.db_manager.begin_transaction()

            user = self.db_manager.execute_query(
                """
                SELECT id, status
                FROM lyfter_car_rental.users
                WHERE id = %s;
                """,
                user_id
            )

            if not user:
                raise Exception("User not found")

            if user[0][1] != "Active":
                raise Exception("User is not active")

            car = self.db_manager.execute_query(
                """
                SELECT id, status
                FROM lyfter_car_rental.cars
                WHERE id = %s;
                """,
                car_id
            )

            if not car:
                raise Exception("Car not found")

            if car[0][1] != "Available":
                raise Exception("Car is not available")

            rental = self.db_manager.execute_query(
                """
                INSERT INTO lyfter_car_rental.rentals(user_id, car_id)
                VALUES(%s,%s)
                RETURNING id, user_id, car_id, rental_date, rental_status;
                """,
                user_id, car_id
            )

            self.db_manager.execute_query(
                """
                UPDATE lyfter_car_rental.cars
                SET status = 'Rented'
                WHERE id = %s;
                """,
                car_id
            )

            self.db_manager.commit()

            return self._format_rentals(rental[0])

        except Exception as error:

            self.db_manager.rollback()

            print("Transaction rolled back:", error)

            return None
        
    def update_rental_status(self, rental_id, rental_status):
        try:

            self.db_manager.begin_transaction()

            rental = self.db_manager.execute_query(
                """
                SELECT id
                FROM lyfter_car_rental.rentals
                WHERE id = %s;
                """,
                rental_id
            )

            if not rental:
                raise Exception("Rental not found")

            updated_rental = self.db_manager.execute_query(
                """
                UPDATE lyfter_car_rental.rentals
                SET rental_status = %s
                WHERE id = %s
                RETURNING
                    id,
                    user_id,
                    car_id,
                    rental_date,
                    rental_status;
                """,
                rental_status,
                rental_id
            )

            self.db_manager.commit()

            return self._format_rentals(updated_rental[0])

        except Exception:

            self.db_manager.rollback()

            traceback.print_exc()

            return None
        
    def complete_rental(self, rental_id):

        try:

            self.db_manager.begin_transaction()

            rental = self.db_manager.execute_query(
                """
                SELECT
                    id,
                    car_id,
                    rental_status
                FROM lyfter_car_rental.rentals
                WHERE id = %s;
                """,
                rental_id
            )

            if not rental:
                raise Exception("Rental not found")

            rental_record = rental[0]

            car_id = rental_record[1]
            rental_status = rental_record[2]

            if rental_status == "Completed":
                raise Exception("Rental already completed")

            updated_rental = self.db_manager.execute_query(
                """
                UPDATE lyfter_car_rental.rentals
                SET rental_status = 'Completed'
                WHERE id = %s
                RETURNING
                    id,
                    user_id,
                    car_id,
                    rental_date,
                    rental_status;
                """,
                rental_id
            )

            self.db_manager.execute_query(
                """
                UPDATE lyfter_car_rental.cars
                SET status = 'Available'
                WHERE id = %s;
                """,
                car_id
            )

            self.db_manager.commit()

            return self._format_rentals(updated_rental[0])

        except Exception as error:

            self.db_manager.rollback()

            print(error)

            return None