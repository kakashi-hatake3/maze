import pytest

from src.field import Field


@pytest.mark.parametrize(
    "w, h, s_c, f_c, exp",
    [
        (5, 5, (0, 0), (6, 1), "Неверные координаты старта или финиша"),
        (5, 5, (0, 0), (2, 2), "Старт и финиш должны быть внешними"),
        (1, 1, (0, 0), (0, 0), "Минимум может быть 2 ячейки"),
    ],
)
def test_field_init(capfd, w, h, s_c, f_c, exp):
    with pytest.raises(SystemExit):
        Field(w, h, s_c, f_c)
        assert capfd.readouterr().out == exp
