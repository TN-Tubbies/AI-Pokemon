from Pokemon import Pokemon
from Item import Item

class Trainer:
    def __init__(self, name:str, team:list[Pokemon], items:list[Item]=[]):
        self.__name = name

        if len(team) == 0 or len(team) > 6:
            raise ValueError("Team must contain between 1 and 6 Pokemons")
        else:
            self.__team = team

        self.__items = items

        pass

    def __eq__(self, other)->bool:
        if isinstance(other, Trainer):
            return self.__name == other.__name and self.__team == other.__team and self.__items == other.__items
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    
    # Getters
    def get_name(self)->str:
        return self.__name
    
    def get_team(self)->list[Pokemon]:
        return self.__team
    
    def get_items(self)->list[Item]:
        return self.__items
    
    # ---------------------------------------------------------------------------------------------

    def use_item(self, item:Item, target:Pokemon):
        if item in self.__items:
            self.__items.remove(item)
            item.use(target)
            pass
        else:
            raise ValueError("Item %s not found!" % item)
            pass
    
    def has_lost(self) -> bool:
        return all(pokemon.get_hp() == 0 for pokemon in self.__team)
    
    def choose_action(self) -> None:
        # TODO: Implement this method
        pass