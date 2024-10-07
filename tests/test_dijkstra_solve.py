import pytest

from src.dijkstra_solve import DijkstraSolver
from src.field import Field


def test_unavailable_field():
    field = Field(1, 3, (0, 0), (0, 2))
    field.generate_field()
    dijkstra = DijkstraSolver(field)
    assert dijkstra.solve_field() == float('inf')

@pytest.mark.parametrize("quality", ["bad", "normal", "good"])
def test_available_field(quality):
    field = Field(1, 3, (0, 0), (0, 2))
    field.generate_field()
    field.matrix[1].name = 'road'
    field.matrix[1].is_visited = True
    field.matrix[1].road_quality = quality
    dijkstra = DijkstraSolver(field)
    assert dijkstra.solve_field() == dijkstra.weights[quality]
