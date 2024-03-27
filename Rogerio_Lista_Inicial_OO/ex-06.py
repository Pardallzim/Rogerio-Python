class TV:

    def __init__(self, numero_canal, volume):
        self.numero_canal = numero_canal
        self.volume = volume

    def trocar_canal(self, novo_canal):
        self.numero_canal = novo_canal
        return self.numero_canal

    def aumentar_volume(self, aumentar):
        if aumentar < self.volume:
            print("inválido")
        else:
            self.volume = aumentar
            return f"Volume da TV é:{self.volume}"

    def diminuir_volume(self,diminuir):
        if diminuir > self.volume:
            print("inválido")
        else:
            self.volume = diminuir
            return f"Volume da TV é:{self.volume}"
    
    def retornar_canal(self):
        return self.numero_canal
    
    def retornar_volume(self):
        return self.volume

tv = TV(1, 0)
print("canal ", tv.retornar_canal())
print("Volume da TV: ", tv.retornar_volume())
novo_canal = int(input("Digite o número do canal: "))
print(tv.trocar_canal(novo_canal))
print("canal ", tv.retornar_canal())
print("Volume da TV: ", tv.retornar_volume())
aumentar = int(input("Digite o numero para aumentar o volume: "))
tv.aumentar_volume(aumentar)
print("Volume da TV: ", tv.retornar_volume())
dimiuir = int(input("Digite o numero para diminuir o volume: "))
tv.diminuir_volume(dimiuir)
print("Volume da TV: ", tv.retornar_volume())