import pytest

from src.main_menu import MainMenu
from src.main_print import MainPrint


@pytest.fixture(scope="module")
def main_print():
    return MainPrint(MainMenu())


def test_generate_field_1(main_print):
    maze = main_print.generate_field()
    assert 'F' in str(maze) and 'S' in str(maze)


def test_generate_field_2(main_print):
    main_print.generate_field()
    assert main_print.menu.generate == "Recursive Backtracker"


def test_solve_field_1(main_print):
    main_print.menu.width = 3
    main_print.menu.height = 1
    main_print.menu.start = (0, 0)
    main_print.menu.finish = (2, 0)
    main_print.generate_field()
    main_print.menu.field.matrix[1].is_visited = False
    main_print.menu.field.matrix[1].name = 'wall'
    maze = main_print.solve_field()
    assert maze == 'Путь не существует'


def test_solve_field_2(main_print):
    main_print.menu.width = 3
    main_print.menu.height = 1
    main_print.menu.start = (0, 0)
    main_print.menu.finish = (2, 0)
    main_print.generate_field()
    main_print.menu.field.matrix[1].is_visited = True
    main_print.menu.field.matrix[1].name = 'road'
    main_print.menu.field.matrix[1].road_quality = 'bad'
    maze = main_print.solve_field()
    assert maze == 'Длина пути: 3'
