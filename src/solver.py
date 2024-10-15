from src.enums import RoadQualityStatus
from src.field import Field


class Solver:
    """Класс для решения лабиринта."""

    def __init__(self, field: Field):
        self.field = field
        self.start = field.start
        self.finish = field.finish
        self.finish.is_visited = True
        self.weights = {
            RoadQualityStatus.normal.value: 2,
            RoadQualityStatus.good.value: 1,
            RoadQualityStatus.bad.value: 3,
            RoadQualityStatus.start.value: 0,  # для старта вес можно считать как 0
            RoadQualityStatus.finish.value: 0,  # для финиша вес не влияет
        }

    def solve_field(self):
        """Переопределяемый метод."""
        pass
