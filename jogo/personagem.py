import random
class Character:
    def __init__(self) -> None:
        self.strength = random.randint(0,21) 
        self.dexterity = random.randint(0,21)
        self.constitution = random.randint(0,21)
        self.wisdom = random.randint(0,21)
        self.intelligence = random.randint(0,21)
        self.charisma = random.randint(0,21)

    def strength_definition(self):
        if self.strength == 0:
            pass
        elif self.strength >= 1 and self.strength <= 5:
            pass
        elif self.strength >= 6 and self.strength <= 9:
            pass
        elif self.strength >= 10 and self.strength <= 11:
            pass
        elif self.strength >= 12 and self.strength <= 15:
            pass
        elif self.strength >= 16 and self.strength <= 20:
            pass
        else:
            pass
    
    def dexterity_definition(self):
        if self.dexterity == 0:
            pass
        elif self.dexterity >= 1 and self.dexterity <= 5:
            pass
        elif self.dexterity >= 6 and self.dexterity <= 9:
            pass
        elif self.dexterity >= 10 and self.dexterity <= 11:
            pass
        elif self.dexterity >= 12 and self.dexterity <= 15:
            pass
        elif self.dexterity >= 16 and self.dexterity <= 20:
            pass
        else:
            pass

    def constitution_definition(self):
        if self.constitution == 0:
            pass
        elif self.constitution >= 1 and self.constitution <= 5:
            pass
        elif self.constitution >= 6 and self.constitution <= 9:
            pass
        elif self.constitution >= 10 and self.constitution <= 11:
            pass
        elif self.constitution >= 12 and self.constitution <= 15:
            pass
        elif self.constitution >= 16 and self.constitution <= 20:
            pass
        else:
            pass

    def wisdom_definition(self):
        if self.wisdom == 0:
            pass
        elif self.wisdom >= 1 and self.wisdom <= 5:
            pass
        elif self.wisdom >= 6 and self.wisdom <= 9:
            pass
        elif self.wisdom >= 10 and self.wisdom <= 11:
            pass
        elif self.wisdom >= 12 and self.wisdom <= 15:
            pass
        elif self.wisdom >= 16 and self.wisdom <= 20:
            pass
        else:
            pass

    def intelligence_definition(self):
        if self.intelligence == 0:
            pass
        elif self.intelligence >= 1 and self.intelligence <= 5:
            pass
        elif self.intelligence >= 6 and self.intelligence <= 9:
            pass
        elif self.intelligence >= 10 and self.intelligence <= 11:
            pass
        elif self.intelligence >= 12 and self.intelligence <= 15:
            pass
        elif self.intelligence >= 16 and self.intelligence <= 20:
            pass
        else:
            pass

    def charisma_definition(self):
        if self.charisma == 0:
            pass
        elif self.charisma >= 1 and self.charisma <= 5:
            pass
        elif self.charisma >= 6 and self.charisma <= 9:
            pass
        elif self.charisma >= 10 and self.charisma <= 11:
            pass
        elif self.charisma >= 12 and self.charisma <= 15:
            pass
        elif self.charisma >= 16 and self.charisma <= 20:
            pass
        else:
            pass

    def __str__(self) -> str:
        pass