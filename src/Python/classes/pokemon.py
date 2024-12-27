from PokemonSpecies import PokemonSpecies
from PokemonAbility import PokemonAbility
from Nature import Nature
from Item import Item
from PokemonMove import PokemonMove

class Pokemon:
    def __init__(self, species: PokemonSpecies, nickname:str, level:int, MaxHP:int,
                 Atk:int, Def: int, SpA:int, SpD:int, Spe:int,
                 ability:PokemonAbility, nature:Nature, 
                 moveset:list[PokemonMove], item:Item=None):
        self.__Species = species
        self.__Nickname = nickname
        self.__Atk = Atk
        self.__Def = Def
        self.__SpA = SpA
        self.__SpD = SpD
        self.__Spe = Spe
        self.__MaxHP = MaxHP
        self.__HP = MaxHP
        self.__Nature = nature

        if level > 0 and level <= 100:
            self.__Level = level
        else:
            raise ValueError("Level must be between 1 and 100.")
        
        if ability in species.get_abilities():
            self.__Ability = ability
        else:
            raise ValueError("Ability must be a valid ability for the given species.")
        
        checked_moveset = []
        possible_moves = species.get_movepool().keys()
        for move in moveset:
            if move in possible_moves:
                checked_moveset.append(move)
            else:
                raise ValueError(f"Move '{move}' is not valid for the given species.")
        self.__moveset = checked_moveset

        if item is not None:
            if item.get_category() in []: # TODO: add item categories here
                self.__Item = item

        pass

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            species = self.__Species == other.get_species()
            nickname = self.__Nickname == other.get_nickname()
            level = self.__Level == other.get_level()
            atk = self.__Atk == other.get_base_atk()
            df = self.__Def == other.get_base_def()
            spa = self.__SpA == other.get_base_spa()
            spd = self.__SpD == other.get_base_spd()
            spe = self.__Spe == other.get_base_spe()
            ability = self.__Ability == other.get_ability()
            nature = self.__Nature == other.get_nature()
            item = self.__Item == other.get_item()
            return species and nickname and level and ability and nature and item and atk and df and spa and spd and spe
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)
    
    # Getters
    def get_species(self) -> PokemonSpecies:
        return self.__Species
    def get_nickname(self) -> str:
        return self.__Nickname
    def get_level(self) -> int:
        return self.__Level
    def get_max_hp(self) -> int:
        return self.__MaxHP
    def get_hp(self) -> int:
        return self.__HP
    def get_base_atk(self) -> int:
        return self.__Atk
    def get_base_def(self) -> int:
        return self.__Def
    def get_base_spa(self) -> int:
        return self.__SpA
    def get_base_spd(self) -> int:
        return self.__SpD
    def get_base_spe(self) -> int:
        return self.__Spe
    def get_atk(self) -> int:
        return self.__Atk
    def get_def(self) -> int:
        return self.__Def
    def get_spa(self) -> int:
        return self.__SpA
    def get_spd(self) -> int:
        return self.__SpD
    def get_spe(self) -> int:
        return self.__Spe
    def get_acc(self) -> int:
        return 0
    def get_eva(self) -> int:
        return 0
    def get_ability(self) -> PokemonAbility:
        return self.__Ability
    def get_nature(self) -> Nature:
        return self.__Nature
    def get_moveset(self) -> list[PokemonMove]:
        return self.__moveset
    def get_item(self) -> Item:
        return self.__Item
    
    # Setters
    def set_nickname(self, nickname: str):
        self.__Nickname = nickname
        pass
    def set_level(self, level: int):
        if level > 0 and level <= 100:
            self.__Level = level
        else:
            raise ValueError("Level must be between 1 and 100.")
        pass
    def set_max_hp(self, mhp : int):
        self.__MaxHP = mhp
        pass
    def set_hp(self, hp : int):
        self.__HP = hp
        pass
    def set_base_atk(self, atk: int):
        self.__Atk = atk
        pass
    def set_base_def(self, defense: int):
        self.__Def = defense
        pass
    def set_base_spa(self, spa: int):
        self.__SpA = spa
        pass
    def set_base_spd(self, spd: int):
        self.__SpD = spd
        pass
    def set_base_spe(self, spe: int):
        self.__Spe = spe
        pass
    def set_ability(self, ability: PokemonAbility):
        if ability in self.__Species.get_abilities():
            self.__Ability = ability
        else:
            raise ValueError("Ability must be a valid ability for the given species.")
        pass
    def set_nature(self, nature: Nature):
        self.__Nature = nature
        pass
    def set_moveset(self, moveset: list[PokemonMove]):
        checked_moveset = []
        possible_moves = self.__Species.get_movepool().keys()
        for move in moveset:
            if move in possible_moves:
                checked_moveset.append(move)
            else:
                raise ValueError(f"Move '{move}' is not valid for the given species.")
        self.__moveset = checked_moveset
        pass
    def set_item(self, item: Item):
        if item.get_category() in []: # TODO: add item categories here
            self.__Item = item
        else:
            raise ValueError(f"Item '{item}' is not valid for the given species.")
        pass
    
    # ---------------------------------------------------------------------------------------------

