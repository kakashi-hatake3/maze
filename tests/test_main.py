import pytest

from src.main import main, handle_menu


def test_main() -> None:
    with pytest.raises(OSError):
        main()


@pytest.fixture
def mock_main_menu(mocker):
    mock_main_menu = mocker.patch('src.main_menu.MainMenu')
    mock_main_menu.generate = "pusto"
    mock_main_menu.solve = "pusto"
    mock_main_menu.exit = False
    mock_main_menu.options = [
        "Выбрать алгоритм генерации",
        "Выбрать алгоритм решения",
        "Ввести длину и ширину лабиринта",
        "Ввести координаты старта и финиша",
        "Печать",
        "Выход",
    ]
    mock_main_menu.selected_index = 0
    mock_main_menu.exit_menu.return_value = "exit"
    mock_main_menu.handle_key.return_value = "enter"
    return mock_main_menu


@pytest.fixture
def mock_menu_choose(mocker):
    mock_menu_choose = mocker.patch('src.menu_choose.MenuChoose')
    mock_menu_choose.choose_generate.return_value = "gen 1"
    mock_menu_choose.choose_solve.return_value = "solve 1"
    mock_menu_choose.choose_width_and_height.return_value = (10, 14)
    mock_menu_choose.choose_start_and_finish.return_value = ((0, 0), (30, 30))
    return mock_menu_choose


def test_handle_menu_choose_generate(mock_main_menu, mock_menu_choose):
    handle_menu(mock_main_menu, mock_menu_choose)
    assert mock_main_menu.generate == "gen 1"


def test_handle_menu_choose_solve(mock_main_menu, mock_menu_choose):
    mock_main_menu.selected_index = 1
    handle_menu(mock_main_menu, mock_menu_choose)
    assert mock_main_menu.solve == "solve 1"


def test_handle_menu_choose_width_and_height(mock_main_menu, mock_menu_choose):
    mock_main_menu.selected_index = 2
    handle_menu(mock_main_menu, mock_menu_choose)
    assert mock_main_menu.width, mock_main_menu.height == (10, 14)


def test_handle_menu_choose_start_and_finish(mock_main_menu, mock_menu_choose):
    mock_main_menu.selected_index = 3
    handle_menu(mock_main_menu, mock_menu_choose)
    assert mock_main_menu.start, mock_main_menu.finish == ((0, 0), (30, 30))

def test_handle_menu_choose_exit(mock_main_menu, mock_menu_choose):
    mock_main_menu.selected_index = 5
    handle_menu(mock_main_menu, mock_menu_choose)
    assert mock_main_menu.exit_menu() == "exit"
