class Raca():
    def __init__(self) -> None:
        self.raca_strength = 0
        self.raca_dexterity = 0
        self.raca_constitution = 0
        self.raca_wisdom = 0
        self.raca_intelligence = 0
        self.raca_charisma = 0

    def __str__(self) -> str:
        return f"\n\n\nStatus da Raça :\nForça : {self.raca_strength}\nDestreza : {self.raca_dexterity}\nConstituição : {self.raca_constitution}\nSabedoria : {self.raca_wisdom}\nInteligencia : {self.raca_intelligence}\nCarisma : {self.raca_charisma}\n"

class Raca_Dwarf(Raca):
    def __init__(self) -> None:
        super().__init__()
        self.raca_constitution = 2

class Raca_Hill_Dwarf(Raca_Dwarf):
    def __init__(self) -> None:
        super().__init__()
        self.raca_wisdom = 1

class Raca_Mountain_Dwarf(Raca_Dwarf):
    def __init__(self) -> None:
        super().__init__()
        self.raca_strength = 2

class Raca_Elf(Raca):
    def __init__(self) -> None:
        super().__init__()
        self.raca_dexterity = 2

class Raca_High_Elf(Raca_Elf):
    def __init__(self) -> None:
        super().__init__()
        self.raca_intelligence = 1

class Raca_Wood_Elf(Raca_Elf):
    def __init__(self) -> None:
        super().__init__()
        self.raca_wisdom = 1

class Raca_Dark_Elf(Raca_Elf):
    def __init__(self) -> None:
        super().__init__()
        self.raca_charisma = 1

class Raca_Barbaro(Raca):
    def __init__(self) -> None:
        super().__init__()
        self.raca_dexterity = 2

class Raca_Lightfoot(Raca_Barbaro):
    def __init__(self) -> None:
        super().__init__()
        self.raca_charisma = 1

class Raca_Stout(Raca_Barbaro):
    def __init__(self) -> None:
        super().__init__()
        self.raca_constitution = 1

class Raca_Human(Raca):
    def __init__(self) -> None:
        super().__init__()
        self.raca_strength = 1
        self.raca_dexterity = 1
        self.raca_constitution = 1
        self.raca_wisdom = 1
        self.raca_intelligence = 1
        self.raca_charisma = 1

class Raca_Dragonborn(Raca):
    def __init__(self) -> None:
        super().__init__()
        self.raca_strength = 2
        self.raca_charisma = 1

class Raca_Gnome(Raca):
    def __init__(self) -> None:
        super().__init__()
        self.raca_intelligence = 2

class Raca_Forest_Gnome(Raca_Gnome):
    def __init__(self) -> None:
        super().__init__()
        self.raca_dexterity = 1

class Raca_Rock_Gnome(Raca_Gnome):
    def __init__(self) -> None:
        super().__init__()
        self.raca_constitution = 1

class Raca_Tiefling(Raca):
    def __init__(self) -> None:
        super().__init__()
        self.raca_intelligence = 1
        self.raca_charisma = 2