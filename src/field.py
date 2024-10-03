from src.cell import Cell


class Field:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.matrix = [Cell(self) for _ in range(width * height)]

    def __str__(self):
        result = ''
        for i in range(self.height):
            for j in range(self.width):
                result += str(self.matrix[i * self.width + j])
            result += '\n'
        return result
