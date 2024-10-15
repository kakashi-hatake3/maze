import random

from src.cell import Cell
from src.enums import RoadQualityStatus, CellName, ExternalSides


class Field:
    """Класс-контейнер для всех ячеек в лабиринте.

    :param width: Ширина лабиринта.
    :param height: Высота лабиринта.
    :param start_coord: Координаты старта.
    :param finish_coord: Координаты финиша.
    """

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
        self.pretended_neighbours = []
        self.current_cell: Cell = Cell(0)
        self.matrix = [Cell(i) for i in range(width * height)]
        self.start, self.finish = self.set_start_and_finish()
        self.initialize_neighbours()

    def setup_current_cell(self) -> None:
        """Ставит параметры для текущей ячейки дороги."""
        self.current_cell.is_visited = True
        if self.current_cell != self.start and self.current_cell != self.finish:
            self.current_cell.name = CellName.road.value
            self.current_cell.road_quality = random.choice(
                [
                    RoadQualityStatus.good.value,
                    RoadQualityStatus.bad.value,
                    RoadQualityStatus.normal.value
                ]
            )

    def add_pretended_neighbours(self) -> None:
        """Добавляет новых возможных соседей."""
        for neighbour in self.current_cell.neighbours:
            neighbour.cell_neighbours_status = [
                c.is_visited for c in neighbour.neighbours
            ]
            if (
                not neighbour.is_visited
                and neighbour.cell_neighbours_status.count(True) < 2
                and neighbour not in self.pretended_neighbours
            ):
                self.pretended_neighbours.append(neighbour)

    def generate_field(self) -> None:
        pass

    def initialize_available_sides_for_neighbours(self, cell: Cell) -> None:
        """Определяет в каких сторонах от клетки мб соседи."""
        if cell.is_external:
            if cell.index < self.width:
                cell.external_side.append(ExternalSides.up)
            if cell.index >= self.width * (self.height - 1):
                cell.external_side.append(ExternalSides.down)
            if cell.index % self.width == self.width - 1:
                cell.external_side.append(ExternalSides.right)
            if cell.index % self.width == 0:
                cell.external_side.append(ExternalSides.left)
            for i in cell.external_side:
                cell.available_sides_for_neighbours.remove(i)

    def add_neighbours(self, cell: Cell) -> None:
        """Добавляет соседей ячейки."""
        self.initialize_available_sides_for_neighbours(cell)
        for side in cell.available_sides_for_neighbours:
            match side:
                case ExternalSides.down:
                    cell.neighbours.append(self.matrix[cell.index + self.width])
                case ExternalSides.up:
                    cell.neighbours.append(self.matrix[cell.index - self.width])
                case ExternalSides.right:
                    cell.neighbours.append(self.matrix[cell.index + 1])
                case ExternalSides.left:
                    cell.neighbours.append(self.matrix[cell.index - 1])

    def initialize_neighbours(self) -> None:
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
        cell_start.name = CellName.road.value
        cell_start.road_quality = RoadQualityStatus.start.value
        cell_finish.is_finish = True
        cell_finish.name = CellName.road.value
        cell_finish.road_quality = RoadQualityStatus.finish.value
        return cell_start, cell_finish

    def __str__(self):
        result = ""
        for i in range(self.height):
            for j in range(self.width):
                result += str(self.matrix[i * self.width + j])
            result += "\n"
        return result
