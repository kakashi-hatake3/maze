import random

from src.cell import Cell


class Field:
    """Класс-контейнер для всех ячеек на поле."""

    def __init__(
        self,
        width: int,
        height: int,
        start_coord: tuple[int, int] | None = None,
        finish_coord: tuple[int, int] | None = None,
    ):
        self.start_coord = start_coord
        self.finish_coord = finish_coord
        self.width = width
        self.height = height
        if self.width < 2 and self.height < 2:
            print("Минимум может быть 2 ячейки")
            exit()
        self.matrix = [Cell(i) for i in range(width * height)]
        self.start, self.finish = self.set_start_and_finish()
        self.initialize_neighbours()

    def generate_field(self):
        pass

    def add_neighbours(self, cell: Cell):
        """Добавляет соседей ячейки."""
        available_sides = ["down", "up", "right", "left"]
        if cell.is_external:
            if cell.index < self.width:
                cell.external_side.append("up")
            if cell.index >= self.width * (self.height - 1):
                cell.external_side.append("down")
            if cell.index % self.width == self.width - 1:
                cell.external_side.append("right")
            if cell.index % self.width == 0:
                cell.external_side.append("left")
            for i in cell.external_side:
                available_sides.remove(i)
        for side in available_sides:
            match side:
                case "down":
                    cell.neighbours.append(self.matrix[cell.index + self.width])
                case "up":
                    cell.neighbours.append(self.matrix[cell.index - self.width])
                case "right":
                    cell.neighbours.append(self.matrix[cell.index + 1])
                case "left":
                    cell.neighbours.append(self.matrix[cell.index - 1])

    def initialize_neighbours(self):
        """Инициализирует соседей для всех ячеек после создания матрицы."""
        for cell in self.matrix:
            self.add_neighbours(cell)
            cell.cell_neighbours_status = [c.is_visited for c in cell.neighbours]

    def set_start_and_finish(self) -> tuple[Cell, Cell]:
        """Устанавливает старт и финиш."""
        external_cells = []
        cell_start = None
        cell_finish = None
        for cell in self.matrix:
            if (
                cell.index < self.width
                or cell.index >= self.width * (self.height - 1)
                or cell.index % self.width == self.width - 1
                or cell.index % self.width == 0
            ):
                cell.is_external = True
                external_cells.append(cell)
        if self.start_coord is None or self.finish_coord is None:
            cell_start = random.choice(external_cells)
            external_cells.remove(cell_start)
            cell_finish = random.choice(external_cells)
        else:
            try:
                cell_start = self.matrix[
                    self.width * self.start_coord[1] + self.start_coord[0]
                ]
                cell_finish = self.matrix[
                    self.width * self.finish_coord[1] + self.finish_coord[0]
                ]
            except IndexError:
                print("Неверные координаты старта или финиша")
                exit()
            else:
                if cell_start.is_external and cell_finish.is_external:
                    pass
                else:
                    print("Старт и финиш должны быть внешними")
                    exit()
        cell_start.is_start = True
        cell_start.name = "road"
        cell_start.road_quality = "start"
        cell_finish.is_finish = True
        cell_finish.name = "road"
        cell_finish.road_quality = "finish"
        return cell_start, cell_finish

    def __str__(self):
        result = ""
        for i in range(self.height):
            for j in range(self.width):
                result += str(self.matrix[i * self.width + j])
            result += "\n"
        return result
