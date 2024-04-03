class Definicao_Atributos:
    def __init__(self) -> None:
        self.desc01 = str
        self.desc02 = str
        self.desc03 = str
        self.desc04 = str
        self.desc05 = str
        self.desc06 = str
        self.desc07 = str

    def name_definition(self, name:str):
        if name == "strength":
            self.desc01 = 
            self.desc02 = 
            self.desc03 = 
            self.desc04 = 
            self.desc05 = 
            self.desc06 = 
            self.desc07 = 
        elif name == "dexterity":
            self.desc01 = 
            self.desc02 = 
            self.desc03 = 
            self.desc04 = 
            self.desc05 = 
            self.desc06 = 
            self.desc07 = 
        elif name == "constitution":
            self.desc01 = 
            self.desc02 = 
            self.desc03 = 
            self.desc04 = 
            self.desc05 = 
            self.desc06 = 
            self.desc07 = 
        elif name == "wisdom":
            self.desc01 = 
            self.desc02 = 
            self.desc03 = 
            self.desc04 = 
            self.desc05 = 
            self.desc06 = 
            self.desc07 = 
        elif name == "intelligence":
            self.desc01 = 
            self.desc02 = 
            self.desc03 = 
            self.desc04 = 
            self.desc05 = 
            self.desc06 = 
            self.desc07 = 
        elif name == "charisma":
            self.desc01 = 
            self.desc02 = 
            self.desc03 = 
            self.desc04 = 
            self.desc05 = 
            self.desc06 = 
            self.desc07 = 
        else:
            pass
        
        return name
    
    def valor_definition(self, valor:int):
        if valor == 0:
            valor = valor, self.desc01
        elif valor >= 1 and valor <= 5:
            valor = valor, self.desc02
        elif valor >= 6 and valor <= 9:
            valor = valor, self.desc03
        elif valor >= 10 and valor <= 11:
            valor = valor, self.desc04
        elif valor >= 12 and valor <= 15:
            valor = valor, self.desc05
        elif valor >= 16 and valor <= 20:
            valor = valor, self.desc06
        else:
            valor = valor, self.desc07
        
        return valor