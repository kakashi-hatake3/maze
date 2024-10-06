import random

from src.field import Field


class GrowingTreeField(Field):
    """Класс для генерации поля с помощью алгоритма growing tree."""

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        # self.edges = []
        # self.initialize_edges()
        # print(self.edges[0][0].index, self.edges[0][1].index)

    # def initialize_edges(self):
    #     """Инициализирует ребра."""
    #     for cell in self.matrix:
    #         for neighbour in cell.neighbours:
    #             self.edges.append(tuple(sorted((cell, neighbour), key=lambda x: x.index)))
    #     self.edges = list(set(self.edges))

    def generate_field(self):
        """Генерирует поле согласно алгоритму growing tree."""
        pretended_cells = []
        current_cell = self.start
        while len(pretended_cells) > 0 or current_cell == self.start:
            current_cell.is_visited = True
            current_cell.name = 'road'
            current_cell.road_quality = random.choice(['good', 'bad', 'normal'])
            for neighbour in current_cell.neighbours:
                if not neighbour.is_visited:
                    neighbor_cell_neighbours_status = [c.is_visited for c in neighbour.neighbours]
                    if neighbor_cell_neighbours_status.count(True) < 2 and neighbour not in pretended_cells:
                        pretended_cells.append(neighbour)
            for cell in pretended_cells:
                neighbor_cell_neighbours_status = [c.is_visited for c in cell.neighbours]
                if neighbor_cell_neighbours_status.count(True) >= 2:
                    pretended_cells.remove(cell)
            if len(pretended_cells) > 0:
                current_cell = random.choice(pretended_cells)
                pretended_cells.remove(current_cell)
