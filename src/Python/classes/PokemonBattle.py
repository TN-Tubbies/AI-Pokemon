from BattleState import BattleState
from BattleField import BattleField
from Music import Music
from Trainer import Trainer

class PokemonBattle:
    def __init__(self,team1:list[Trainer], team2:list[Trainer], modifiers:dict={}):
        if len(team1) not in [1, 2, 3]:
            raise ValueError("Team 1 must have 1, 2, or 3 Trainers.")
        elif len(team2) not in [1, 2, 3]:
            raise ValueError("Team 2 must have 1, 2, or 3 Trainers.")
        elif team1 == team2:
            raise ValueError("Both teams must be different.")
        else:
            self.__team1 = team1
            self.__team2 = team2
        
        self.__current_state = BattleState.StartState
        self.__current_turn_id = 1

        self.__battlefield = BattleField()
        self.__Music = Music()

        if modifiers != {}:
            for key in modifiers.keys():
                print(key)  # FIXME: add modifiers
        pass

    def run_battle(self) -> int:
        self.__Music.play_battle_theme()
        self.__current_state = BattleState.StartOfTurn

        while self.__current_state != BattleState.EndState and self.__current_state != BattleState.ErrorState:
            for trainer in self.__team1 + self.__team2:
                if trainer.has_lost():
                    self.__team1.remove(trainer)
                    self.__team2.remove(trainer)
                else:
                    for pokemon in trainer.get_team():
                        if pokemon.get_hp() > 0:
                            pokemon.get_ability().run_ability(self.__current_state, self.__battlefield)

            self.__current_state = self.__handle_turn()

            if len(self.__team1) == 0 or len(self.__team2) == 0:
                self.__current_state = BattleState.EndState
            elif self.__current_state == BattleState.EndOfTurn:
                self.__current_turn_id += 1
                self.__current_state = BattleState.StartOfTurn

        self.__Music.stop_battle_theme()
        if self.__current_state == BattleState.ErrorState:
            raise Exception("Battle ended unexpectedly.")

        else:
            has_team1_lost = True
            for trainer in self.__team1:
                if not trainer.pokemon.has_lost():
                    has_team1_lost = False
                    break
            has_team2_lost = True
            for trainer in self.__team2:
                if not trainer.pokemon.has_lost():
                    has_team2_lost = False
                    break
            if has_team1_lost and has_team2_lost:
                return 0
            elif has_team1_lost:
                return 2
            else:
                return 1

    def __handle_turn(self) -> BattleState:
        # TODO: Implement logic for handling turns
        if self.__current_state == BattleState.StartOfTurn:
            for trainer in self.__team1:
                if not trainer.pokemon.has_lost():
                    trainer.choose_action()
            for trainer in self.__team2:
                if not trainer.pokemon.has_lost():
                    trainer.choose_action()
            self.__battlefield.run_actions()
            return BattleState.ActionsDone
        if self.__battlefield == BattleState.ActionsDone:
            return BattleState.EndOfTurn
        return BattleState.ErrorState