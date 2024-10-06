from collections import deque

from src.solver import Solver


class WaveFrontSolver(Solver):
    """Класс для решения лабиринта с помощью алгоритма wall follower."""

    def __init__(self, field: 'Field'):
        super().__init__(field)

    def solve_field(self):
        """Реализация алгоритма wave front."""
        queue = deque()  # Очередь для клеток, которые нужно обработать
        queue.append(self.start)  # Начинаем с начальной клетки
        distances = {self.start: 0}  # Словарь для хранения расстояний от старта
        visited = []  # Список для хранения посещенных клеток

        while queue:
            current_cell = queue.popleft()  # Вытаскиваем первую клетку из очереди

            if current_cell == self.finish:  # Если дошли до цели — возвращаем расстояние
                return distances[current_cell]

            if current_cell in visited:  # Пропускаем уже посещенные клетки
                continue

            visited.append(current_cell)
            current_cell.is_this_the_way = True  # Помечаем, что эта клетка входит в найденный путь

            # Проходим по всем соседям текущей клетки
            for neighbour in current_cell.neighbours:
                if not neighbour.is_visited or neighbour in visited:  # Пропускаем посещенные и непроходимые клетки
                    continue

                # Если сосед еще не был посещен
                if neighbour not in distances:
                    distances[neighbour] = distances[current_cell] + self.weights[neighbour.road_quality]  # Обновляем расстояние
                    queue.append(neighbour)  # Добавляем соседа в очередь для дальнейшего рассмотрения
        # Если мы не нашли пути до финиша
        return float('inf')
