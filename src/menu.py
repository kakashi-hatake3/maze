import os

from src.enums import MenuKeys


class Menu:
    """
    Родительский класс для всех меню
    :param options: для каждой меню принимает разные значения,
     это кнопки в меню, по которым передвигается пользователь
    :param exit: флаг, проверяющий вышел ли пользователь из меню
    :param selected_index: это индекс определяющий на какой кнопке меню сейчас стрелка
    """

    options: list
    exit = False
    selected_index: int = 0

    def exit_menu(self) -> None:
        self.exit = True

    def print_menu(self) -> None:
        """
        Чистит экран с помощью clear_screen() и рисует кнопки меню из options и стрелку напротив соответствующей кнопки
        :return: None
        """
        os.system("cls")
        print("Выберите опцию:")
        for i, option in enumerate(self.options):
            if i == self.selected_index:
                print(f"> {option}")
            else:
                print(f"  {option}")

    def handle_key(self):
        """
        Обрабатывает ввод пользователя с помощью input.
        :return: 'enter' если была нажата клавиша Enter, иначе None.
        """
        key = (
            input(
                "Введите 'w' для вверх, 's' для вниз, 'Enter' для выбора, 'e' для выхода: "
            )
            .strip()
            .lower()
        )

        match key:
            case MenuKeys.choose.value:
                return MenuKeys.enter.value
            case MenuKeys.up.value:
                self.selected_index = (self.selected_index - 1) % len(self.options)
            case MenuKeys.down.value:
                self.selected_index = (self.selected_index + 1) % len(self.options)
            case MenuKeys.escape.value:
                self.exit = True
        return None
