class Definicao_Atributos:
    def __init__(self, nome:str, valor:int) -> None:
        self.name = nome
        self.valor = valor
        self.desc01 = str
        self.desc02 = str
        self.desc03 = str
        self.desc04 = str
        self.desc05 = str
        self.desc06 = str
        self.desc07 = str

    def name_definition(self):
        if self.name == "strength":
            self.desc01 = "Incorpóreo"
            self.desc02 = "Incapaz"
            self.desc03 = "Fraco"
            self.desc04 = "Mediano"
            self.desc05 = "Forte"
            self.desc06 = "Super Poderoso"
            self.desc07 = "Imbatível"
        elif self.name == "dexterity":
            self.desc01 = "Desacordado"
            self.desc02 = "Abatido"
            self.desc03 = "Desajeitado"
            self.desc04 = "Regular"
            self.desc05 = "Ágil"
            self.desc06 = "Ninja"
            self.desc07 = "Imperceptível"
        elif self.name == "constitution":
            self.desc01 = "Espectro"
            self.desc02 = "Enfermo"
            self.desc03 = "Frágil"
            self.desc04 = "Saudável"
            self.desc05 = "Durão"
            self.desc06 = "Super Resisténte"
            self.desc07 = "Imortal"
        elif self.name == "wisdom":
            self.desc01 = "Inconsciente"
            self.desc02 = "Irracional"
            self.desc03 = "Desatento"
            self.desc04 = "Simples"
            self.desc05 = "Perspicaz"
            self.desc06 = "Filósofo"
            self.desc07 = "Iluminado"
        elif self.name == "intelligence":
            self.desc01 = "Inanimado"
            self.desc02 = "Incivilizado"
            self.desc03 = "Parvo"
            self.desc04 = "Medíocre"
            self.desc05 = "Estudado"
            self.desc06 = "Gênio"
            self.desc07 = "Onisciente"
        elif self.name == "charisma":
            self.desc01 = "Aberração"
            self.desc02 = "Inexpressivo"
            self.desc03 = "Rude"
            self.desc04 = "Sociável"
            self.desc05 = "Persuasivo"
            self.desc06 = "Influente"
            self.desc07 = "Ídolo"
        else:
            pass
        
        return self.name
    
    def valor_definition(self):
        if self.valor == 0:
            self.valor = self.valor, self.desc01
        elif self.valor >= 1 and self.valor <= 5:
            self.valor = self.valor, self.desc02
        elif self.valor >= 6 and self.self.valor <= 9:
            self.valor = self.valor, self.desc03
        elif self.valor >= 10 and self.valor <= 11:
            self.valor = self.valor, self.desc04
        elif self.valor >= 12 and self.valor <= 15:
            self.valor = self.valor, self.desc05
        elif self.valor >= 16 and self.valor <= 20:
            self.valor = self.valor, self.desc06
        else:
            self.valor = self.valor, self.desc07
        
        return self.valor