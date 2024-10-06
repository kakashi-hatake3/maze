import random

from src.field import Field
from src.stack import Stack


class RecursiveBacktrackerField(Field):
    """Класс для генерации поля с помощью алгоритма Recursive Backtracker."""

    def __init__(self, width: int, height: int):
        super().__init__(width, height)

    def generate_field(self):
        """Генерирует поле согласно адаптированному алгоритму бэктрекинга."""
        stack = Stack()
        current_cell = self.start
        stack.push(current_cell)
        while not stack.empty():
            current_cell.is_visited = True
            if current_cell != self.start and current_cell != self.finish:
                current_cell.name = 'road'
                current_cell.road_quality = random.choice(['good', 'bad', 'normal'])
            pretended_neighbours = []
            for cell in current_cell.neighbours:
                cell.cell_neighbours_status = [c.is_visited for c in cell.neighbours]
                if not cell.is_visited and cell.cell_neighbours_status.count(True) < 2:
                    pretended_neighbours.append(cell)
            if len(pretended_neighbours) > 0:
                if current_cell not in stack.stack:
                    stack.push(current_cell)
                current_cell = random.choice(pretended_neighbours)
            else:
                current_cell = stack.pop()
