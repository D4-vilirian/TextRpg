import json
import random
with open("textrpg.json", "r") as arquivo:
    dados = json.load(arquivo)
while True:
    time = random.choice (["sol","lua"])
    vida_zumbi = dados["zumbi"] ["vida"]
    dano_zumbi = dados["zumbi"] ["dano"]
    vida_player = dados["player"] ["vida"]
    dano_player = dados["player"] ["dano"]
    vida_zumbi = vida_zumbi + dados[time] ["zumbi"] ["vida"] 
    dano_zumbi = dano_zumbi + dados[time] ["zumbi"] ["dano"]
    vida_player = vida_player + dados[time] ["player"] ["vida"]
    dano_player = dano_player + dados[time] ["player"] ["dano"]
    print("clima da run atual:", time)
    print("vida do zumbi:", vida_zumbi)
    print("vida do player:", vida_player)
    while "random.choice" == "sol":
            if acao == "pocao pequena": 
                cura = dados["pocoes"] ["pocao pequena"] ["cura"]
                vida_player = min(vida_player + cura , 100)
                print("você curou!", vida_player)
    while "random.choice" == "lua":
            if acao == "pocao média":
                        cura = dados["pocoes"] ["pocao média"] ["cura"]
                        vida_player = min(vida_player + cura , 100)
                        print("você curou!", vida_player)
    if vida_player <= 10 :
                if acao == "poção grande": 
                            cura = dados["pocoes"] ["pocao grande"] ["cura"]
                            vida_player = min(vida_player + cura , 100)
                            print("você curou!", vida_player)
    else:
        acao = input("digite atacar para bater no zumbi, com menos de 20 de vida: digite pocao (pequena, média ou grande ) para usar uma pocao:")
        if acao == "atacar" :     
                 vida_zumbi = vida_zumbi - dano_player
                 print("você atacou! vida do zumbi agora:", vida_zumbi)
                 vida_player = vida_player - dano_zumbi 
                 print("o zumbi te atacou!")
                 print("vida zumbi", vida_zumbi)
                 print("vida player", vida_player)
    while vida_zumbi > 0:
        acao = input("digite atacar   para bater no zumbi, com menos de 20 de vida: digite pocao (pequena, média ou grande ) para usar uma pocao:")
        if acao == "atacar" :
            vida_zumbi= vida_zumbi - dano_player 
            print("você atacou! vida do zumbi agora:", vida_zumbi)
            vida_player=vida_player-dano_zumbi
            print("o zumbi te atacou!")
            print("vida zumbi", vida_zumbi)
            print("vida player", vida_player)
            if vida_zumbi <= 0:
                novo = input("digite recomeçar para recomeçar,digite sair para sair:")
                if novo == "recomeçar":
                    print("novo jogo")
                if novo == "sair":
                    break
            if vida_player <= 0:
                novo = input("digite recomeçar para recomeçar, digite sair para sair:")
                if novo == "recomeçar":
                    print("novo jogo")
                if novo == "sair":
                    break     
    
