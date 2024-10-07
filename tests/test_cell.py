import pytest

from src.field import Field

@pytest.fixture(scope="module")
def test_get_field():
    field = Field(3, 3)
    return field


@pytest.mark.parametrize("index", [0, 1, 2, 3, 5, 6, 7, 8])
def test_is_external(test_get_field, index):
    field = test_get_field
    assert field.matrix[index].is_external == True


@pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5, 6, 7, 8])
def test_check_external_sides(test_get_field, index):
    ind_to_sides = {
        0: ['up', 'left'],
        1: ['up'],
        2: ['up', 'right'],
        3: ['left'],
        4: [],
        5: ['right'],
        6: ['down', 'left'],
        7: ['down'],
        8: ['down', 'right'],
    }
    field = test_get_field
    assert field.matrix[index].external_side == ind_to_sides[index]


@pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5, 6, 7, 8])
def test_cell_neighbours(test_get_field, index):
    field = test_get_field
    cell = field.matrix[index]
    ind_to_neigh = {
        0: [field.matrix[1], field.matrix[3]],
        1: [field.matrix[0], field.matrix[2], field.matrix[4]],
        2: [field.matrix[1], field.matrix[5]],
        3: [field.matrix[0], field.matrix[4], field.matrix[6]],
        4: [field.matrix[1], field.matrix[3], field.matrix[5], field.matrix[7]],
        5: [field.matrix[2], field.matrix[4], field.matrix[8]],
        6: [field.matrix[3], field.matrix[7]],
        7: [field.matrix[4], field.matrix[6], field.matrix[8]],
        8: [field.matrix[5], field.matrix[7]],
    }
    assert sorted(cell.neighbours, key=lambda x: x.index) == ind_to_neigh[index]


@pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5])
def test_cell_print(index):
    field = Field(1, 6, (0, 0), (0, 5))

    field.matrix[1].name = 'road'
    field.matrix[1].is_visited = True
    field.matrix[1].road_quality = 'good'

    field.matrix[2].name = 'road'
    field.matrix[2].is_visited = True
    field.matrix[2].road_quality = 'normal'

    field.matrix[3].name = 'road'
    field.matrix[3].is_visited = True
    field.matrix[3].road_quality = 'bad'

    cell = field.matrix[index]
    ind_to_str = {
        0: '\x1b[32mS\x1b[0m',
        1: '\x1b[35m$\x1b[0m',
        2: '\x1b[35m*\x1b[0m',
        3: '\x1b[35m^\x1b[0m',
        4: '#',
        5: '\x1b[32mF\x1b[0m',
    }
    assert str(cell) == ind_to_str[index]