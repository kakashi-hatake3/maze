from unittest.mock import patch

import pytest

from src.menu import Menu


@pytest.fixture(scope="function")
def menu():
    menu = Menu()
    menu.options = ["1", "2", "3"]
    return menu


def test_exit_menu(menu):
    menu.exit_menu()
    assert menu.exit

@pytest.mark.parametrize("selected_index", [0, 1, 2])
def test_print_menu(capfd, selected_index, menu):
    menu.selected_index = selected_index
    menu.print_menu()
    match selected_index:
        case 0:
            assert "> 1" in capfd.readouterr().out
        case 1:
            assert "> 2" in capfd.readouterr().out
        case 2:
            assert "> 3" in capfd.readouterr().out


@pytest.mark.parametrize("input_value, expected_selected_index, expected_exit, expected_return", [
    ('', 0, False, 'enter'),
    ('w', 2, False, None),
    ('s', 1, False, None),
    ('e', 0, True, None),
])
def test_handle_key(menu, input_value, expected_selected_index, expected_exit, expected_return):

    with patch('builtins.input', return_value=input_value):
        result = menu.handle_key()

    assert menu.selected_index == expected_selected_index
    assert menu.exit == expected_exit
    assert result == expected_return
