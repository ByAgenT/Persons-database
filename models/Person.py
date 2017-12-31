from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, Integer, String

Base = declarative_base()


class Person(Base):
    """
    Model represents person in the database.
    """
    
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40))
    surname = Column(String(40))
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.name} {self.surname} {self.age}"




