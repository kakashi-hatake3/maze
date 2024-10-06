import random

from cell import Cell


class Field:
    """Класс-контейнер для всех ячеек на поле."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.matrix = [Cell(self, i) for i in range(width * height)]
        self.start, self.finish = self.set_start()
        self.initialize_neighbours()

    def initialize_neighbours(self):
        """Инициализирует соседей для всех ячеек после создания матрицы."""
        for cell in self.matrix:
            cell.add_neighbours()
            cell.cell_neighbours_status = [c.is_visited for c in cell.neighbours]

    def set_start(self) -> tuple[Cell, Cell]:
        """Устанавливает старт."""
        external_cells = []
        for cell in self.matrix:
            if (cell.index < self.width
                    or cell.index >= self.width * (self.height - 1)
                    or cell.index % self.width == self.width - 1
                    or cell.index % self.width == 0):
                cell.is_external = True
                external_cells.append(cell)
        cell_start = random.choice(external_cells)
        cell_start.is_start = True
        external_cells.remove(cell_start)
        cell_finish = random.choice(external_cells)
        cell_finish.is_finish = True
        return cell_start, cell_finish

    def __str__(self):
        result = ''
        for i in range(self.height):
            for j in range(self.width):
                result += str(self.matrix[i * self.width + j])
            result += '\n'
        return result
