import pytest

from src.field import Field
from src.wave_front_solve import WaveFrontSolver


def test_unavailable_field():
    field = Field(1, 3, (0, 0), (0, 2))
    field.generate_field()
    dijkstra = WaveFrontSolver(field)
    assert dijkstra.solve_field() == float('inf')

@pytest.mark.parametrize("quality", ["bad", "normal", "good"])
def test_available_field(quality):
    field = Field(1, 3, (0, 0), (0, 2))
    field.generate_field()
    field.matrix[1].name = 'road'
    field.matrix[1].is_visited = True
    field.matrix[1].road_quality = quality
    dijkstra = WaveFrontSolver(field)
    assert dijkstra.solve_field() == dijkstra.weights[quality]
