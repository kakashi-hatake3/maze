from src.recursive_backtracker_generate import RecursiveBacktrackerField
from src.solver import Solver


def test_solver():
    field = RecursiveBacktrackerField(10, 6)
    field.generate_field()
    solver = Solver(field)
    assert solver.finish.is_visited
