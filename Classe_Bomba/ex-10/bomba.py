class BombaCombustivel:
    def __init__(self):
        self.__tipo_combustivel = None
        self.__valor_litro = 0.0
        self.__quantidade_combustivel = 0

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel
    
    @tipo_combustivel.setter
    def tipo_combustivel(self, x):
        self.__tipo_combustivel = x