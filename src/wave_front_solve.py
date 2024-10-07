from collections import deque
from src.solver import Solver


class WaveFrontSolver(Solver):
    """Класс для решения лабиринта с помощью алгоритма wall follower."""

    def __init__(self, field: "Field"):
        super().__init__(field)

    def solve_field(self):
        """
        Решает лабиринт с помощью алгоритма wave front, работает как BFS.

        Queue используется для хранения ячеек, которые необходимо посетить
        следующими. Ячейки, которые уже были посещены, не помещаются в queue.
        Расстояния от старта до каждой ячейки хранятся в словаре.

        :return: Длина кратчайшего пути от старта до финиша.
        """
        queue = deque()
        queue.append(self.start)
        distances = {self.start: 0}
        visited = []
        while queue:
            current_cell = queue.popleft()
            if current_cell == self.finish:
                return distances[current_cell]
            if current_cell in visited:
                continue
            visited.append(current_cell)
            current_cell.is_this_the_way = True
            for neighbour in current_cell.neighbours:
                if not neighbour.is_visited or neighbour in visited:
                    continue
                if neighbour not in distances:
                    distances[neighbour] = (
                        distances[current_cell] + self.weights[neighbour.road_quality]
                    )
                    queue.append(neighbour)
        return float("inf")
