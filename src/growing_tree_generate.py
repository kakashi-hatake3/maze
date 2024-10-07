import random

from src.field import Field


class GrowingTreeField(Field):
    """Класс для генерации поля с помощью алгоритма growing tree."""

    def __init__(self, width: int, height: int, *args):
        super().__init__(width, height, *args)

    def generate_field(self) -> None:
        """
        Генерирует поле согласно алгоритму growing tree.

        Алгоритм growing tree выбирает случайного соседа, не посещенного до этого,
        и добавляет его к списку ячеек, которые нужно посетить. Затем выбирается
        случайная ячейка из списка и становится текущей. Если у соседей ячейки
        больше двух непосещенных соседей, то она удаляется из списка.

        :return: None
        """
        pretended_cells = []
        current_cell = self.start
        while len(pretended_cells) > 0 or current_cell == self.start:
            current_cell.is_visited = True
            if current_cell != self.start and current_cell != self.finish:
                current_cell.name = 'road'
                current_cell.road_quality = random.choice(['good', 'bad', 'normal'])
            for neighbour in current_cell.neighbours:
                if not neighbour.is_visited:
                    neighbor_cell_neighbours_status = [c.is_visited for c in neighbour.neighbours]
                    if neighbor_cell_neighbours_status.count(True) < 2 and neighbour not in pretended_cells:
                        pretended_cells.append(neighbour)
            # Проверка на то, что у соседей больше двух непосещенных соседей
            for cell in pretended_cells:
                neighbor_cell_neighbours_status = [c.is_visited for c in cell.neighbours]
                if neighbor_cell_neighbours_status.count(True) >= 2:
                    pretended_cells.remove(cell)
            if len(pretended_cells) > 0:
                current_cell = random.choice(pretended_cells)
                pretended_cells.remove(current_cell)
