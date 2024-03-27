class Pessoa:

    def __init__(self,nome:str,idade:int,peso:float,altura:float)->None:
        self.nome = nome
        self._idade = idade
        self.__peso = peso
        self.altura = altura
    
    def envelhecer(self)->None:
        self._idade += 1
        self.crescer()

    def crescer(self)->None:
        if self._idade < 21:
            self.altura += 0.04
        else:
            pass    

    def engordar(self, grama:float)->None:
        self.__peso += grama

    def emagrecer(self, grama:float)->None:
        self.__peso -= grama

    def __str__(self):
        return f"Eu sou o {self.nome} tenho {self._idade} com {self.__peso}Kg e {self.altura}M."

rogerio = Pessoa("Rogério",16,78.65,1.72)     
print(rogerio)  
rogerio.envelhecer() 
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
rogerio.envelhecer()
print(rogerio)