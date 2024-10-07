from src.recursive_backtracker_generate import RecursiveBacktrackerField


def test_generate_field():
    field = RecursiveBacktrackerField(10, 6)
    field.generate_field()
    for cell in field.matrix:
        if cell.name == "road":
            assert cell.cell_neighbours_status.count(True) <= 3
