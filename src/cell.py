class Cell:
    def __init__(self, width: int, height: int):
        self.index: int = 0
        self.name: str = 'wall'
        self.road_quality: str = 'normal'
        self.is_visited: bool = False
        self.is_external: bool = False
        self.neighbors = []
        if self.is_external:
            # self.external_side: str = ''
            self.external_side = []
            if self.index < width:
                self.external_side.append('down')
            if self.index >= width * (height - 1):
                self.external_side.append('up')
            if self.index % width == width - 1:
                self.external_side.append('right')
            if self.index % width == 0:
                self.external_side.append('left')

    def add_neighbors(self, field: 'Field'):
        base_sides = ['down', 'up', 'right', 'left']
        matrix = field.matrix
        width = field.width
        if self.is_external:
            for i in self.external_side:
                base_sides.remove(i)
        for side in base_sides:
            match side:
                case 'down':
                    self.neighbors.append(matrix[self.index - width])
                case 'up':
                    self.neighbors.append(matrix[self.index + width])
                case 'right':
                    self.neighbors.append(matrix[self.index + 1])
                case 'left':
                    self.neighbors.append(matrix[self.index - 1])


    def __str__(self):
        match self.name:
            case 'wall':
                return '#'
            case 'road':
                match self.road_quality:
                    case 'good':
                        return '$'
                    case 'bad':
                        return '^'
                    case 'normal':
                        return ' '
