import random
class Character():
    def __init__(self, nome:str, raca:str) -> None:
        self.nome = nome
        self.raca = raca
        self._strength = random.randint(0,21)
        self._dexterity = random.randint(0,21)
        self._constitution = random.randint(0,21)
        self._wisdom = random.randint(0,21)
        self._intelligence = random.randint(0,21)
        self._charisma = random.randint(0,21)

    def atributos(self):
        if self.raca =="Anão da Colina":
            self._constitution = self._constitution + 2
            self._wisdom = self._wisdom + 1
        elif self.raca =="Anão da Montanha":
            self._constitution = self._constitution + 2
            self._strength = self._strength + 2
        elif self.raca =="Alto Elfo":
            self._dexterity = self._dexterity + 2
            self._intelligence = self._intelligence + 1
        elif self.raca =="Elfo da Floresta":
            self._dexterity = self._dexterity + 2
            self._wisdom = self._wisdom + 1
        elif self.raca =="Elfo Negro 'Drow'":
            self._dexterity = self._dexterity + 2
            self._charisma = self._charisma + 1
        elif self.raca =="Pés Leves":
            self._dexterity = self._dexterity + 2
            self._charisma = self._charisma + 1
        elif self.raca =="Robusto":
            self._dexterity = self._dexterity + 2
            self._constitution = self._constitution + 1
        elif self.raca =="Humano":
            self._strength = self._strength + 1
            self._dexterity = self._dexterity + 1
            self._constitution = self._constitution + 1
            self._wisdom = self._wisdom + 1
            self._intelligence = self._intelligence + 1
            self._charisma = self._charisma + 1
        elif self.raca =="Draconato":
            self._strength = self._strength + 2
            self._charisma = self._charisma + 1
        elif self.raca =="Gnomo da Floresta":
            self._intelligence = self._intelligence + 2
            self._dexterity = self._dexterity + 1
        elif self.raca =="Gnomo da Pedra":
            self._intelligence = self._intelligence + 2
            self._constitution = self._constitution + 1
        else:
            self._intelligence = self._intelligence + 1
            self._charisma = self._charisma + 2

    def strength_definition(self):
        if self._strength == 0:
            self._strength = self._strength,"Incorpóreo"
        elif self._strength >= 1 and self._strength <= 5:
            self._strength = self._strength,"Incapaz"
        elif self._strength >= 6 and self._strength <= 9:
            self._strength = self._strength,"Fraco"
        elif self._strength >= 10 and self._strength <= 11:
            self._strength = self._strength,"Mediano"
        elif self._strength >= 12 and self._strength <= 15:
            self._strength = self._strength,"Forte"
        elif self._strength >= 16 and self._strength <= 20:
            self._strength = self._strength,"Super Poderoso"
        else:
            self._strength = self._strength,"Imbatível"

        return self._strength
    

    def dexterity_definition(self):
        if self._dexterity == 0:
            self._dexterity = self._dexterity,"Desacordado"
        elif self._dexterity >= 1 and self._dexterity <= 5:
            self._dexterity = self._dexterity,"Abatido"
        elif self._dexterity >= 6 and self._dexterity <= 9:
            self._dexterity = self._dexterity,"Desajeitado"
        elif self._dexterity >= 10 and self._dexterity <= 11:
            self._dexterity = self._dexterity,"Regular"
        elif self._dexterity >= 12 and self._dexterity <= 15:
            self._dexterity = self._dexterity,"Ágil"
        elif self._dexterity >= 16 and self._dexterity <= 20:
            self._dexterity = self._dexterity,"Ninja"
        else:
            self._dexterity = self._dexterity,"Imperceptível"
        return self._dexterity
    
    def constitution_definition(self):
        if self._constitution == 0:
            self._constitution = self._constitution,"Espectro"
        elif self._constitution >= 1 and self._constitution <= 5:
            self._constitution = self._constitution,"Enfermo"
        elif self._constitution >= 6 and self._constitution <= 9:
            self._constitution = self._constitution,"Frágil"
        elif self._constitution >= 10 and self._constitution <= 11:
            self._constitution = self._constitution,"Saudável"
        elif self._constitution >= 12 and self._constitution <= 15:
            self._constitution = self._constitution,"Durão"
        elif self._constitution >= 16 and self._constitution <= 20:
            self._constitution = self._constitution,"Super Resisténte"
        else:
            self._constitution = self._constitution,"Imortal"

        return self._constitution
    
    def wisdom_definition(self):
        if self._wisdom == 0:
            self._wisdom = self._wisdom,"Inconsciente"
        elif self._wisdom >= 1 and self._wisdom <= 5:
            self._wisdom = self._wisdom,"Irracional"
        elif self._wisdom >= 6 and self._wisdom <= 9:
            self._wisdom = self._wisdom,"Desatento"
        elif self._wisdom >= 10 and self._wisdom <= 11:
            self._wisdom = self._wisdom,"Simples"
        elif self._wisdom >= 12 and self._wisdom <= 15:
            self._wisdom = self._wisdom,"Perspicaz"
        elif self._wisdom >= 16 and self._wisdom <= 20:
            self._wisdom = self._wisdom,"Filósofo"
        else:
            self._wisdom = self._wisdom,"Iluminado"

        return self._wisdom
    
    def intelligence_definition(self):
        if self._intelligence == 0:
            self._intelligence = self._intelligence,"Inanimado"
        elif self._intelligence >= 1 and self._intelligence <= 5:
            self._intelligence = self._intelligence,"Incivilizado"
        elif self._intelligence >= 6 and self._intelligence <= 9:
            self._intelligence = self._intelligence,"Parvo"
        elif self._intelligence >= 10 and self._intelligence <= 11:
            self._intelligence = self._intelligence,"Medíocre"
        elif self._intelligence >= 12 and self._intelligence <= 15:
            self._intelligence = self._intelligence,"Estudado"
        elif self._intelligence >= 16 and self._intelligence <= 20:
            self._intelligence = self._intelligence,"Gênio"
        else:
            self._intelligence = self._intelligence,"Onisciente"

        return self._intelligence
    
    def charisma_definition(self):
        if self._charisma == 0:
            self._charisma = self._charisma,"Aberração"
        elif self._charisma >= 1 and self._charisma <= 5:
            self._charisma = self._charisma,"Inexpressivo"
        elif self._charisma >= 6 and self._charisma <= 9:
            self._charisma = self._charisma,"Rude"
        elif self._charisma >= 10 and self._charisma <= 11:
            self._charisma = self._charisma,"Sociável"
        elif self._charisma >= 12 and self._charisma <= 15:
            self._charisma = self._charisma,"Persuasivo"
        elif self._charisma >= 16 and self._charisma <= 20:
            self._charisma = self._charisma,"Influente"
        else:
            self._charisma = self._charisma,"Ídolo"

        return self._charisma

    def __str__(self) -> str:
        return f"\n\n\nNome : {self.nome} \nRaça : {self.raca} \nForça : {self._strength}\nDestreza : {self._dexterity}\nConstituição : {self._constitution}\nSabedoria : {self._wisdom}\nInteligencia : {self._intelligence}\nCarisma : {self._charisma}\n"
    