from collections.abc import Callable
from enum import Enum

from classes.type import PokemonType

class MoveCategory(Enum):
    PHYSICAL = "Physical"
    SPECIAL = "Special"
    STATUS = "Status"

class TargetCategory(Enum):
    ALL = "All"

class Move:
    def __init__(self, name:str, type:PokemonType, power:int, accuracy:int, category:MoveCategory, PP:int,
                 target:TargetCategory, effect_function:Callable[[], None], priority:int,
                 is_direct:bool, can_be_protected_from:bool, can_be_mirrored:bool):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.category = category
        self.pp = PP
        self.target = target
        self.effect_function = effect_function
        self.priority = priority
        self.is_direct = is_direct
        self.can_be_protected_from = can_be_protected_from
        self.can_be_mirrored = can_be_mirrored
        pass

    def __repr__(self) -> str:
        return f"Move: {self.name}, Type: {self.type}, Power: {self.power}, Accuracy: {self.accuracy}, Category: {self.category}, PP: {self.pp}, Target: {self.target}, Priority: {self.priority}\n"