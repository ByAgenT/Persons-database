from console_menu import Menu
from database_controller import DatabaseConnector
import sys


def main():
    db_path: str = None
    if len(sys.argv) >= 2:
        db_path = sys.argv[1]
    if db_path:
        db_conn = DatabaseConnector(db_path)
    else:
        raise ValueError("No database path")
    menu: Menu = Menu(db_conn)
    while True:
        menu.print_menu()
        if not menu.listen_to_command():
            break


if __name__ == '__main__':
    main()
