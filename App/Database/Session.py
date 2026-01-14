from sqlalchemy.engine import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
import os


class DatabaseManager:
    def __init__(self) -> None:
        self.conn_path = (
            str(os.getenv("DB_DIALECT"))
            + "+"
            + str(os.getenv("DB_SQL_DRIVER"))
            + "://"
            + str(os.getenv("DB_USER"))
            + ":"
            + str(os.getenv("DB_PASSWORD"))
            + "@"
            + str(os.getenv("DB_IP"))
            + ":"
            + str(os.getenv("DB_PORT"))
            + "/?service_name="
            + str(os.getenv("DB_SERVICE"))
        )
        self.engine = None
        self.session = None

    def start_engine(self):
        try:
            self.engine = create_engine(self.conn_path, poolclass=NullPool)
        except Exception as e:
            raise Exception(f"Erro ao tentar inicializar a engine: {str(e)}") from e

    def __enter__(self):
        if not self.engine:
            self.start_engine()

        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()
        return self.session

    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type:
                self.session.rollback()
                pass
            else:
                self.session.commit()
        finally:
            self.session.close()
