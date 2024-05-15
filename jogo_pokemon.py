import random
import time
caverna = ["Zubat", "Geodude", "Aaron", "Onix"]
mato = ["Weedle", "Caterpie", "Metapod", "Bellsprout"]
nome_jogador=[]
pokedex=[]
prob_capt_mato=0.5
prob_capt_caverna=0.35
pokebolas=3
pokemon_inicial=["Bulbasaur", "squirtle", "charmander"]

def introducao():
    linha()
    print("                            |MUNDO POKÉMON|                            ")
    linha()
    print("Olá!")
    pausa(1)
    print("É um prazer conhecê-lo(a)!")
    pausa(1)
    print("Bem-vindo ao fabuloso mundo POKéMON!")
    pausa(1)
    print("Meu nome é CARVALHO!")
    pausa(1)
    print("Mas todos aqui me chamam de PROFESSOR OAK.")
    pausa(1)
    print("Este mundo é habitado por várias criaturas chamadas de POKéMON.")
    pausa(1)
    print("Mas primeiro, me fale um pouco sobre você!")
    pausa(1)
    print("Agora diga-me.")
    pausa(1)
    pergunta_genero()
    pausa(1)
    pergunta_nome()
    pausa(1)
    print(f"Certo, {nome_jogador[0]}!")
    pausa(1)
    print(f"A sua própria lenda POKéMON está prestes a começar!")
    pausa(1)
    print(f"Um mundo de sonhos e aventuras o aguarda! Então, vamos lá!")
    pausa(1)
    print("Agora escolha um pókemon inicial!")
    linha()
    escolha_pokemon_inicial()
    mostrar_pokedex()
    print(f"Você inicia com {pokebolas} Pokebolas!")
    pausa(1)
    print(f"VAMOS LÁ!")
    pausa(1)

def menu():
    while True:
        try:
            print(20*"-")
            print("|  MENU DE ESCOLHAS  |\n")
            print("[1] Caverna\n[2] Mato\n[3] Mostrar Pokédex\n[4] Sair")
            print(20*"-")
            
            escolha = int(input("Escolha uma opção: "))
            print(60*"-")
            if escolha==4:
                print(f"Até logo {nome_jogador[0]}!")
                pausa(1)
                print("Espero te reencontrar novamente...")
                break
            if escolha <=0 or escolha >3:
                print("Escolha incorreta, digite novamente!")
                continue
            if escolha ==1:
                explorar_caverna()
                            
            elif escolha ==2:
                    explorar_mato()
            elif escolha==3:
                mostrar_pokedex()
        except ValueError:
            print("Escolha inválida, Tente novamente!") 

def adicionar_pokebola(q_pokebolas):
    global pokebolas
    pokebolas=q_pokebolas
    prob=random.randint(0,2) 
    if prob==0:
        linha()
        print(f"Infelizmente você não encontrou nenhuma pokébola\n Suas pokébolas atuais são: {pokebolas}")
        linha()
    elif prob==1:
        pokebolas+=1
        linha()
        print(f"Parabéns você encontrou uma pokébola \nSuas pokébolas atuais são: {pokebolas}")
        linha()
    elif prob==2:
        pokebolas+=2
        linha()
        print(f"Parabéns! Você encontrou duas pokébolas \nSuas pokébolas atuais são: {pokebolas}")
        linha()   
    else:
        print("Erro!")

def sorteio_pokemon_aleatorio(pokemon):

    return random.choice(pokemon)   

def pergunta_genero():
       while True:
            try:
                genero = int(input("[1] Garoto\n[2] Garota\nVocê é um garoto ou uma garota? "))

                if genero == 1:
                    print("Olá garoto!")
                    break

                elif genero == 2:
                    print("Olá garota!")
                    break

                if genero < 1 or genero > 2:
                    print("Escolha a opção 1 ou 2 ,Tente novamente!")

            except ValueError:
                print("Escolha a opção 1 ou 2 ,Tente novamente!")

def pergunta_nome(): 
        while True:
            nome = input("Como se chama? ")

            if not nome or not nome.isalpha():
                print("Por favor, insira um nome válido.")

            else:
                nome_jogador.append(nome)
                return nome
            
def mostrar_pokedex():  
    print("===POKÉDEX===")
    for pokemon_cap in pokedex:
        print(f"-{pokemon_cap}")
        continue 
    print("=============")  
    pausa(1)      

def linha():
    print(60*"-")

def captura_pokemon(pokemon_alt):
                        pokedex.append(pokemon_aleatorio)
                        linha()
                        print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                        linha()
                        print("Voltando para o menu...")
                        pausa(1) 
                        

def prob_capturar_pokemon(probabilidade):
   return random.random() <= probabilidade

def pausa(x):
    time.sleep(x)    

