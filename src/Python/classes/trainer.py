from classes.pokemon import Pokemon
from classes.item import Item

class Trainer:
    def __init__(self, name:str, pokemons:list[Pokemon], usable_items:list[Item]) -> None:
        self.name = name
        self.pokemons = pokemons
        self.usable_items = usable_items
        pass