import json
import random
with open("textrpg.json", "r") as arquivo:
    dados = json.load(arquivo)
while True:
    time = random.choice (["sol","lua","nenhum","chuva"])
    vida_zumbi = dados["zumbi"] ["vida"]
    dano_zumbi = dados["zumbi"] ["dano"]
    vida_player = dados["player"] ["vida"]
    dano_player = dados["player"] ["dano"]
    vida_ptimeldano_zumbieyer = dados["ptimeldano zumbieyer"] ["vida"]
    dano_ptimeldano_zumbieyer = dados["ptimeldano zumbieyer"] ["dano"]
    vida_zumbi = vida_zumbi + dados[time] ["zumbi"] ["vida"] 
    dano_zumbi = dano_zumbi + dados[time] ["zumbi"] ["dano"]
    vida_player = vida_player + dados[time] ["player"] ["vida"]
    dano_player = dano_player + dados[time] ["player"] ["dano"]
    print("clima da run atual:", time)
    print("vida do zumbi:", vida_zumbi)
    print("vida do player:", vida_player)
    acao = input("digite atacar para atacar :")
    if acao == "atacar" :     
                 vida_zumbi = vida_zumbi - dano_player
                 print("você atacou! vida do zumbi agora:", vida_zumbi)
                 vida_player = vida_player - dano_zumbi 
                 print("o zumbi te atacou!")
                 print("vida do zumbi", vida_zumbi)
                 print("vida do player", vida_player)
    while vida_zumbi > 0:
        acao = input("digite atacar para atacar :")
        if acao == "atacar" :
            vida_zumbi= vida_zumbi - dano_player 
            print("você atacou! vida do zumbi agora:", vida_zumbi)
            vida_player=vida_player-dano_zumbi
            print("o zumbi te atacou!")
            print("vida do zumbi", vida_zumbi)
            print("vida do player", vida_player)
            if vida_player <= 0:
                novo = input("você morreu! digite recomeçar :")
                if novo == "recomeçar":
                    print(" você perdeu! novo jogo:")
                    break
            if vida_zumbi <= 0:
                vida_player = vida_player + dados["benção"] ["benção dos mortos-vivos"] ["player"] ["vida"]
                dano_player = dano_player + dados["benção"] ["benção dos mortos-vivos"] ["player"] ["dano"]
                print("você recebeu a benção dos mortos vivos por matar o zumbi!")
                novo = input("digite fase 2 para a fase 2:")
                if novo == "fase2":
                    print("vida do ptimeldano:", vida_ptimeldano_zumbieyer)
                    print("vida do player:", vida_player)
                    acao = input ("digite atacar para atacar o boss ptimeldano zumbieyer :")   
                    if acao == "atacar":
                        vida_ptimeldano_zumbieyer = vida_ptimeldano_zumbieyer - dano_player
                        print("você atacou!")
                        vida_player = vida_player - dano_ptimeldano_zumbieyer
                        print("o ptimeldano te atacou!")
                        print("vida do player:", vida_player)
                        print("vida do ptimeldano:", vida_ptimeldano_zumbieyer)
        while vida_ptimeldano_zumbieyer > 0:
                    print("vida do ptimeldano:", vida_ptimeldano_zumbieyer)
                    print("vida do player:", vida_player)
                    acao = input ("digite atacar para atacar o boss ptimeldano zumbieyer :")
                    if acao == "atacar":
                        vida_ptimeldano_zumbieyer = vida_ptimeldano_zumbieyer - dano_player
                        print("você atacou!")
                        vida_player = vida_player - dano_ptimeldano_zumbieyer
                        print("o ptimeldano te atacou!")
                        print("vida do player:", vida_player)
                        print("vida do ptimeldano:", vida_ptimeldano_zumbieyer)
    if vida_player <= 0:
                novo = input("você morreu! digite recomeçar :")
                if novo == "recomeçar":
                    print("você morreu! novo jogo:")
                    break
    if vida_ptimeldano_zumbieyer <= 0:
                novo = input("voce matou o boss!espere mais no futuro. digite recomeçar :")
                if novo == "recomeçar":
                    print("novo jogo")
                    break
