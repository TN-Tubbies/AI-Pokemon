from typing import override
from PokemonType import PokemonType
from PokemonMoveEffect import PokemonMoveEffect
from TargetCategory import TargetCategory

class PokemonMove:
    def __init__(self, name:str, description:str, type:PokemonType,
                 power:int, accuracy:int, maxPP:int, priority:int,
                 targetCategory:TargetCategory, effect:PokemonMoveEffect=None, PP:int=None):
        self.__Name = name
        self.__Description = description
        self.__Type = type
        self.__Power = power
        self.__Accuracy = accuracy
        self.__MaxPP = maxPP
        self.__Priority = priority
        self.__TargetCategory = targetCategory
        self.__effect = effect

        if PP is not None:
            self.__PP = PP
        else:
            self.__PP = maxPP
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
    def getPriority(self) -> int:
        return self.__Priority
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
    def setPriority(self, priority:int):
        if priority < -6 or priority > 6:
            raise ValueError("Priority out of range: -6 <= priority <= 6.")
        else:
            self.__Priority = priority
        pass
    def setTargetCategory(self, targetCategory:TargetCategory):
        self.__TargetCategory = targetCategory
        pass
    def setEffect(self, effect: PokemonMoveEffect):
        self.__effect = effect
        pass

    # ---------------------------------------------------------------------------------------------

    def is_temporary(self) -> bool:
        return False

    def is_target_valid(self, target:list) -> bool:
        # TODO: write this function
        return

    def run_move(self, target:list) -> None:
        if self.is_target_valid(target):
            # TODO: finish this function
            ran_effect = self.__effect.clone(target)
            ran_effect.run_effect()
            pass
        else:
            raise ValueError("Target-type error: This move can't be run on given target.")

    def upgrade_to_z_move(self, z_crystal) -> None:
        # TODO: write this function
        pass
    def downgrade_from_z_move(self, z_crystal) -> None:
        # TODO: write this function
        pass

# -------------------------------------------------------------------------------------------------

class TemporaryChangedMove(PokemonMove):
    def __init__(self, move:PokemonMove, turn:int, changes:dict[str]):
        super().__init__(move.getName(), move.getDescription(), move.getType(),
                         move.getPower(), move.getAccuracy(), move.getMaxPP(),
                         move.getPriority(), move.getTargetCategory(), move.getEffect())
        self.__lastingTurn = turn

        # Apply changes to the move
        for change in changes.keys():
            if change == "Power":
                self.setPower(self.getPower() * changes[change])

        pass

    # Getters
    def getLastingTurn(self) -> int:
        return self.__lastingTurn
    
    # Setters
    def setLastingTurn(self, turn: int):
        if turn < 1:
            raise ValueError("Invalid turn number: turn must be at least 1.")
        else:
            self.__lastingTurn = turn
        pass
    
    # ---------------------------------------------------------------------------------------------

    @override
    def is_temporary(self) -> bool:
        return True

    def manage_expiration(self) -> None:
        self.__lastingTurn -= 1
        if self.__lastingTurn <= 0:
            self = PokemonMove(self.getName(), self.getDescription(), self.getType(),
                         self.getPower(), self.getAccuracy(), self.getMaxPP(),
                         self.getPriority(), self.getTargetCategory(), self.getEffect(), self.getPP())
        pass

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------