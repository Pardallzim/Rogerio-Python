import random
import os
class Character:
    def __init__(self, nome:str, raca:str) -> None:
        self.nome = nome
        self.raca = raca
        self.__strength = random.randint(0,21) 
        self.__dexterity = random.randint(0,21)
        self.__constitution = random.randint(0,21)
        self.__wisdom = random.randint(0,21)
        self.__intelligence = random.randint(0,21)
        self.__charisma = random.randint(0,21)

    def strength_definition(self):
        if self.__strength == 0:
            self.__strength = self.__strength,"Incorpóreo"
        elif self.__strength >= 1 and self.__strength <= 5:
            self.__strength = self.__strength,"Incapaz"
        elif self.__strength >= 6 and self.__strength <= 9:
            self.__strength = self.__strength,"Fraco"
        elif self.__strength >= 10 and self.__strength <= 11:
            self.__strength = self.__strength,"Mediano"
        elif self.__strength >= 12 and self.__strength <= 15:
            self.__strength = self.__strength,"Forte"
        elif self.__strength >= 16 and self.__strength <= 20:
            self.__strength = self.__strength,"Super Poderoso"
        else:
            self.__strength = self.__strength,"Imbatível"
        
        return self.__strength

    def dexterity_definition(self):
        if self.__dexterity == 0:
            self.__dexterity = self.__dexterity,"Desacordado"
        elif self.__dexterity >= 1 and self.__dexterity <= 5:
            self.__dexterity = self.__dexterity,"Abatido"
        elif self.__dexterity >= 6 and self.__dexterity <= 9:
            self.__dexterity = self.__dexterity,"Desajeitado"
        elif self.__dexterity >= 10 and self.__dexterity <= 11:
            self.__dexterity = self.__dexterity,"Regular"
        elif self.__dexterity >= 12 and self.__dexterity <= 15:
            self.__dexterity = self.__dexterity,"Ágil"
        elif self.__dexterity >= 16 and self.__dexterity <= 20:
            self.__dexterity = self.__dexterity,"Ninja"
        else:
            self.__dexterity = self.__dexterity,"Imperceptível"
        return self.__dexterity

    def constitution_definition(self):
        if self.__constitution == 0:
            self.__constitution = self.__constitution,"Espectro"
        elif self.__constitution >= 1 and self.__constitution <= 5:
            self.__constitution = self.__constitution,"Enfermo"
        elif self.__constitution >= 6 and self.__constitution <= 9:
            self.__constitution = self.__constitution,"Frágil"
        elif self.__constitution >= 10 and self.__constitution <= 11:
            self.__constitution = self.__constitution,"Saudável"
        elif self.__constitution >= 12 and self.__constitution <= 15:
            self.__constitution = self.__constitution,"Durão"
        elif self.__constitution >= 16 and self.__constitution <= 20:
            self.__constitution = self.__constitution,"Super Resisténte"
        else:
            self.__constitution = self.__constitution,"Imortal"
        
        return self.__constitution

    def wisdom_definition(self):
        if self.__wisdom == 0:
            self.__wisdom = self.__wisdom,"Inconsciente"
        elif self.__wisdom >= 1 and self.__wisdom <= 5:
            self.__wisdom = self.__wisdom,"Irracional"
        elif self.__wisdom >= 6 and self.__wisdom <= 9:
            self.__wisdom = self.__wisdom,"Desatento"
        elif self.__wisdom >= 10 and self.__wisdom <= 11:
            self.__wisdom = self.__wisdom,"Simples"
        elif self.__wisdom >= 12 and self.__wisdom <= 15:
            self.__wisdom = self.__wisdom,"Perspicaz"
        elif self.__wisdom >= 16 and self.__wisdom <= 20:
            self.__wisdom = self.__wisdom,"Filósofo"
        else:
            self.__wisdom = self.__wisdom,"Iluminado"
        
        return self.__wisdom

    def intelligence_definition(self):
        if self.__intelligence == 0:
            self.__intelligence = self.__intelligence,"Inanimado"
        elif self.__intelligence >= 1 and self.__intelligence <= 5:
            self.__intelligence = self.__intelligence,"Incivilizado"
        elif self.__intelligence >= 6 and self.__intelligence <= 9:
            self.__intelligence = self.__intelligence,"Parvo"
        elif self.__intelligence >= 10 and self.__intelligence <= 11:
            self.__intelligence = self.__intelligence,"Medíocre"
        elif self.__intelligence >= 12 and self.__intelligence <= 15:
            self.__intelligence = self.__intelligence,"Estudado"
        elif self.__intelligence >= 16 and self.__intelligence <= 20:
            self.__intelligence = self.__intelligence,"Gênio"
        else:
            self.__intelligence = self.__intelligence,"Onisciente"
        
        return self.__intelligence

    def charisma_definition(self):
        if self.__charisma == 0:
            self.__charisma = self.__charisma,"Aberração"
        elif self.__charisma >= 1 and self.__charisma <= 5:
            self.__charisma = self.__charisma,"Inexpressivo"
        elif self.__charisma >= 6 and self.__charisma <= 9:
            self.__charisma = self.__charisma,"Rude"
        elif self.__charisma >= 10 and self.__charisma <= 11:
            self.__charisma = self.__charisma,"Sociável"
        elif self.__charisma >= 12 and self.__charisma <= 15:
            self.__charisma = self.__charisma,"Persuasivo"
        elif self.__charisma >= 16 and self.__charisma <= 20:
            self.__charisma = self.__charisma,"Influente"
        else:
            self.__charisma = self.__charisma,"Ídolo"
        
        return self.__charisma

    def __str__(self) -> str:
        return f"Nome : {self.nome} \nRaça : {self.raca} \nForça : {self.__strength}\nDestreza : {self.__dexterity}\nConstituição : {self.__constitution}\nSabedoria : {self.__wisdom}\nInteligencia : {self.__intelligence}\nCarisma : {self.__charisma}\n"

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
        raca_personagem = "Dwarf"
        teste_raca1 = False
    elif raca_personagem == 2:
        raca_personagem = "Elf"
        teste_raca1 = False
    elif raca_personagem == 3:
        raca_personagem = "Barbaro"
        teste_raca1 = False
    elif raca_personagem == 4:
        raca_personagem = "Human"
        teste_raca1 = False
    elif raca_personagem == 5:
        raca_personagem = "Dragonborn"
        teste_raca1 = False
    elif raca_personagem == 6:
        raca_personagem = "Gnome"
        teste_raca1 = False
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
            raca_personagem = "Dwarf"
        elif raca_personagem == 2:
            raca_personagem = "Elf"
        elif raca_personagem == 3:
            raca_personagem = "Barbaro"
        elif raca_personagem == 4:
            raca_personagem = "Human"
        elif raca_personagem == 5:
            raca_personagem = "Dragonborn"
        elif raca_personagem == 6:
            raca_personagem = "Gnome"
        elif raca_personagem == 7:
            raca_personagem = "Tiefling"
        else:
            raca_personagem = "Human"
    else:
        print("Erro de digitação Digite apenas 1 OU 2 para SIM e NÃO respectivamente")

x = Character(nome_personagem, raca_personagem)
x.strength_definition()
x.dexterity_definition()
x.constitution_definition()
x.wisdom_definition()
x.intelligence_definition()
x.charisma_definition()
print(x)
os.system("pause")