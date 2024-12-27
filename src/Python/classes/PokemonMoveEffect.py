from abc import ABC, abstractmethod
from TargetCategory import TargetCategory

class PokemonMoveEffect(ABC):
    def __init__(self, id:str, targetCategory:TargetCategory):
        self.__id = id
        self.__targetCategory = targetCategory
        pass

    # Getters
    def get_id(self) -> str:
        return self.__id
    def get_target_category(self) -> TargetCategory:
        return self.__targetCategory
    
    # Setters
    def set_id(self, id:str):
        self.__id = id
        pass
    def set_target_category(self, targetCategory:TargetCategory):
        self.__targetCategory = targetCategory
        pass

    # ---------------------------------------------------------------------------------------------

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def run_effect(self) -> None:
        pass