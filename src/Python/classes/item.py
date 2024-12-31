from abc import ABC, abstractmethod
from PokemonType import PokemonType
from TargetCategory import TargetCategory
from PokemonMove import PokemonMove, TemporaryChangedMove

class Item(ABC):
    def __init__(self, name:str, description:str):
        self._name = name
        self._description = description
        pass
    def __eq__(self, other):
        return isinstance(other, Item) and self.get_name() == other.get_name() and self.get_category() == other.get_category()
    def __ne__(self, other):
        return not self.__eq__(other)

    def get_name(self) -> str:
        return self._name
    def get_description(self) -> str:
        return self._description
    @abstractmethod
    def get_category(self) -> str:
        return "Unknown"
    @abstractmethod
    def use_by_trainer(self, target) -> None:
        pass
    @abstractmethod
    def use_when_held(self, holder, move:PokemonMove) -> None:
        pass

# -------------------------------------------------------------------------------------------------
# BERRIES -----------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

class Berry(Item):
    def __init__(self, berry_name: str, description: str):
        super().__init__(f"{berry_name} Berry", description)
        pass
    def get_category(self) -> str:
        return "Berry"

    @abstractmethod
    def use_by_trainer(self, target) -> None:
        pass
    @abstractmethod
    def use_when_held(self, holder, move:PokemonMove) -> None:
        pass
