from abc import ABC, abstractmethod

class BattleFieldProperty(ABC):
    def __init__(self, id:str, battlefield):
        self.__id = id
        self.__battlefield = battlefield
        pass

    def get_id(self) -> str:
        return self.__id

    @abstractmethod
    def apply(self):
        pass