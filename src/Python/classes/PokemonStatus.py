from abc import abstractmethod
from typing import override
from Pokemon import Pokemon
from PokemonMove import PokemonMove

class PokemonStatus(Pokemon):
    def __init__(self, pokemon:Pokemon, status_name:str, duration:int, probability:float):
        super().__init__(pokemon)
        self.__status_name = status_name
        self.__status_duration = duration
        self.__status_trigger_probability = probability
        pass

    # Getters
    def get_status_name(self) -> str:
        return self.__status_name
    def get_status_duration(self) -> int:
        return self.__status_duration
    def get_status_probability(self) -> float:
        return self.__status_trigger_probability
    
    # Setters
    def set_status_duration(self, duration: int) -> None:
        self.__status_duration = duration
    def set_status_probability(self, probability: float) -> None:
        self.__status_trigger_probability = probability
    
    # ---------------------------------------------------------------------------------------------

    @override
    def has_status(self) -> bool:
        return True

    def manage_status(self) -> None:
        # TODO: write this function

        pass

    def cure_status(self) -> None:
        # TODO: write this function

        pass

    @override
    @abstractmethod
    def run_move(self, move:PokemonMove) -> None:
        pass
    
    @abstractmethod
    def trigger_status(self) -> None:
        pass

# -------------------------------------------------------------------------------------------------
# TODO: implement all statuses