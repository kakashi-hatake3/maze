import heapq

from src.solver import Solver


class DijkstraSolver(Solver):
    """Класс для решения с помощью алгоритма Дейкстры."""

    def __init__(self, field: 'Field'):
        super().__init__(field)

    def solve_field(self) -> float:
        """
        Решает лабиринт с помощью алгоритма Дейкстры.

        Приоритетная очередь используется для хранения ячеек, которые необходимо посетить
        следующими. Приоритетом каждой ячейки является ее минимальное расстояние до
        старта. Расстояния также хранятся в словаре для быстрого доступа.

        :return: Длина кратчайшего пути от старта до финиша.
        """
        priority_queue = []
        heapq.heappush(priority_queue, (0, self.start.index, self.start))
        distances = {self.start: 0}
        visited = []
        while priority_queue:
            current_dist, _, current_cell = heapq.heappop(priority_queue)
            if current_cell == self.finish:
                return current_dist
            if current_cell in visited:
                continue
            visited.append(current_cell)
            current_cell.is_this_the_way = True
            for neighbour in current_cell.neighbours:
                if not neighbour.is_visited or neighbour in visited:
                    continue
                new_dist = distances[current_cell] + self.weights[neighbour.road_quality]
                if new_dist < distances.get(neighbour, float('inf')):
                    distances[neighbour] = new_dist
                    heapq.heappush(priority_queue, (new_dist, neighbour.index, neighbour))
        return float('inf')
