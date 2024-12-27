from abc import ABC, abstractmethod
from Pokemon import Pokemon
from PokemonMove import PokemonMove
from Item import Item

class BattleAction(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_id(self) -> str:
        return ""
    
    @abstractmethod
    def get_priority(self) -> int:
        return 0

# -------------------------------------------------------------------------------------------------

class SwitchAction(BattleAction):
    def __init__(self, sw_in:Pokemon, sw_out:Pokemon):
        self.__switch_in = sw_in
        self.__switch_out = sw_out
        pass

    def get_id(self) -> str:
        return "SwitchPokemon"
    def get_priority(self) -> int:
        return 8
    def get_switch_in(self) -> Pokemon:
        return self.__switch_in
    def get_switch_out(self) -> Pokemon:
        return self.__switch_out

class UseItemAction(BattleAction):
    def __init__(self, target: Pokemon, item: Item):
        self.__target = target
        self.__item = item
        pass
    
    def get_id(self) -> str:
        return "UseItem"
    def get_priority(self) -> int:
        return 7
    def get_target(self) -> Pokemon:
        return self.__target
    def get_item(self) -> Item:
        return self.__item

class PokemonUseMoveAction(BattleAction):
    def __init__(self, user: Pokemon, target: list[Pokemon], move: PokemonMove):
        self.__user = user
        self.__target = target
        self.__move = move
        pass
    
    def get_id(self) -> str:
        return "PokemonUseMove"
    def get_priority(self) -> int:
        return self.__move.getPriority()
    def get_user(self) -> Pokemon:
        return self.__user
    def get_target(self) -> list[Pokemon]:
        return self.__target
    def get_move(self) -> PokemonMove:
        return self.__move

# -------------------------------------------------------------------------------------------------