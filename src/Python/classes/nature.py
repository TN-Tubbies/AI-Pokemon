from enum import Enum
from Stat import Stat

class Nature(Enum):
    Adamant : 0
    Bashful : 1
    Bold : 2
    Brave : 3
    Calm : 4
    Careful : 5
    Docile : 6
    Gentle : 7
    Hardy : 8
    Hasty : 9
    Impish : 10
    Jolly : 11
    Lax : 12
    Lonely : 13
    Mild : 14
    Modest : 15
    Naive : 16
    Naughty : 17
    Quiet : 18
    Quirky : 19
    Rash : 20
    Relaxed : 21
    Sassy : 22
    Serious : 23
    Timid : 24

def get_nature_dict()->dict[Nature, tuple[Stat, Stat]]:
    """
        Returns a dictionary mapping Nature to tuples of stat boosts and stat reductions.
        The first element of the tuple is the nerfed stat, the second is the buffed one.
    """
    return {
        Nature.Adamant : (Stat.SpecialAttack , Stat.Attack),
        Nature.Bashful : (Stat.NULL , Stat.NULL),
        Nature.Bold : (Stat.Attack , Stat.Defense),
        Nature.Brave : (Stat.Speed , Stat.Attack),
        Nature.Calm : (Stat.Attack , Stat.SpecialDefense),
        Nature.Careful : (Stat.SpecialAttack , Stat.SpecialDefense),
        Nature.Docile : (Stat.NULL , Stat.NULL),
        Nature.Gentle : (Stat.Defense , Stat.SpecialDefense),
        Nature.Hardy : (Stat.NULL , Stat.NULL),
        Nature.Hasty : (Stat.Defense , Stat.Speed),
        Nature.Impish : (Stat.SpecialAttack , Stat.Defense),
        Nature.Jolly : (Stat.SpecialAttack , Stat.Speed),
        Nature.Lax : (Stat.SpecialDefense , Stat.Defense),
        Nature.Lonely : (Stat.Defense , Stat.Attack),
        Nature.Mild : (Stat.Defense , Stat.SpecialAttack),
        Nature.Modest : (Stat.Attack , Stat.SpecialAttack),
        Nature.Naive : (Stat.SpecialDefense , Stat.Speed),
        Nature.Naughty : (Stat.SpecialDefense , Stat.Attack),
        Nature.Quiet : (Stat.Speed , Stat.SpecialAttack),
        Nature.Quirky : (Stat.NULL , Stat.NULL),
        Nature.Rash : (Stat.SpecialDefense , Stat.SpecialAttack),
        Nature.Relaxed : (Stat.Speed , Stat.Defense),
        Nature.Sassy : (Stat.Speed , Stat.SpecialDefense),
        Nature.Serious : (Stat.NULL , Stat.NULL),
        Nature.Timid : (Stat.Attack , Stat.Speed)
    }