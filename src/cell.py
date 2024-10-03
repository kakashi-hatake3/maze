class Cell:
    """Класс ячейки."""

    def __init__(self, field: 'Field', index: int):
        self.field = field
        self.index = index
        self.is_finish = False
        self.is_start = False
        self.name: str = 'wall'
        self.road_quality: str = 'normal'
        self.is_visited: bool = False
        self.is_external: bool = False
        self.neighbors = []
        self.external_side = []
        self.cell_neighbors_status = []

    def add_neighbors(self):
        """Добавляет соседей ячейки."""
        available_sides = ['down', 'up', 'right', 'left']
        matrix = self.field.matrix
        width = self.field.width
        if self.is_external:
            if self.index < self.field.width:
                self.external_side.append('up')
            if self.index >= self.field.width * (self.field.height - 1):
                self.external_side.append('down')
            if self.index % self.field.width == self.field.width - 1:
                self.external_side.append('right')
            if self.index % self.field.width == 0:
                self.external_side.append('left')
            for i in self.external_side:
                available_sides.remove(i)
        for side in available_sides:
            match side:
                case 'down':
                    self.neighbors.append(matrix[self.index + width])
                case 'up':
                    self.neighbors.append(matrix[self.index - width])
                case 'right':
                    self.neighbors.append(matrix[self.index + 1])
                case 'left':
                    self.neighbors.append(matrix[self.index - 1])

    def __str__(self):
        match self.name:
            case 'wall':
                return '#'
            case 'road':
                if self.is_visited:
                    return 'X'
                match self.road_quality:
                    case 'good':
                        return '$'
                    case 'bad':
                        return '^'
                    case 'normal':
                        return ' '
