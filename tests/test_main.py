import pytest

from src.main import main


def test_main() -> None:
    with pytest.raises(OSError):
        main()
