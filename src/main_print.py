from src.dijkstra_solve import DijkstraSolver
from src.growing_tree_generate import GrowingTreeField
from src.main_menu import MainMenu
from src.recursive_backtracker_generate import RecursiveBacktrackerField
from src.wave_front_solve import WaveFrontSolver


class MainPrint:
    def __init__(self, menu: MainMenu):
        self.menu = menu

    def generate_field(self):
        match self.menu.generate:
            case "Growing Tree":
                self.menu.field = GrowingTreeField(
                    self.menu.width,
                    self.menu.height,
                    self.menu.start,
                    self.menu.finish
                )
            case "Recursive Backtracker":
                self.menu.field = RecursiveBacktrackerField(
                    self.menu.width,
                    self.menu.height,
                    self.menu.start,
                    self.menu.finish
                )
        self.menu.field.generate_field()
        return self.print_field()

    def solve_field(self):
        solver = None
        match self.menu.solve:
            case "Dijkstra":
                solver = DijkstraSolver(self.menu.field)
            case "Wave Front":
                solver = WaveFrontSolver(self.menu.field)
        count_of_steps = solver.solve_field()
        if count_of_steps != float('inf'):
            return 'Длина пути: ' + str(count_of_steps)
        else:
            return 'Путь не существует'
    
    def print_field(self):
       return self.menu.field
