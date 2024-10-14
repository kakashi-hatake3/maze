import logging
import os
import platform
from time import sleep

from src.main_menu import MainMenu
from src.main_print import MainPrint
from src.menu_choose import MenuChoose

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info(platform.python_version())
    menu = MainMenu()
    menu_choose = MenuChoose()
    while not menu.exit:
        menu.print_menu()
        if menu.handle_key() == "enter" and menu.exit is False:
            menu_selected_index = menu.options[menu.selected_index]
            match menu_selected_index:
                case "Выбрать алгоритм генерации":
                    menu.generate = menu_choose.choose_generate()

                case "Выбрать алгоритм решения":
                    menu.solve = menu_choose.choose_solve()

                case "Ввести длину и ширину лабиринта":
                    menu.width, menu.height = menu_choose.choose_width_and_height()

                case "Ввести координаты старта и финиша":
                    menu.start, menu.finish = menu_choose.choose_start_and_finish()

                case "Печать":
                    os.system("cls")
                    main_print = MainPrint(menu)
                    print(main_print.generate_field())
                    print(main_print.solve_field())
                    print(main_print.print_field())
                    sleep(5)

                case "Выход":
                    menu.exit_menu()


if __name__ == "__main__":
    main()
