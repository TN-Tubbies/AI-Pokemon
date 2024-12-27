from enum import Enum

class BattleState(Enum):
    ErrorState = 0
    StartState = 1
    EndState = 2
    StartOfTurn = 3
    ActionsDone = 4
    EndOfTurn = 10