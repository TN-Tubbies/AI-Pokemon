from abc import ABC, abstractmethod
from BattleState import BattleState
from BattleField import BattleField

class PokemonAbility(ABC):
    def __init__(self, id:str, owner):
        self.__id = id
        self.__owner = owner
        pass

    @abstractmethod
    def run_ability(self, state:BattleState, battlefield:BattleField) -> None:
        pass