def explorar_caverna():
    global pokebolas, pokemon_aleatorio, pokedex
    print("Você está adentrando a caverna...")
    pausa(1)
    adicionar_pokebola(pokebolas)
    pokemon_aleatorio = sorteio_pokemon_aleatorio(caverna)
    print(f"Você entrou na caverna e encontrou um {pokemon_aleatorio}!")
    
    if pokemon_aleatorio in pokedex:
        print(f"Você já tem o {pokemon_aleatorio} em sua pokédex!")
        print(f"Voltando para o menu...")
        pausa(1)
    else:
        while True:
            resposta = input("[1]-Sim\n[2]-Não\nDeseja tentar capturar esse pokémon? ")
            if resposta.isdigit():
                resposta = int(resposta)
                if resposta == 1:
                    if pokebolas <= 0:
                        print(f"Suas pokébolas acabaram")
                        break
                    if prob_capturar_pokemon(prob_capt_caverna):
                        captura_pokemon(pokemon_aleatorio)
                        break
                    else:
                        print(f"O {pokemon_aleatorio} escapou!")
                        if pokebolas > 0:
                                resposta2 = input(f"[1]-Sim\n[2]-Não\nQuer tentar capturar o {pokemon_aleatorio} novamente? ")
                                if resposta2.isdigit():
                                    resposta2=int(resposta2)
                                    if resposta ==1:    
                                        pokebolas -= 1
                                        if prob_capturar_pokemon(prob_capt_caverna):
                                            pokedex.append(pokemon_aleatorio)
                                            linha()
                                            print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                                            print(f"Você tem {pokebolas} pokébolas!")
                                            linha()
                                            print("Voltando para o menu...")
                                            pausa(1)
                                            break
                                        else:
                                            print(f"O {pokemon_aleatorio} escapou!")
                                            print(f"Você tem {pokebolas} pokébolas!")
                                            print("Voltando para o menu...")
                                            pausa(1)
                                            break
                                    elif resposta2==2:
                                        print("Voltando para o menu...")
                                        pausa(1)
                                        break
                                    elif resposta>2 or resposta<1:
                                        print("Erro, digite 1 para sim e 2 para não.")
                                        continue
                                         
                                else:
                                    print("Erro, digite 1 para sim e 2 para não.")
                                    continue
                            
                elif resposta == 2:
                    print("Voltando para o menu...")
                    pausa(1)
                    break
                else:
                    print("Erro, digite 1 para sim e 2 para não.")
                    continue
            else:
                print("Erro, digite 1 para sim e 2 para não.")
                continue


def explorar_mato():
            global pokebolas,pokemon_aleatorio,pokedex
            print("Você está adentrando no mato...")
            pausa(1)
            adicionar_pokebola(pokebolas)
            pokemon_aleatorio=sorteio_pokemon_aleatorio(mato)
            print(f"Você entrou no mato e encontrou um {pokemon_aleatorio}!")
                          
            if pokemon_aleatorio in pokedex:
                print(f"Você já tem o {pokemon_aleatorio} em sua pokédex!")
                print(f"Voltando para o menu...")
                pausa(1)
            else: 
                while True:                
                    resposta = input("[1]-Sim\n[2]-Não\nDeseja tentar capturar esse pokémon? ")                   
                    if resposta.isdigit():
                            resposta=int(resposta)
                            if resposta==1:
                                if prob_capturar_pokemon(prob_capt_mato):
                                    captura_pokemon(pokemon_aleatorio)
                                    break
                                else:    
                                    print(f"O {pokemon_aleatorio} escapou!")
                                    if pokebolas<=0:
                                        print(f"Suas pokébolas acabaram")
                                        break
                                    else:     
                                            resposta2 = input(f"[1]-Sim\n[2]-Não\nQuer tentar capturar o {pokemon_aleatorio} novamente? ")
                                            if resposta2.isdigit():
                                                resposta2=int(resposta2)
                                                if resposta2 ==1:
                                                    pokebolas-=1
                                                    
                                                    if prob_capturar_pokemon(prob_capt_mato):
                                                        pokedex.append(pokemon_aleatorio)
                                                        linha()
                                                        print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                                                        print(f"Você tem {pokebolas} pokébolas!")
                                                        linha()
                                                        print("Voltando para o menu...")
                                                        pausa(1)
                                                        break
                                                    else:
                                                        print(f"O {pokemon_aleatorio} escapou!")
                                                        print(f"Você tem {pokebolas} pokébolas!")
                                                        print("Voltando para o menu...")
                                                        pausa(1)
                                                        break
                                                elif resposta2==2:
                                                    print("Voltando para o menu...")
                                                    pausa(1)
                                                    break
                                            elif resposta2==2:
                                                print("Voltando para o menu...")
                                                pausa(1)
                                                break
                                                     
                                            elif resposta>2 or resposta<1:
                                                print("Erro, digite 1 para sim e 2 para não.")
                                                continue    
                                    
                            elif resposta==2:
                                print("Erro, digite 1 para sim e 2 para não.")
                                continue 

                            elif resposta>2 or resposta<1:
                                print("Erro, digite 1 para sim e 2 para não.")
                                continue    
                    else:
                        print("Erro, digite 1 para sim e 2 para não.")
                        continue       

def escolha_pokemon_inicial():
    print("Escolha o seu Pokémon inicial:")
    for i, pokemon in enumerate(pokemon_inicial, start=1):
        print(f"[{i}] {pokemon}")

    escolha_Pok_inc = input("Digite o número correspondente ao Pokémon que você deseja escolher: ")
    while not escolha_Pok_inc.isdigit() or not (1 <= int(escolha_Pok_inc) <= len(pokemon_inicial)):
        print("Escolha inválida. Por favor, digite o número correspondente ao Pokémon desejado.")
        escolha_Pok_inc = input("Digite o número correspondente ao Pokémon que você deseja escolher: ")

    pokemon_escolhido = pokemon_inicial[int(escolha_Pok_inc) - 1]
    linha()
    print(f"Você escolheu: {pokemon_escolhido}")
    print(f"Parabéns! Você recebeu o {pokemon_escolhido} em sua pokédex")
    linha()
    pokedex.append(pokemon_escolhido)
#Programa Principal

introducao()
menu()