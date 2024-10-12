import pytest

from src.menu_choose import MenuChoose


@pytest.fixture(scope="module")
def menu_choose():
    return MenuChoose()


def test_choose_generate_growing_tree(menu_choose, mocker):
    mocker.patch('builtins.input', side_effect=[''])
    result = menu_choose.choose_generate()
    assert result == "Growing Tree"


def test_choose_generate_recursive_backtracker(menu_choose, mocker):
    mocker.patch('builtins.input', side_effect=['s', ''])
    result = menu_choose.choose_generate()
    assert result == "Recursive Backtracker"


def test_choose_generate_exit(menu_choose, mocker):
    mocker.patch('builtins.input', side_effect=['w', ''])
    result = menu_choose.choose_generate()
    assert result == "Recursive Backtracker"


def test_choose_solve_dijkstra(menu_choose, mocker):
    mocker.patch('builtins.input', side_effect=[''])
    result = menu_choose.choose_solve()
    assert result == "Dijkstra"


def test_choose_solve_wave_front(menu_choose, mocker):
    mocker.patch('builtins.input', side_effect=['s', ''])
    result = menu_choose.choose_solve()
    assert result == "Wave Front"


def test_choose_solve_exit(menu_choose, mocker):
    mocker.patch('builtins.input', side_effect=['w', ''])
    result = menu_choose.choose_solve()
    assert result == "Wave Front"


def test_choose_width_and_height_positive(menu_choose, mocker):
    mocker.patch('os.system')
    mocker.patch('builtins.input', side_effect=[10, 15])
    assert menu_choose.choose_width_and_height() == (10, 15)


def test_choose_width_and_height_negative(capfd, menu_choose, mocker):
    mocker.patch('os.system')
    mocker.patch('builtins.input', side_effect=['asdad', 10, 15])
    assert menu_choose.choose_width_and_height() == (10, 15)


def test_choose_start_and_finish_positive(menu_choose, mocker):
    mocker.patch('os.system')
    mocker.patch('builtins.input', side_effect=[0, 1, 2, 0])
    assert menu_choose.choose_start_and_finish() == ((0, 1), (2, 0))


def test_choose_start_and_finish_negative(menu_choose, mocker):
    mocker.patch('os.system')
    mocker.patch('builtins.input', side_effect=['asd', 0, 'asd', 2, 0, 'xc', 0, 1, 2, 0])
    assert menu_choose.choose_start_and_finish() == ((0, 1), (2, 0))
