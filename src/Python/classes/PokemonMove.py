from PokemonType import PokemonType
from PokemonMoveEffect import PokemonMoveEffect

class PokemonMove:
    def __init__(self, name:str, description:str, type:PokemonType,
                 power:int, accuracy:int, maxPP:int, effect:PokemonMoveEffect=None):
        self.__Name = name
        self.__Description = description
        self.__Type = type
        self.__Power = power
        self.__Accuracy = accuracy
        self.__MaxPP = maxPP
        self.__PP = maxPP
        self.__effect = effect
        pass