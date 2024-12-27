from PokemonType import PokemonType
from PokemonMoveEffect import PokemonMoveEffect
from TargetCategory import TargetCategory

class PokemonMove:
    def __init__(self, name:str, description:str, type:PokemonType,
                 power:int, accuracy:int, maxPP:int, 
                 targetCategory:TargetCategory, effect:PokemonMoveEffect=None):
        self.__Name = name
        self.__Description = description
        self.__Type = type
        self.__Power = power
        self.__Accuracy = accuracy
        self.__MaxPP = maxPP
        self.__PP = maxPP
        self.__TargetCategory = targetCategory
        self.__effect = effect
        pass

    # Getters
    def getName(self) -> str:
        return self.__Name
    def getDescription(self) -> str:
        return self.__Description
    def getType(self) -> PokemonType:
        return self.__Type
    def getPower(self) -> int:
        return self.__Power
    def getAccuracy(self) -> int:
        return self.__Accuracy
    def getMaxPP(self) -> int:
        return self.__MaxPP
    def getPP(self) -> int:
        return self.__PP
    def getTargetCategory(self) -> TargetCategory:
        return self.__TargetCategory
    def getEffect(self) -> PokemonMoveEffect:
        return self.__effect
    
    # Setters
    def setName(self, name:str):
        self.__Name = name
        pass
    def setDescription(self, description:str):
        self.__Description = description
        pass
    def setType(self, type:PokemonType):
        self.__Type = type
        pass
    def setPower(self, power:int):
        self.__Power = power
        pass
    def setAccuracy(self, accuracy:int):
        self.__Accuracy = accuracy
        pass
    def setMaxPP(self, maxPP:int):
        self.__MaxPP = maxPP
        pass
    def setPP(self, pp:int):
        self.__PP = pp
        if self.__PP < 0:
            self.__PP = 0
        elif self.__PP > self.__MaxPP:
            self.__PP = self.__MaxPP
        pass
    def setTargetCategory(self, targetCategory:TargetCategory):
        self.__TargetCategory = targetCategory
        pass
    def setEffect(self, effect: PokemonMoveEffect):
        self.__effect = effect
        pass

    # ---------------------------------------------------------------------------------------------

    def is_target_valid(self, target:list) -> bool:
        return

    def run_move(self, target:list) -> None:
        if self.is_target_valid(target):

            ran_effect = self.__effect.clone(target)
            ran_effect.run_effect()
            pass
        else:
            raise ValueError("Target-type error: This move can't be run on given target.")