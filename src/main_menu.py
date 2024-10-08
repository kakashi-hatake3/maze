from src.menu import Menu


class MainMenu(Menu):
    """Главное меню.

    :param options: Список возможных действий.
    :type options: list
    :param generate: Алгоритм генерации лабиринта.
    :type generate: str
    :param solve: Алгоритм решения лабиринта.
    :type solve: str
    :param width: Ширина лабиринта.
    :type width: int
    :param height: Высота лабиринта.
    :type height: int
    :param start: Координаты старта.
    """

    def __init__(self):
        self.options = [
            "Выбрать алгоритм генерации",
            "Выбрать алгоритм решения",
            "Ввести длину и ширину лабиринта",
            "Ввести координаты старта и финиша",
            "Печать",
            "Выход",
        ]
        self.generate = "Recursive Backtracker"
        self.solve = "Wave Front"
        self.width = 3
        self.height = 3
        self.start = None
        self.finish = None
        self.field = None
