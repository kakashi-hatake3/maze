import logging
import platform

from src.kruskal_generate import KruskalField
from src.recursive_backtracker_generate import RecursiveBacktrackerField

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info(platform.python_version())

    field = RecursiveBacktrackerField(10, 8)
    field.generate_field()
    print(field)
    print(f"Start: {field.start.index}")
    print(f"Finish: {field.finish.index}")
    f = KruskalField(2, 3)

if __name__ == "__main__":
    main()
