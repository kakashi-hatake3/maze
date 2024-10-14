import random

from src.field import Field
from src.stack import Stack


class RecursiveBacktrackerField(Field):
    """Класс для генерации поля с помощью алгоритма Recursive Backtracker."""

    def __init__(self, width: int, height: int, *args):
        super().__init__(width, height, *args)

    def generate_field(self) -> None:
        """
        Генерирует поле согласно алгоритму Recursive Backtracker.

        Recursive Backtracker - это алгоритм, который строит лабиринт методом DFS.
        Он начинает с любого места в лабиринте и шаг за шагом строит лабиринт,
        выбирая направление, в котором можно пройти. Я его изменил,
        теперь он не вызывается рекурсивно, а выполняется в цикле

        :return: None
        """
        stack = Stack()
        self.current_cell = self.start
        stack.push(self.current_cell)
        while not stack.empty():

            self.setup_current_cell()

            self.pretended_neighbours = []

            self.add_pretended_neighbours()

            if len(self.pretended_neighbours) > 0:
                if self.current_cell not in stack.stack:
                    stack.push(self.current_cell)
                self.current_cell = random.choice(self.pretended_neighbours)
            else:
                self.current_cell = stack.pop()
