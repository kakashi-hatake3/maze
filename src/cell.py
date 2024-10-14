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
        self.name: str = "wall"
        self.road_quality: str = "normal"
        self.is_visited: bool = False
        self.is_external: bool = False
        self.available_sides_for_neighbours = ["down", "up", "right", "left"]
        self.neighbours = []
        self.external_side = []
        self.cell_neighbours_status = []

    def __str__(self):
        match self.name:
            case "wall":
                return "#"
            case "road":
                match self.road_quality:
                    case "start":
                        return "\33[32m" + "S" + "\033[0m"  # 32 - green
                    case "finish":
                        return "\33[32m" + "F" + "\033[0m"  # 32 - green
                    case "good":
                        if self.is_this_the_way:
                            return "\33[34m" + "$" + "\033[0m"  # 34 - blue
                        if self.is_visited:
                            return "\33[35m" + "$" + "\033[0m"  # 35 - magenta
                        return "$"
                    case "bad":
                        if self.is_this_the_way:
                            return "\33[34m" + "^" + "\033[0m"  # 34 - blue
                        if self.is_visited:
                            return "\33[35m" + "^" + "\033[0m"  # 35 - magenta
                        return "^"
                    case "normal":
                        if self.is_this_the_way:
                            return "\33[34m" + "*" + "\033[0m"  # 34 - blue
                        if self.is_visited:
                            return "\33[35m" + "*" + "\033[0m"  # 35 - magenta
                        return "*"
