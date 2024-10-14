import os
from time import sleep

from src.menu import Menu


class MenuChoose:
    """Класс объединяющий методы для выбора параметров лабиринта."""

    @staticmethod
    def choose_generate() -> str:
        """
        Меню для выбора алгоритма генерации лабиринта.

        :return: строка, выбранный алгоритм, или дефолт значение, если пользователь вышел из меню
        """
        generate_menu = Menu()
        generate_menu.options = ["Growing Tree", "Recursive Backtracker", "Выход"]
        while not generate_menu.exit:
            generate_menu.print_menu()
            if generate_menu.handle_key() == "enter" and generate_menu.exit is False:
                selected_item = generate_menu.options[generate_menu.selected_index]
                if selected_item != "Выход":
                    return selected_item
                generate_menu.exit = True
        return "Recursive Backtracker"

    @staticmethod
    def choose_solve() -> str:
        """
        Меню выбора алгоритма решения.

        :return: имя выбранного алгоритма или дефолтное значение "Wave Front"
        """
        solve_menu = Menu()
        solve_menu.options = ["Dijkstra", "Wave Front", "Выход"]
        while not solve_menu.exit:
            solve_menu.print_menu()
            if solve_menu.handle_key() == "enter" and solve_menu.exit is False:
                selected_item = solve_menu.options[solve_menu.selected_index]
                if selected_item != "Выход":
                    return selected_item
                solve_menu.exit = True
        return "Wave Front"

    def choose_width_and_height(self) -> tuple[int, int]:
        """
        Выбор ширины и длины лабиринта.

        Очищает консоль и предлагает пользователю выбрать ширину и длину лабиринта.
        Если пользователь вводит некорректные данные, то выводится сообщение
        "Некорректные данные" и функция перезапрашивает ввод.

        :return: кортеж из двух целых чисел - ширины и длины лабиринта.
        """
        os.system("cls")
        try:
            return int(input("Длина лабиринта: ")), int(input("Ширина лабиринта: "))
        except ValueError:
            print("Некорректные данные")
            sleep(0.1)
            return self.choose_width_and_height()

    def choose_start_and_finish(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """
        Функция для ввода координат старта и финиша.

        Функция очищает консоль и предлагает пользователю ввести координаты
        старта и финиша. Если пользователь вводит некорректные данные, то
        выводится сообщение "Некорректные данные" и функция перезапрашивает ввод.

        :return: кортеж из двух tuple, в которых содержатся координаты
            старта и финиша соответственно.
        """
        os.system("cls")
        try:
            start_x = int(input("X координата старта: "))
            start_y = int(input("Y координата старта: "))
            finish_x = int(input("X координата финиша: "))
            finish_y = int(input("Y координата финиша: "))
        except ValueError:
            print("Некорректные данные")
            sleep(0.1)
            return self.choose_start_and_finish()
        else:
            return (start_x, start_y), (finish_x, finish_y)
