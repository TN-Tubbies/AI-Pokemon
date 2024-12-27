from enum import Enum

class TargetCategory(Enum):
    AllAllies = 0
    AllNearFoes = 1
    AllNearOthers = 2
    BothSides = 3
    FoeSide = 4
    NearAlly = 5
    NearFoe = 6
    NearOther = 7
    None = 8
    Other = 9
    RandomNearFoe = 10
    User = 11
    UserAndAllies = 12
    UserOrNearAlly = 13
    UserSide = 14