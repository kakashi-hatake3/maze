from src.field import Field


class KruskalField(Field):
    """Класс для генерации поля с помощью алгоритма Kruskal."""

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.edges = []
        self.initialize_edges()
        # print(self.edges[0][0].index, self.edges[0][1].index)

    def initialize_edges(self):
        """Инициализирует ребра."""
        for cell in self.matrix:
            for neighbour in cell.neighbours:
                self.edges.append(tuple(sorted((cell, neighbour), key=lambda x: x.index)))
        self.edges = list(set(self.edges))

    def generate_field(self):
        """Генерирует поле согласно алгоритму Kruskal."""

