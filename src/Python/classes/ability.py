from collections.abc import Callable

from classes.battle import Battle

class Skill:
    def __init__(self, name:str, check_function:Callable[[Battle],bool], run_function:Callable[[Battle],None]):
        self.name = name
        self.check = check_function
        self.run = run_function
        pass