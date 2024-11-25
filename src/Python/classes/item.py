from enum import Enum
from collections.abc import Callable

class ItemType(Enum):
    BERRY = 1    
    USABLE = 2
    CONSOMMABLE = 3
    ON_ATTACKED = 4
    ON_ATTACKING = 5

    MISC = 9999999

class Item:
    def __init__(self, name:str, type:ItemType, use_function:Callable[[], None]):
        self.name = name
        self.type = type
        self.use = use_function
        pass

    def is_usable(self)->bool:
        return self.type == ItemType.USABLE