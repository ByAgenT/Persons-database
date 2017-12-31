from typing import List

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import ArgumentError

Base = declarative_base()


class DatabaseConnectorError(Exception):
    """Base class for DatabaseConnector errors"""
    pass


class DatabasePathError(DatabaseConnectorError):
    """Raised when database not found and engine cannot be created"""
    pass


class DatabaseConnector:

    def __init__(self, db: str) -> None:
        self._session = self._create_connection(db)

    # noinspection PyMethodMayBeStatic
    def _create_connection(self, db: str) -> Session:
        """
        Creates new connection to the database

        :param db: Path to the database
        :return: Database session
        """
        try:
            engine = sqlalchemy.create_engine(db)
            session = sessionmaker(bind=engine)()
            return session
        except (ArgumentError, ):
            raise DatabasePathError("Cannot find database")

    def add(self, obj: Base) -> None:
        """
        Adds an object to the database

        :param obj: object to be added
        :return: None
        """
        self._session.add(obj)
        self._session.commit()

    def remove(self, obj: Base) -> None:
        """
        Removes an object from the database

        :param obj: Object to be removed
        :return: None
        """
        self._session.delete(obj)
        self._session.commit()

    def retrieve(self, entity: Base, q_id: int) -> Base:
        """
        Retrieves object from the database with id

        :param entity: Entity to be retrieved
        :param q_id: Object id to be retrieved
        :return: SQLAlchemy inherited from Base object
        """
        return self._session.query(entity).filter(id=q_id)

    def retrieve_all(self, entity: Base) -> List[Base]:
        """
        Retrieve all entities from the database

        :param entity: Entities to be retrieved
        :return: List of entities
        """
        return self._session.query(entity).all()
