from database_controller import DatabaseConnector
from models.Person import Person
from enum import Enum

import re


class Menu:
    """
    Menu class representing
    """

    class MenuChoice(Enum):
        """
        Enum describing menu choices
        """
        ADD = 1
        REMOVE = 2
        DISPLAY = 3
        FILTER = 4
        EXIT = 5

    def __init__(self, db_controller: DatabaseConnector):
        self._database_controller: DatabaseConnector = db_controller

    @staticmethod
    def print_menu() -> None:
        """
        Print menu to the console

        :return: None
        """
        print(r"""1: Add new person
2: Remove person
3: Display all persons
4: Filter persons
5: Exit""")

    def listen_to_command(self) -> bool:
        """
        Listen to a command from a console input and then execute it

        :return: True if program should continue, otherwise false
        """
        command: int = input("Enter command: ")
        try:
            command: self.MenuChoice = self.MenuChoice(int(command))
            if command is self.MenuChoice.ADD:
                self.add()
            elif command is self.MenuChoice.REMOVE:
                pass
            elif command is self.MenuChoice.DISPLAY:
                self.display()
            elif command is self.MenuChoice.FILTER:
                pass
            elif command is self.MenuChoice.EXIT:
                return False
            return True
        except (ValueError, ):
            pass  # TODO: enum error

    def add(self) -> None:
        """
        Prompt person information and add new object to the database

        :return: None
        """
        while True:
            name: str = input("Enter first name: ")
            if re.match(r'^[a-z.,\']{1,40}$', name, re.IGNORECASE):
                break
            print("Incorrect first name")
        while True:
            surname: str = input("Enter surname: ")
            if re.match(r'^[a-z.,\']{1,40}$', surname, re.IGNORECASE):
                break
            print("Incorrect surname")

        while True:
            age: str = input("Enter age: ")
            try:
                age: int = int(age)
                if age > 0:
                    break
            except (ValueError, ):
                pass
            print("Incorrect age")

        person = Person(name=name, surname=surname, age=age)

        self._database_controller.add(person)

    def display(self) -> None:
        """
        Print all persons from database to the console

        :return: None
        """
        print("\t=PERSONS=")
        persons = self._database_controller.retrieve_all(Person)
        for person in persons:
            print(person)
        print("==========")

