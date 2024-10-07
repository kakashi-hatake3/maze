from src.field import Field


class Solver:
    """Класс для решения лабиринта."""

    def __init__(self, field: Field):
        self.field = field
        self.start = field.start
        self.finish = field.finish
        self.finish.is_visited = True
        self.weights = {
            "normal": 2,
            "good": 1,
            "bad": 3,
            "start": 0,  # для старта вес можно считать как 0
            "finish": 0,  # для финиша вес не влияет
        }

    def solve_field(self):
        """Переопределяемый метод."""
        pass
