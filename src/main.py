import logging
import os
import platform
from time import sleep

from src.dijkstra_solve import DijkstraSolver
from src.growing_tree_generate import GrowingTreeField
from src.main_menu import MainMenu
from src.menu import Menu
from src.recursive_backtracker_generate import RecursiveBacktrackerField
from src.wave_front_solve import WaveFrontSolver

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info(platform.python_version())
    menu = MainMenu()
    while not menu.exit:
        menu.print_menu()
        if menu.handle_key() == 'enter' and menu.exit is False:
            menu_selected_index = menu.options[menu.selected_index]
            match menu_selected_index:
                case "Выбрать алгоритм генерации":
                    generate_menu = Menu()
                    generate_menu.options = ["Growing Tree", "Recursive Backtracker", "Выход"]
                    while not generate_menu.exit:
                        generate_menu.print_menu()
                        if generate_menu.handle_key() == 'enter' and generate_menu.exit is False:
                            selected_item = generate_menu.options[generate_menu.selected_index]
                            if selected_item != 'Выход':
                                menu.generate = selected_item
                            generate_menu.exit = True

                case "Выбрать алгоритм решения":
                    solve_menu = Menu()
                    solve_menu.options = ["Dijkstra", "Wave Front", "Выход"]
                    while not solve_menu.exit:
                        solve_menu.print_menu()
                        if solve_menu.handle_key() == 'enter' and solve_menu.exit is False:
                            selected_item = solve_menu.options[solve_menu.selected_index]
                            if selected_item != 'Выход':
                                menu.solve = selected_item
                            solve_menu.exit = True

                case "Ввести длину и ширину лабиринта":
                    os.system('cls')
                    try:
                        menu.width = int(input("Длина лабиринта: "))
                        menu.height = int(input("Ширина лабиринта: "))
                    except ValueError:
                        print("Некорректные данные")
                        sleep(0.1)
                        continue

                case "Ввести координаты старта и финиша":
                    os.system('cls')
                    try:
                        start_x = int(input("X координата старта: "))
                        start_y = int(input("Y координата старта: "))
                        finish_x = int(input("X координата финиша: "))
                        finish_y = int(input("Y координата финиша: "))
                    except ValueError:
                        print("Некорректные данные")
                        sleep(0.1)
                        continue
                    else:
                        menu.start = (start_x, start_y)
                        menu.finish = (finish_x, finish_y)

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
