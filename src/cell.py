class Cell:
    """Класс ячейки."""

    def __init__(self, index: int):
        self.index = index
        self.is_finish = False
        self.is_start = False
        self.is_this_the_way = False
        self.name: str = "wall"
        self.road_quality: str = "normal"
        self.is_visited: bool = False
        self.is_external: bool = False
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
