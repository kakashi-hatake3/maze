from src.growing_tree_generate import GrowingTreeField


def test_generate_field():
    field = GrowingTreeField(10, 6)
    field.generate_field()
    for cell in field.matrix:
        if cell.name == 'road':
            assert cell.cell_neighbours_status.count(True) <= 3
