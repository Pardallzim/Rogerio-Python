import random
import os
from definicao_atributos import Definicao_Atributos 
from raca import Raca
class Character(Raca):
    def __init__(self, nome:str, raca:str) -> None:
        super().__init__()
        self.nome = nome
        self.raca = raca
        self.__strength = random.randint(0,21) + self.raca_strength
        self.__dexterity = random.randint(0,21) + self.raca_dexterity
        self.__constitution = random.randint(0,21) + self.raca_constitution
        self.__wisdom = random.randint(0,21) + self.raca_wisdom
        self.__intelligence = random.randint(0,21) + self.raca_intelligence
        self.__charisma = random.randint(0,21) + self.raca_charisma

    def __str__(self) -> str:
        return f"Status da Raça :\nForça : {self.raca_strength}\nDestreza : {self.raca_dexterity}\nConstituição : {self.raca_constitution}\nSabedoria : {self.raca_wisdom}\nInteligencia : {self.raca_intelligence}\nCarisma : {self.raca_charisma}\n\n\nNome : {self.nome} \nRaça : {self.raca} \nForça : {self.__strength}\nDestreza : {self.__dexterity}\nConstituição : {self.__constitution}\nSabedoria : {self.__wisdom}\nInteligencia : {self.__intelligence}\nCarisma : {self.__charisma}\n"

nome_personagem=str(input("Digite o nome do seu personagem: "))
teste_nome = True
while teste_nome:
    print(f"O nome do seu personagem é: '{nome_personagem}' ?")
    confirmacao_nome=int(input("Digite 1 para SIM e 2 para NÃO: "))
    if confirmacao_nome == 1:
        teste_nome = False
    elif confirmacao_nome == 2:
        nome_personagem=str(input("Digite o nome do seu personagem: "))
    else:
        print("Erro de digitação Digite apenas 1 OU 2 para SIM e NÃO respectivamente")

teste_raca1 = True
while teste_raca1:
    print("1 - Dwarf\n2 - Elf\n3 - Barbaro\n4 - Human\n5 - Dragonborn\n6 - Gnome\n7 - Tiefling")
    raca_personagem=int(input("Digite o número da a raça do seu personagem: "))
    if raca_personagem == 1:
        print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n11 - Hill Dwarf\n12 - Mountain Dwarf")
        raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
        if raca_personagem == 11:
            raca_personagem = "Hill Dwarf"
            teste_raca1 = False
        elif raca_personagem == 12:
            raca_personagem = "Mountain Dwarf"
            teste_raca1 = False
        else:
            print("Número digitado INCORRETO")
    elif raca_personagem == 2:
        print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n21 - High Elf\n22 - Wood Elf\n23 - Dark Elf 'Drow'")
        raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
        if raca_personagem == 21:
            raca_personagem = "High Elf"
            teste_raca1 = False
        elif raca_personagem == 22:
            raca_personagem = "Wood Elf"
            teste_raca1 = False
        elif raca_personagem == 23:
            raca_personagem = "Dark Elf 'Drow'"
            teste_raca1 = False
        else:
            print("Número digitado INCORRETO")
    elif raca_personagem == 3:
        print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n31 - Lightfoot\n32 - Stout")
        raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
        if raca_personagem == 31:
            raca_personagem = "Lightfoot"
            teste_raca1 = False
        elif raca_personagem == 32:
            raca_personagem = "Stout"
            teste_raca1 = False
        else:
            print("Número digitado INCORRETO")
    elif raca_personagem == 4:
        raca_personagem = "Human"
        teste_raca1 = False
    elif raca_personagem == 5:
        raca_personagem = "Dragonborn"
        teste_raca1 = False
    elif raca_personagem == 6:
        print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n61 - Forest Gnome\n62 - Rock Gnome")
        raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
        if raca_personagem == 61:
            raca_personagem = "Forest Gnome"
            teste_raca1 = False
        elif raca_personagem == 62:
            raca_personagem = "Rock Gnome"
            teste_raca1 = False
        else:
            print("Número digitado INCORRETO")
    elif raca_personagem == 7:
        raca_personagem = "Tiefling"
        teste_raca1 = False
    else:
        print("Número digitado INCORRETO Digite o Número novamente")
teste_raca2 = True
while teste_raca2:
    print(f"A raça do seu personagem é: '{raca_personagem}' ?")
    confirmacao_raca=int(input("Digite 1 para SIM e 2 para NÃO: "))
    if confirmacao_raca == 1:
        teste_raca2 = False
    elif confirmacao_raca == 2:
        print("1 - Dwarf\n2 - Elf\n3 - Barbaro\n4 - Human\n5 - Dragonborn\n6 - Gnome\n7 - Tiefling")
        raca_personagem=int(input("Digite o número da a raça do seu personagem: "))
        if raca_personagem == 1:
            print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n11 - Hill Dwarf\n12 - Mountain Dwarf")
            raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
            if raca_personagem == 11:
                raca_personagem = "Hill Dwarf"
            elif raca_personagem == 12:
                raca_personagem = "Mountain Dwarf"
            else:
                print("Número digitado INCORRETO")
        elif raca_personagem == 2:
            print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n21 - High Elf\n22 - Wood Elf\n23 - Dark Elf 'Drow'")
            raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
            if raca_personagem == 21:
                raca_personagem = "High Elf"
            elif raca_personagem == 22:
                raca_personagem = "Wood Elf"
            elif raca_personagem == 23:
                raca_personagem = "Dark Elf 'Drow'"
            else:
                print("Número digitado INCORRETO")
        elif raca_personagem == 3:
            print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n31 - Lightfoot\n32 - Stout")
            raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
            if raca_personagem == 31:
                raca_personagem = "Lightfoot"
            elif raca_personagem == 32:
                raca_personagem = "Stout"
            else:
                print("Número digitado INCORRETO")
        elif raca_personagem == 4:
            raca_personagem = "Human"
        elif raca_personagem == 5:
            raca_personagem = "Dragonborn"
        elif raca_personagem == 6:
            print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n61 - Forest Gnome\n62 - Rock Gnome")
            raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
            if raca_personagem == 61:
                raca_personagem = "Forest Gnome"
            elif raca_personagem == 62:
                raca_personagem = "Rock Gnome"
            else:
                print("Número digitado INCORRETO")
        elif raca_personagem == 7:
            raca_personagem = "Tiefling"
        else:
            print("Número digitado INCORRETO Digite o Número novamente")

x = Character(nome_personagem, raca_personagem)
print(x)
os.system("pause")