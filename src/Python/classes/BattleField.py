from Trainer import Trainer
from Pokemon import Pokemon
from BattleFieldProperties import BattleFieldProperty
from BattleMode import BattleMode
from BattleAction import*

class BattleField:
    def __init__(self, battle_mode:BattleMode=BattleMode.SingleBattle, properties:list[BattleFieldProperty]=[]):
        self.__properties = properties
        self.__battle_mode = battle_mode

        self.__side1:list[Pokemon] = []
        self.__side2:list[Pokemon] = []
        pass

    # Getters
    def __get_side_bound(self):
        if self.__battle_mode == BattleMode.SingleBattle:
            return 1
        elif self.__battle_mode == BattleMode.DoubleBattle:
            return 2
        else:
            return 3
    def get_properties(self):
        return self.__properties.copy()
    def get_property_ids(self):
        return [property.get_id() for property in self.__properties]
    def get_side(self, side_id:int) -> list[Pokemon]:
        if side_id == 1:
            return self.__side1
        elif side_id == 2:
            return self.__side2
        else:
            raise ValueError(f"Invalid side_id: {side_id}")
    def get_side_id_from_pokemon(self, nickname:str) -> int:
        for side_id, side in enumerate([self.__side1, self.__side2], start=1):
            for pokemon in side:
                if pokemon.get_nickname() == nickname:
                    return side_id
        raise ValueError(f"No pokemon with nickname '{nickname}' found.")

    # Setters
    def add_property(self, property: BattleFieldProperty):
        if property not in self.__properties:
            self.__properties.append(property)
        pass
    def remove_property(self, property: BattleFieldProperty):
        if property in self.__properties:
            self.__properties.remove(property)
        pass
    def clean_properties(self):
        self.__properties = []
        pass
    def add_pokemon_to_side(self, side_id:int, pokemon:Pokemon):
        if side_id == 1:
            if len(self.__side1) > self.__get_side_bound():
                raise ValueError("Side 1 is already full.")
            else:
                self.__side1.append(pokemon)
        elif side_id == 2:
            if len(self.__side2) > self.__get_side_bound():
                raise ValueError("Side 2 is already full.")
            else:
                self.__side2.append(pokemon)
        else:
            raise ValueError(f"Invalid side_id: {side_id}")
        pass
    def remove_pokemon_from_side(self, side_id:int, pokemon:Pokemon):
        if side_id == 1:
            if pokemon in self.__side1:
                self.__side1.remove(pokemon)
        elif side_id == 2:
            if pokemon in self.__side2:
                self.__side2.remove(pokemon)
        else:
            raise ValueError(f"Invalid side_id: {side_id}")
        pass

    # ---------------------------------------------------------------------------------------------

    def __run_action(self, trainer:Trainer, action:BattleAction) -> None:
        action_id = action.get_id()
        if action_id == "SwitchPokemon":
            action : SwitchAction = action
            if action.get_switch_in().get_hp > 0 and action.get_switch_out().get_hp() > 0:
                if self.get_side_id_from_pokemon(action.get_switch_in()) == 1:
                    self.__side1.remove(action.get_switch_out())
                    self.__side1.append(action.get_switch_in())
                elif self.get_side_id_from_pokemon(action.get_switch_in()) == 2:
                    self.__side2.remove(action.get_switch_out())
                    self.__side2.append(action.get_switch_in())
                else:
                    raise ValueError(f"Invalid side_id: {self.get_side_id_from_pokemon(action.get_switch_in())}")
            pass
        elif action_id == "UseItem":
            action : UseItemAction = action
            if action.get_item() in trainer.get_items():
                trainer.remove_item(action.get_item())
                action.get_item().use(action.get_target())
            pass
        elif action_id == "PokemonUseMove":
            action : PokemonUseMoveAction = action
            if action.get_move() in action.get_user().get_moveset():
                action.get_move().run_move(action.get_target())
            pass
        else:
            raise ValueError(f"Action unusable: {trainer.get_name()} tried to use {action_id}.")

    def run_actions(self):
        # Getting all actions chosen by in-game trainers (both AI and player), and their priority
        actions = []
        for trainer in self.__side1 + self.__side2:
            actions.append([
                trainer,
                trainer.get_current_action(),
                trainer.get_current_action().get_priority()
            ])

        # Sort the "actions" list by priority (the first element is the last to happen), then reverse
        actions = sorted(actions, key=lambda x: x[2]).reverse()
        
        # Execute the actions
        for action in actions:
            self.__run_action(action[0], action[1])
        pass

    # ---------------------------------------------------------------------------------------------