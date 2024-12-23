from PokemonAbility import PokemonAbility
from Nature import Nature
from Item import Item
from PokemonMove import PokemonMove
from PokemonType import PokemonType


class PokemonSpecies:
    def __init__(self, name:str, abilities:list[PokemonAbility],
                 types:list[PokemonType], movepool:dict[PokemonMove]):
        self.__name = name

        if len(abilities) in [1, 2, 3]:
            self.__abilities = abilities
        else:
            raise ValueError("A Pokemon species must have between 1 and 3 abilities!")

        if len(types) == 1:
            self.__types = [types[0], PokemonType.Null]
        elif len(types) == 2:
            self.__types = types
        else:
            raise ValueError("A Pokemon species must have between 1 and 2 types!")

        if len(movepool.keys) > 0:
            self.__movepool = movepool
        else:
            raise ValueError("A Pokemon species must have at least one move!")
        pass

    # Getters
    def get_name(self) -> str:
        return self.__name
    def get_abilities(self) -> list[PokemonAbility]:
        return self.__abilities
    def get_types(self) -> list[PokemonType]:
        return self.__types
    def get_movepool(self) -> dict[PokemonMove]:
        return self.__movepool
    
    # Setters
    def set_name(self, name: str) -> None:
        self.__name = name
    
    def set_abilities(self, abilities: list[PokemonAbility]) -> None:
        if len(abilities) in [1, 2, 3]:
            self.__abilities = abilities
        else:
            raise ValueError("A Pokemon species must have between 1 and 3 abilities!")
    
    def set_types(self, types: list[PokemonType]) -> None:
        if len(types) == 1:
            self.__types = [types[0], PokemonType.Null]
        elif len(types) == 2:
            self.__types = types
        else:
            raise ValueError("A Pokemon species must have between 1 and 2 types!")
    
    def set_movepool(self, movepool: dict[PokemonMove]) -> None:
        if len(movepool) > 0:
            self.__movepool = movepool
        else:
            raise ValueError("A Pokemon species must have at least one move!")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            name = self.__name == other.get_name()
            abilities = self.__abilities == other.get_abilities()
            types = self.__types == other.get_types()
            movepool = self.__movepool == other.get_movepool()
            return name and abilities and types and movepool
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)
    
    # Getters
    def get_name(self):
        return self.__name
    def get_abilities(self):
        return self.__abilities
    def get_types(self):
        return self.__types
    def get_movepool(self):
        return self.__movepool
    
    # Setters