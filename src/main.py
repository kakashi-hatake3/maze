import logging
import platform

from src.recursive_backtracker import RecursiveBacktrackerField

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info(platform.python_version())

    field = RecursiveBacktrackerField(10, 6)
    field.generate_field()
    print(field)
    print(f"Start: {field.start.index}")
    print(f"Finish: {field.finish.index}")

if __name__ == "__main__":
    main()
