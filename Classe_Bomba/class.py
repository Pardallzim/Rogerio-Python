class Bomba:
    def __init__(self,tipo_combustivel,valor_litro,quantidade_combustivel):
        self.__tipo_combustivel = tipo_combustivel
        self.__valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    """@property
    def tipo(self):
        return self.__tipo_combustivel
    
    @property
    def valorl(self):
        return self.__valor_litro
    
    @property
    def quantcombustivel(self):
        return self.__quantidade_combustivel
    
    @tipo.setter
    def tipo(self, valor):
        self.__tipo_combustivel = valor

    @valorl.setter
    def valorl(self, valor):
        self.__valor_litro = valor

    @quantcombustivel.setter
    def quantcombustivel(self, valor):
        self.__quantidade_combustivel = valor"""

    def abastecer_por_valor(self, valor_abastecer:float):
        self.quantidade_combustivel -= (valor_abastecer / self.__valor_litro)
        return valor_abastecer / self.__valor_litro
    
    def bomba_combustivel(self):
        return self.quantidade_combustivel
        
    def abastecer_por_litro(self, litro_abastecer:float):
        self.quantidade_combustivel -= litro_abastecer
        return self.__valor_litro * litro_abastecer

    def alterar_valor(self, novo_valor:float):
        self.__valor_litro = novo_valor
    
    def alterar_combustivel(self, novo_combustivel:str):
        self.__tipo_combustivel = novo_combustivel
        return self.__tipo_combustivel
    
    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade

bomba_gasolina = Bomba("Etanol", 4.15, 20000)
bomba_gasolina.abastecer_por_valor(100)
print(bomba_gasolina.bomba_combustivel())
