import builtins
from unittest import mock

import pytest

from src.menu_choose import MenuChoose


@pytest.fixture(scope="module")
def menu_choose():
    return MenuChoose()


def test_choose_generate(menu_choose):
    with pytest.raises(OSError):
        assert menu_choose.choose_generate() in ["Growing Tree", "Recursive Backtracker"]


def test_choose_solve(menu_choose):
    with pytest.raises(OSError):
        assert menu_choose.choose_solve() in ["Dijkstra", "Wave Front"]


def test_choose_width_and_height_positive(menu_choose):
    with mock.patch.object(builtins, 'input', lambda _: 5):
        assert menu_choose.choose_width_and_height() == (5, 5)


def test_choose_start_and_finish_positive(menu_choose):
    with mock.patch.object(builtins, 'input', lambda _: 0):
        assert menu_choose.choose_start_and_finish() == ((0, 0), (0, 0))
