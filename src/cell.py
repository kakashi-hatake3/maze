from src.enums import CellName, RoadQualityStatus, ExternalSides, CellSymbols


class Cell:
    """Класс ячейки.

    :param index: индекс ячейки в матрице
    :type index: int
    :param is_finish: флаг, проверяющий ячейку является ли она финишной
    :type is_finish: bool
    :param is_start: флаг, проверяющий ячейку является ли она стартной
    :type is_start: bool
    :param is_this_the_way: флаг, проверяющий ячейку является ли она в пути
    :type is_this_the_way: bool
    :param name: имя ячейки
    :type name: str
    :param road_quality: качество дороги
    :type road_quality: str
    :param is_visited: флаг, проверяющий ячейку является ли она посещенной
    :type is_visited: bool
    :param is_external: флаг, проверяющий ячейку является ли она внешней
    :type is_external: bool
    :param neighbours: список соседних ячейок
    :type neighbours: list
    :param external_side: список сторон, которые являются внешними
    :type external_side: list
    :param cell_neighbours_status: список статусов соседей
    :type cell_neighbours_status: list
    """

    def __init__(self, index: int):
        self.index = index
        self.is_finish = False
        self.is_start = False
        self.is_this_the_way = False
        self.name: str = CellName.wall.value
        self.road_quality: str = ""
        self.is_visited: bool = False
        self.is_external: bool = False
        self.available_sides_for_neighbours = [
            ExternalSides.down,
            ExternalSides.up,
            ExternalSides.right,
            ExternalSides.left
        ]
        self.neighbours = []
        self.external_side = []
        self.cell_neighbours_status = []

    @staticmethod
    def color_text(text, color_code):
        return f"\33[{color_code}m{text}\033[0m"

    def color_green(self, text):
        return self.color_text(text, 32)

    def color_blue(self, text):
        return self.color_text(text, 34)

    def color_magenta(self, text):
        return self.color_text(text, 35)

    def get_symbol(self):
        symbols = {
            RoadQualityStatus.start.value: CellSymbols.start.value,
            RoadQualityStatus.finish.value: CellSymbols.finish.value,
            RoadQualityStatus.good.value: CellSymbols.good_road.value,
            RoadQualityStatus.bad.value: CellSymbols.bad_road.value,
            RoadQualityStatus.normal.value: CellSymbols.normal_road.value
        }

        symbol = symbols.get(self.road_quality, CellSymbols.wall.value)

        if (
                self.road_quality == RoadQualityStatus.start.value
                or self.road_quality == RoadQualityStatus.finish.value
        ):
            return self.color_green(symbol)
        elif self.is_this_the_way:
            return self.color_blue(symbol)
        elif self.is_visited:
            return self.color_magenta(symbol)
        return symbol

    def __str__(self):
        return self.get_symbol()
