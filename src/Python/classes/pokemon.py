from classes.item import Item
from classes.ability import Skill
from classes.move import Move
from classes.nature import Nature
from classes.type import PokemonType

class Pokemon:
    def __init__(self, nickname:str, species:str, nature:Nature, base_stats:dict[str, int], types:list[PokemonType],
                 level:int, item:Item, ability:Skill, moveset:list[Move]):
        self.nickname = nickname
        self.species = species
        self.nature = nature
        if len(base_stats) != 6:
            raise ValueError("A Pokémon has 6 base stats (base HP, attack, defense, special attack, special defense and speed).")
        else:
            self.base_stats = base_stats
        self.alteredBaseStats = self.nature.applyNature(self)
        if len(types) not in [1, 2]:    
            raise ValueError("A Pokémon must have between 1 and 2 types.")
        else:
            self.types = types
        self.level = level
        self.item = item
        self.ability = ability
        if len(moveset) not in [1, 2, 3, 4]:
            raise ValueError("A Pokémon must have between 1 and 4 moves.")
        else:
            self.moveset = moveset
        
        self.current_health = self.calculate_health()
        self.stat_changes = {
            'attack': 0,
            'defense': 0,
            'special_attack': 0,
            'special_defense': 0,
            'speed': 0,
            'accuracy': 0,
            'evasion': 0
        }
        pass