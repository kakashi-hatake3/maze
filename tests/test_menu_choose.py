import builtins
from unittest import mock

import pytest

from src.menu_choose import MenuChoose


# class MockBoolCheck:
#     def __init__(self, fail_after=0):
#         self.count = 0
#         self.fail_after = fail_after
#
#     def __call__(self):
#         called = self.count
#         self.count += 1
#         return called <= self.fail_after


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

# def test_choose_width_and_height_negative_1(capfd, menu_choose):
#     menu_choose.choose_width_and_height = MockBoolCheck()
#     with mock.patch.object(builtins, 'input', lambda _: 'asd'):
#         with pytest.raises(ValueError):
#             assert menu_choose.choose_width_and_height() is True
#             # assert capfd.readouterr().out == "Некорректные данные"
#             # assert True
#         # assert menu_choose.choose_width_and_height() == (5, 5)

def test_choose_start_and_finish_positive(menu_choose):
    with mock.patch.object(builtins, 'input', lambda _: 0):
        assert menu_choose.choose_start_and_finish() == ((0, 0), (0, 0))
