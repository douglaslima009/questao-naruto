#Aluno: Douglas Lima Menezes.
#ES1.

posicao_inicial_naruto = int(input("Digite a posição inicial do Naruto: "))
posicao_inicial_sasuke = int(input("Digite a posição inicial do Sasuke: "))
velocidade_cons_naruto = int(input("Digite a velocidade constante do Naruto: "))
velocidade_cons_sasuke = int(input("Digite a velocidade constante do Sasuke: "))

if posicao_inicial_naruto > posicao_inicial_sasuke:
        print("Naruto já está a frente do Sasuke.")
elif velocidade_cons_naruto <= velocidade_cons_sasuke:
    print("Sasuke chegou no esconderijo do Orochimaru")
else:
    tempo = (posicao_inicial_sasuke - posicao_inicial_naruto) / (velocidade_cons_naruto - velocidade_cons_sasuke)
    posicao_encontro = posicao_inicial_naruto + velocidade_cons_naruto * tempo
    print("Naruto e Sasuke vão se encontrar na posição:", posicao_encontro)