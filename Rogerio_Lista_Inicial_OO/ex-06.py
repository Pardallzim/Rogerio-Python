class TV:

    def __init__(self, numero_canal, volume):
        self.numero_canal = numero_canal
        self.volume = volume

    def trocar_canal(self):
        self.numero_canal = self.numero_canal + 1
        return self.numero_canal

    def aumentar_volume(self):
        self.volume = int(input("Aumentar volume até: "))
        if self.volume > 99 or self.volume < 0:
            print("inválido")

    def diminuir_volume(self):
        self.volume = int(input("Diminuir volume até: "))
        if self.volume > 99 or self.volume < 0:
            print("inválido")
        else:
            print(f"Volume da TV é:{self.volume}")
    
    def retornar_canal(self):
        return self.numero_canal

tv = TV(1, 0)
print("canal ", tv.retornar_canal())
print("Volume da TV: ", tv.retornar_volume())
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
tv.trocar_canal()
print(tv.trocar_canal())
print("canal ", tv.retornar_canal())
tv.aumentar_volume()
print("Volume da TV: ", tv.retornar_volume())
tv.diminuir_volume()
print("Volume da TV: ", tv.retornar_volume())