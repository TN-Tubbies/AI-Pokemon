from classes.pokemon import Pokemon

class Nature:
    def __init__(self, name:str, buffedStat:str, nerfedStat:str):
        """A Nature boosts a statistic and nerfs another.
        Note: some Natures have no effect.

        Args:
            name (str): Nature's (french) name.
            buffedStat (str): Stat the Nature buffs.
            nerfedStat (str): Stat the Nature nerfs.
        """
        self.name = name
        self.buffedStat = buffedStat
        self.nerfedStat = nerfedStat
        pass

    def applyNature(self, pokemon:Pokemon)->dict[str,int]:
        res = {
            "Attaque" : pokemon.base_stats["Attaque"],
            "Défense" : pokemon.base_stats["Défense"],
            "Attaque Spéciale" : pokemon.base_stats["Attaque Spéciale"],
            "Défense Spéciale" : pokemon.base_stats["Défense Spéciale"],
            "Vitesse" : pokemon.base_stats["Vitesse"]
        }
        if self.buffedStat!= "" and self.nerfedStat!= "":
            res[self.buffedStat] *= 1.10
            res[self.nerfedStat] *= 0.90
        return res

def GetAllNatures(onlyEffectiveOnes:bool=False)->list[Nature]:
    if onlyEffectiveOnes:
        return [
            Nature("Assuré","Défense","Attaque"),
            Nature("Brave","Attaque","Vitesse"),
            Nature("Calme","Défense Spéciale","Attaque"),
            Nature("Discret","Attaque Spéciale","Vitesse"),
            Nature("Doux","Attaque Spéciale","Défense"),
            Nature("Foufou","Attaque Spéciale","Défense Spéciale"),
            Nature("Gentil","Défense","Défense Spéciale"),
            Nature("Jovial","Vitesse","Attaque Spéciale"),
            Nature("Lâche","Défense","Défense Spéciale"),
            Nature("Malin","Défense","Attaque Spéciale"),
            Nature("Malpoli","Défense Spéciale","Vitesse"),
            Nature("Mauvais","Attaque","Défense Spéciale"),
            Nature("Modeste","Attaque Spéciale","Attaque"),
            Nature("Naïf","Vitesse","Défense Spéciale"),
            Nature("Pressé","Vitesse","Défense"),
            Nature("Prudent","Défense Spéciale","Attaque Spéciale"),
            Nature("Relax","Défense","Vitesse"),
            Nature("Rigide","Attaque","Attaque Spéciale"),
            Nature("Solo","Attaque","Défense"),
            Nature("Timide","Vitesse","Attaque")
        ]
    else:
        return [
            Nature("Assuré","Défense","Attaque"),
            Nature("Bizarre","",""),
            Nature("Brave","Attaque","Vitesse"),
            Nature("Calme","Défense Spéciale","Attaque"),
            Nature("Discret","Attaque Spéciale","Vitesse"),
            Nature("Docile","",""),
            Nature("Doux","Attaque Spéciale","Défense"),
            Nature("Foufou","Attaque Spéciale","Défense Spéciale"),
            Nature("Gentil","Défense","Défense Spéciale"),
            Nature("Hardi","",""),
            Nature("Jovial","Vitesse","Attaque Spéciale"),
            Nature("Lâche","Défense","Défense Spéciale"),
            Nature("Malin","Défense","Attaque Spéciale"),
            Nature("Malpoli","Défense Spéciale","Vitesse"),
            Nature("Mauvais","Attaque","Défense Spéciale"),
            Nature("Modeste","Attaque Spéciale","Attaque"),
            Nature("Naïf","Vitesse","Défense Spéciale"),
            Nature("Pressé","Vitesse","Défense"),
            Nature("Prudent","Défense Spéciale","Attaque Spéciale"),
            Nature("Pudique","",""),
            Nature("Relax","Défense","Vitesse"),
            Nature("Rigide","Attaque","Attaque Spéciale"),
            Nature("Sérieux","",""),
            Nature("Solo","Attaque","Défense"),
            Nature("Timide","Vitesse","Attaque")
        ]