import os
from personagem import Character
from raca import *
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
    print("1 - Anão\n2 - Elfo\n3 - Bárbaro\n4 - Humano\n5 - Draconato\n6 - Gnomo\n7 - Ladrão")
    raca_personagem=int(input("Digite o número da a raça do seu personagem: "))
    if raca_personagem == 1:
        print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n11 - Anão da Colina\n12 - Anão da Montanha")
        raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
        if raca_personagem == 11:
            raca_personagem = "Anão da Colina"
            ob = Raca_Hill_Dwarf()
            teste_raca1 = False
        elif raca_personagem == 12:
            raca_personagem = "Anão da Montanha"
            ob = Raca_Mountain_Dwarf()
            teste_raca1 = False
        else:
            print("Número digitado INCORRETO")
            raca_personagem = "Humano"
            ob = Raca_Human()
    elif raca_personagem == 2:
        print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n21 - Alto Elfo\n22 - Elfo da Floresta\n23 - Elfo Negro 'Drow'")
        raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
        if raca_personagem == 21:
            raca_personagem = "Alto Elfo"
            ob = Raca_High_Elf()
            teste_raca1 = False
        elif raca_personagem == 22:
            raca_personagem = "Elfo da Floresta"
            ob = Raca_Wood_Elf()
            teste_raca1 = False
        elif raca_personagem == 23:
            raca_personagem = "Elfo Negro 'Drow'"
            ob = Raca_Dark_Elf()
            teste_raca1 = False
        else:
            print("Número digitado INCORRETO")
            raca_personagem = "Humano"
            ob = Raca_Human()
    elif raca_personagem == 3:
        print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n31 - Pés Leves\n32 - Robusto")
        raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
        if raca_personagem == 31:
            raca_personagem = "Pés Leves"
            ob = Raca_Lightfoot()
            teste_raca1 = False
        elif raca_personagem == 32:
            raca_personagem = "Robusto"
            ob = Raca_Stout()
            teste_raca1 = False
        else:
            print("Número digitado INCORRETO")
            raca_personagem = "Humano"
            ob = Raca_Human()
    elif raca_personagem == 4:
        raca_personagem = "Humano"
        ob = Raca_Human()
        teste_raca1 = False
    elif raca_personagem == 5:
        raca_personagem = "Draconato"
        ob = Raca_Dragonborn()
        teste_raca1 = False
    elif raca_personagem == 6:
        print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n61 - Gnomo da Floresta\n62 - Gnomo da Pedra")
        raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
        if raca_personagem == 61:
            raca_personagem = "Gnomo da Floresta"
            ob = Raca_Forest_Gnome()
            teste_raca1 = False
        elif raca_personagem == 62:
            raca_personagem = "Gnomo da Pedra"
            ob = Raca_Rock_Gnome()
            teste_raca1 = False
        else:
            print("Número digitado INCORRETO")
            raca_personagem = "Humano"
            ob = Raca_Human()
    elif raca_personagem == 7:
        raca_personagem = "Ladrão"
        ob = Raca_Tiefling()
        teste_raca1 = False
    else:
        print("Número digitado INCORRETO Digite o Número novamente")
        raca_personagem = "Humano"
        ob = Raca_Human()
        
teste_raca2 = True
while teste_raca2:
    print(f"A raça do seu personagem é: '{raca_personagem}' ?")
    confirmacao_raca=int(input("Digite 1 para SIM e 2 para NÃO: "))
    if confirmacao_raca == 1:
        teste_raca2 = False
    elif confirmacao_raca == 2:
        print("1 - Anão\n2 - Elfo\n3 - Bárbaro\n4 - Humano\n5 - Draconato\n6 - Gnomo\n7 - Ladrão")
        raca_personagem=int(input("Digite o número da a raça do seu personagem: "))
        if raca_personagem == 1:
            print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n11 - Anão da Colina\n12 - Anão da Montanha")
            raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
            if raca_personagem == 11:
                raca_personagem = "Anão da Colina"
                ob = Raca_Hill_Dwarf()
            elif raca_personagem == 12:
                raca_personagem = "Anão da Montanha"
                ob = Raca_Mountain_Dwarf()
            else:
                print("Número digitado INCORRETO")
                raca_personagem = "Humano"
            ob = Raca_Human()
        elif raca_personagem == 2:
            print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n21 - Alto Elfo\n22 - Elfo da Floresta\n23 - Elfo Negro 'Drow'")
            raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
            if raca_personagem == 21:
                raca_personagem = "Alto Elfo"
                ob = Raca_High_Elf()
            elif raca_personagem == 22:
                raca_personagem = "Elfo da Floresta"
                ob = Raca_Wood_Elf()
            elif raca_personagem == 23:
                raca_personagem = "Elfo Negro 'Drow'"
                ob = Raca_Dark_Elf()
            else:
                print("Número digitado INCORRETO")
                raca_personagem = "Humano"
                ob = Raca_Human()
        elif raca_personagem == 3:
            print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n31 - Pés Leves\n32 - Robusto")
            raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
            if raca_personagem == 31:
                raca_personagem = "Pés Leves"
                ob = Raca_Lightfoot()
            elif raca_personagem == 32:
                raca_personagem = "Robusto"
                ob = Raca_Stout()
            else:
                print("Número digitado INCORRETO")
                raca_personagem = "Humano"
                ob = Raca_Human()
        elif raca_personagem == 4:
            raca_personagem = "Humano"
            ob = Raca_Human()
        elif raca_personagem == 5:
            raca_personagem = "Draconato"
            ob = Raca_Dragonborn()
        elif raca_personagem == 6:
            print("Parece que sua raça tem uma Sub-Raça, escolha uma Sub-Raça\n61 - Gnomo da Floresta\n62 - Gnomo da Pedra")
            raca_personagem=int(input("Digite o número da a Sub-Raça do seu personagem: "))
            if raca_personagem == 61:
                raca_personagem = "Gnomo da Floresta"
                ob = Raca_Forest_Gnome()
            elif raca_personagem == 62:
                raca_personagem = "Gnomo da Pedra"
                ob = Raca_Rock_Gnome()
            else:
                print("Número digitado INCORRETO")
                raca_personagem = "Humano"
                ob = Raca_Human()
        elif raca_personagem == 7:
            raca_personagem = "Ladrão"
            ob = Raca_Tiefling()
        else:
            print("Número digitado INCORRETO Digite o Número novamente")

x = Character(nome_personagem, raca_personagem)
print(ob)
x.atributos()
x.strength_definition()
x.dexterity_definition()
x.constitution_definition()
x.wisdom_definition()
x.intelligence_definition()
x.charisma_definition()
print(x)
os.system("pause")