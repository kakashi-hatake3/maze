import random

from src.field import Field
from src.stack import Stack


class RecursiveBacktrackerField(Field):

    def __init__(self, width: int, height: int):
        super().__init__(width, height)

    def generate_field(self):
        stack = Stack()
        current_cell = self.start
        stack.push(current_cell)
        while not stack.empty():
            current_cell.is_visited = True
            current_cell.name = 'road'
            current_cell.road_quality = random.choice(['good', 'bad', 'normal'])



            pretended_neighbors = []
            for cell in current_cell.neighbors:
                cell.cell_neighbors_status = [c.is_visited for c in cell.neighbors]
                if not cell.is_visited and cell.cell_neighbors_status.count(True) < 2:
                    pretended_neighbors.append(cell)
            if len(pretended_neighbors) > 0:
                if current_cell not in stack.stack:
                    stack.push(current_cell)
                current_cell = random.choice(pretended_neighbors)
            else:
                current_cell = stack.pop()
