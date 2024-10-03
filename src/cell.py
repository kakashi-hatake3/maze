class Cell:
    def __init__(self):
        self.index: int
        self.name: str = 'wall'
        self.road_quality: str = 'normal'

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