class BabiriBerry(Berry):
    def __init__(self):
        super().__init__("Babiri", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Steel-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_STEEL:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class ChartiBerry(Berry):
    def __init__(self):
        super().__init__("Charti", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Rock-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_ROCK:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class ChestoBerry(Berry):
    def __init__(self):
        super().__init__("Chesto", "A Berry to be consumed by Pokémon. If a Pokémon holds one, it can recover from sleep on its own in battle.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if holder.has_status():
            if holder.get_status_name() == "Asleep":
                holder.cure_status()
                holder.set_item(None)
        pass
class ChilanBerry(Berry):
    def __init__(self):
        super().__init__("Chilan", "If held by a Pokémon, this Berry will lessen the damage taken from one Normal-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_NORMAL:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class ChopleBerry(Berry):
    def __init__(self):
        super().__init__("Chople", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Fighting-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_FIGHTING:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class CobaBerry(Berry):
    def __init__(self):
        super().__init__("Coba", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Flying-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_FLYING:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class ColburBerry(Berry):
    def __init__(self):
        super().__init__("Colbur", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Dark-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_DARK:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class HabanBerry(Berry):
    def __init__(self):
        super().__init__("Haban", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Dragon-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_DRAGON:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class KasibBerry(Berry):
    def __init__(self):
        super().__init__("Kasib", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Ghost-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_GHOST:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class KebiaBerry(Berry):
    def __init__(self):
        super().__init__("Kebia", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Poison-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_POISON:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class OccaBerry(Berry):
    def __init__(self):
        super().__init__("Occa", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Fire-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_FIRE:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class OranBerry(Berry):
    def __init__(self):
        super().__init__("Oran", "A Berry to be consumed by Pokémon. If a Pokémon holds one, it can restore its own HP by 10 points during battle.")
        pass
    
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_hp() + 10)
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if holder.get_hp() <= holder.get_max_hp() // 2:
            holder.set_hp(holder.get_hp() + 10)
            holder.set_item(None)
        pass
class PasshoBerry(Berry):
    def __init__(self):
        super().__init__("Passho", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Water-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_WATER:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class PayapaBerry(Berry):
    def __init__(self):
        super().__init__("Payapa", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Psychic-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_PSYCHIC:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class RindoBerry(Berry):
    def __init__(self):
        super().__init__("Rindo", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Grass-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_PSYCHIC:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class RoseliBerry(Berry):
    def __init__(self):
        super().__init__("Roseli", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Fairy-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_FAIRY:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class ShucaBerry(Berry):
    def __init__(self):
        super().__init__("Shuca", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Ground-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_FAIRY:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class SitrusBerry(Berry):
    def __init__(self):
        super().__init__("Sitrus", "A Berry to be consumed by Pokémon. If a Pokémon holds one, it can restore its own HP by a small amount during battle.")
        pass
    
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_hp() + target.get_max_hp() // 4)
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if holder.get_hp() <= holder.get_max_hp() // 2:
            holder.set_hp(holder.get_hp() + holder.get_max_hp() // 4)
            holder.set_item(None)
        pass
class TangaBerry(Berry):
    def __init__(self):
        super().__init__("Tanga", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Bug-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_BUG:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class WacanBerry(Berry):
    def __init__(self):
        super().__init__("Wacan", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Electric-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_ELECTRIC:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass
class YacheBerry(Berry):
    def __init__(self):
        super().__init__("Yache", "If held by a Pokémon, this Berry will lessen the damage taken from one supereffective Ice-type attack.")
        pass
    
    def use_by_trainer(self, target) -> None:
        # No effect
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        if move is not None:
            if move.getType() == PokemonType.Type_ICE:
                move = TemporaryChangedMove(move, 1, {"Power" : 0.5})
                holder.set_item(None)
        pass

# -------------------------------------------------------------------------------------------------
# MEDICINE ----------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

class Medicine(Item):
    def __init__(self, name:str, description:str):
        super().__init__(name, description)
        pass
    def get_category(self):
        return "Medicine"

    @abstractmethod
    def use_by_trainer(self, target) -> None:
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        # Can't be used when held
        pass
class Antidote(Medicine):
    def __init__(self):
        super().__init__("Antidote", "A spray-type medicine for treating poisoning. It can be used to lift the effects of being poisoned from a single Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        if target.has_status():
            if target.get_status_name() == "Poisoned":
                target.cure_status()
        pass
class BurnHeal(Medicine):
    def __init__(self):
        super().__init__("Burn Heal", "A spray-type medicine for treating burns. It can be used to heal a single Pokémon suffering from a burn.")
        pass
    def use_by_trainer(self, target) -> None:
        if target.has_status():
            if target.get_status_name() == "Burnt":
                target.cure_status()
        pass
class Elixir(Medicine):
    def __init__(self):
        super().__init__("Elixir", "This medicine can be used to restore 10 PP to each of the moves that have been learned by a Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        for move in target.get_moveset():
            move.set_pp(move.get_pp() + 10)
        pass
class EnergyPowder(Medicine):
    def __init__(self):
        super().__init__("Energy Powder", "A very bitter medicinal powder. It can be used to restore 60 HP to a single Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_hp() + 60)
        pass
class EnergyRoot(Medicine):
    def __init__(self):
        super().__init__("Energy Root", "An extremely bitter medicinal root. It can be used to restore 120 HP to a single Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_hp() + 120)
        pass
class Ether(Medicine):
    def __init__(self, move_id:int):
        super().__init__("Ether", "This medicine can be used to restore 10 PP to a single selected move that has been learned by a Pokémon.")
        self.__move_id = move_id
        pass
    def use_by_trainer(self, target) -> None:
        target.get_moveset()[self.__move_id].setPP(target.get_moveset()[self.__move_id].getPP() + 10)
        pass
class FreshWater(Medicine):
    def __init__(self):
        super().__init__("Fresh Water", "Water with high mineral content. It can be used to restore 30 HP to a single Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_hp() + 30)
        pass
class FullHeal(Medicine):
    def __init__(self):
        super().__init__("Full Heal", "A spray-type medicine that is broadly effective. It can be used to heal all the status conditions of a single Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        if target.has_status():
            target.cure_status()
        pass
class FullRestore(Medicine):
    def __init__(self):
        super().__init__("Full Restore", "A medicine that can be used to fully restore the HP of a single Pokémon and heal any status conditions it has.")
        pass
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_max_hp())
        if target.has_status():
            target.cure_status()
        pass
class HealPowder(Medicine):
    def __init__(self):
        super().__init__("Energy Root", "A very bitter medicinal powder. It can be used once to heal all the status conditions of a Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        if target.has_status():
            target.cure_status()
        pass
class HyperPotion(Medicine):
    def __init__(self):
        super().__init__("Hyper Potion", "A spray-type medicine for treating wounds. It can be used to restore 120 HP to a single Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_hp() + 120)
        pass
class IceHeal(Medicine):
    def __init__(self):
        super().__init__("Ice Heal", "A spray-type medicine for treating freezing. It can be used to thaw out a single Pokémon that has been frozen solid.")
        pass
    def use_by_trainer(self, target) -> None:
        if target.has_status():
            if target.get_status_name() == "Frozen":
                target.cure_status()
        pass
class Lemonade(Medicine):
    def __init__(self):
        super().__init__("Lemonade", "A very sweet and refreshing drink. It can be used to restore 70 HP to a single Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_hp() + 70)
        pass
class MaxElixir(Medicine):
    def __init__(self):
        super().__init__("Max Elixir", "This medicine can be used to fully restore the PP of all of the moves that have been learned by a Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        for move in target.get_moveset():
            move.set_pp(move.get_max_pp())
        pass
class MaxEther(Medicine):
    def __init__(self, move_id:int):
        super().__init__("Max Ether", "This medicine can be used to fully restore the PP of a single selected move that has been learned by a Pokémon.")
        self.__move_id = move_id
        pass
    def use_by_trainer(self, target) -> None:
        target.get_moveset()[self.__move_id].setPP(target.get_moveset()[self.__move_id].getMaxPP())
        pass
class MaxPotion(Medicine):
    def __init__(self):
        super().__init__("Max Potion", "A spray-type medicine for treating wounds. It can be used to completely restore the max HP of a single Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_max_hp())
        pass
class MoomooMilk(Medicine):
    def __init__(self):
        super().__init__("Moomoo Milk", "A bottle of highly nutritious milk. It can be used to restore 100 HP to a single Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_hp() + 100)
        pass
class ParalyzeHeal(Medicine):
    def __init__(self):
        super().__init__("Paralyze Heal", "A spray-type medicine for treating paralysis. It can be used to free a single Pokémon that has been paralyzed.")
        pass
    def use_by_trainer(self, target) -> None:
        if target.has_status():
            if target.get_status_name() == "Paralyzed":
                target.cure_status()
        pass
class Potion(Medicine):
    def __init__(self):
        super().__init__("Potion", "A spray-type medicine for treating wounds. It can be used to restore 20 HP to a single Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_hp() + 20)
        pass
class SodaPop(Medicine):
    def __init__(self):
        super().__init__("Soda Pop", "A highly carbonated soda drink. It can be used to restore 50 HP to a single Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_hp() + 50)
        pass
class SuperPotion(Medicine):
    def __init__(self):
        super().__init__("Super Potion", "A spray-type medicine for treating wounds. It can be used to restore 60 HP to a single Pokémon.")
        pass
    def use_by_trainer(self, target) -> None:
        target.set_hp(target.get_hp() + 60)
        pass

# -------------------------------------------------------------------------------------------------
# EVOLUTION ITEM ----------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

class EvolutionItem(Item):
    def __init__(self, name:str, description:str):
        super().__init__(name, description)
        pass
    def get_category(self):
        return "Evolution Item"

    def use_by_trainer(self, target) -> None:
        # Can't be used by trainer
        pass
    @abstractmethod
    def use_when_held(self, holder, move:PokemonMove) -> None:
        pass

# -------------------------------------------------------------------------------------------------
# BOOSTING ITEM -----------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

class BoostingItem(Item):
    def __init__(self, name:str, description:str):
        super().__init__(name, description)
        pass
    def get_category(self):
        return "Boosting Item"

    @abstractmethod
    def use_by_trainer(self, target) -> None:
        pass
    @abstractmethod
    def use_when_held(self, holder, move:PokemonMove) -> None:
        pass

# -------------------------------------------------------------------------------------------------
# FIGHTING ITEM -----------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

class FightingItem(Item):
    def __init__(self, name:str, description:str):
        super().__init__(name, description)
        pass
    def get_category(self):
        return "Fighting Item"

    @abstractmethod
    def use_by_trainer(self, target) -> None:
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        # Can't be used while held
        pass

# -------------------------------------------------------------------------------------------------
# Z-CRYSTALS --------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

class ZCrystal(Item):
    def __init__(self, name:str, description:str, move:PokemonMove, type:PokemonType, restrictions:dict={}):
        super().__init__(name, description)
        self.__move = move
        self.__type = type
        self.__restrictions = restrictions
        self.__has_been_used = False
        pass
    def get_category(self) -> str:
        return "Z-Crystal"
    def get_move(self) -> PokemonMove:
        return self.__move
    def get_type(self) -> PokemonType:
        return self.__type
    def get_restrictions(self) -> dict:
        return self.__restrictions
    def can_be_used(self) -> bool:
        return not self.__has_been_used

    def use_by_trainer(self, target) -> None:
        # Can't be used by trainer
        pass
    def use_when_held(self, holder, move:PokemonMove) -> None:
        for m in holder.get_moveset():
            if m.get_type() == PokemonType.Type_BUG:
                self.__has_been_used = True
                m.upgrade_to_z_move(self)
        pass
    def un_use_when_held(self, holder, move:PokemonMove) -> None:
        for m in holder.get_moveset():
            if m.get_type() == PokemonType.Type_BUG:
                self.__has_been_used = False
                m.downgrade_from_z_move(self)
        pass
class BuginiumZ(ZCrystal):
    def __init__(self):
        move = PokemonMove(
            "Savage Spin-Out", "The user binds the target with full force with threads of silk that the user spits using its Z-Power. The power varies, depending on the original move.",
            type=PokemonType.Type_BUG,
            category=TargetCategory.NearOther,
            power=-1,
            accuracy=100
        )
        super().__init__(
            "Buginium Z", "This is a crystallized form of Z-Power. It upgrades Bug-type moves to Z-Moves.", 
            move,
            PokemonType.Type_BUG,
            {}
        )
        pass
class DarkiniumZ(ZCrystal):
    def __init__(self):
        move = PokemonMove(
            "Black Hole Eclipse", "The user gathers dark energy using its Z-Power and sucks the target into it. The power varies, depending on the original move.",
            type=PokemonType.Type_DARK,
            category=TargetCategory.NearOther,
            power=-1,
            accuracy=100
        )
        super().__init__(
            "Darkinium Z", "This is a crystallized form of Z-Power. It upgrades Dark-type moves to Z-Moves.", 
            move,
            PokemonType.Type_DARK,
            {}
        )
        pass
class DragoniumZ(ZCrystal):
    def __init__(self):
        move = PokemonMove(
            "Devastating Drake", "The user materializes its aura using its Z-Power and attacks the target with full force. The power varies, depending on the original move.",
            type=PokemonType.Type_DRAGON,
            category=TargetCategory.NearOther,
            power=-1,
            accuracy=100
        )
        super().__init__(
            "Dragonium Z", "This is a crystallized form of Z-Power. It upgrades Dragon-type moves to Z-Moves.", 
            move,
            PokemonType.Type_DRAGON,
            {}
        )
        pass
class ElectriumZ(ZCrystal):
    def __init__(self):
        move = PokemonMove(
            "Gigavolt Havoc", "The user hits the target with a powerful electric current collected by its Z-Power. The power varies, depending on the original move.",
            type=PokemonType.Type_ELECTRIC,
            category=TargetCategory.NearOther,
            power=-1,
            accuracy=100
        )
        super().__init__(
            "Electrium Z", "This is a crystallized form of Z-Power. It upgrades Electric-type moves to Z-Moves.", 
            move,
            PokemonType.Type_ELECTRIC,
            {}
        )
        pass
#TODO: add the other Z-Crystals

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------