import logging
import os
import platform
from time import sleep

from src.dijkstra_solve import DijkstraSolver
from src.growing_tree_generate import GrowingTreeField
from src.main_menu import MainMenu
from src.menu import Menu
from src.menu_choose import MenuChoose
from src.recursive_backtracker_generate import RecursiveBacktrackerField
from src.wave_front_solve import WaveFrontSolver

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info(platform.python_version())
    menu = MainMenu()
    menu_choose = MenuChoose()
    while not menu.exit:
        menu.print_menu()
        if menu.handle_key() == 'enter' and menu.exit is False:
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
                    os.system('cls')
                    match menu.generate:
                        case "Growing Tree":
                            menu.field = GrowingTreeField(
                                menu.width,
                                menu.height,
                                menu.start,
                                menu.finish
                            )
                        case "Recursive Backtracker":
                            menu.field = RecursiveBacktrackerField(
                                menu.width,
                                menu.height,
                                menu.start,
                                menu.finish
                            )
                    menu.field.generate_field()
                    print(menu.field)

                    solver = None

                    match menu.solve:
                        case "Dijkstra":
                            solver = DijkstraSolver(menu.field)
                        case "Wave Front":
                            solver = WaveFrontSolver(menu.field)
                    count_of_steps = solver.solve_field()
                    if count_of_steps != float('inf'):
                        print('Длина пути: ' + str(count_of_steps))
                    else:
                        print('Путь не существует')
                    print(menu.field)

                    sleep(5)

                case "Выход":
                    menu.exit_menu()


if __name__ == "__main__":
    main()
