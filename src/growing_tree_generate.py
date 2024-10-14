import random

from src.field import Field


class GrowingTreeField(Field):
    """Класс для генерации поля с помощью алгоритма growing tree."""

    def __init__(self, width: int, height: int, *args):
        super().__init__(width, height, *args)

    def check_unvisited_neighbours(self) -> None:
        """Проверяем соседей из списка возможных следующих ходов."""
        for cell in self.pretended_neighbours:
            neighbor_cell_neighbours_status = [c.is_visited for c in cell.neighbours]
            if neighbor_cell_neighbours_status.count(True) >= 2:
                self.pretended_neighbours.remove(cell)

    def generate_field(self) -> None:
        """
        Генерирует поле согласно алгоритму growing tree.

        Алгоритм growing tree выбирает случайного соседа, не посещенного до этого,
        и добавляет его к списку ячеек, которые нужно посетить. Затем выбирается
        случайная ячейка из списка и становится текущей. Если у соседей ячейки
        больше двух непосещенных соседей, то она удаляется из списка.

        :return: None
        """
        self.current_cell = self.start
        while len(self.pretended_neighbours) > 0 or self.current_cell == self.start:

            self.setup_current_cell()

            self.add_pretended_neighbours()

            self.check_unvisited_neighbours()

            if len(self.pretended_neighbours) > 0:
                self.current_cell = random.choice(self.pretended_neighbours)
                self.pretended_neighbours.remove(self.current_cell)
