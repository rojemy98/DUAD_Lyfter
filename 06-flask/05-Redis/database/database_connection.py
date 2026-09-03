from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseConnection:
    def __init__(self, user, password, host, database, port=5432):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.port = port


    def connection_string(self):
        return (
            f"postgresql://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.database}"
        )

    def create_engine(self, echo=False):
        return create_engine(
            self.connection_string(),
            echo=echo
        )

    def create_session(self):
        engine = self.create_engine()

        SessionLocal = sessionmaker(bind=engine)

        return SessionLocal()