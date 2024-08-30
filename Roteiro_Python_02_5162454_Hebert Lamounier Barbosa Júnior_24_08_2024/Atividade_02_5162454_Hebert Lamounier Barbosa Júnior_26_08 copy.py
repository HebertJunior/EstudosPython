'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 26/08/24
 ATIVIDADE: Atividade 02
 ROTEIRO: ROTEIRO_PYTHON_02
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_02_5162454_Hebert Lamounier Barbosa Júnior_26_08.py
'''


destroyer = [2]  
porta_avi = [8, 9]  
encouracado = [4, 5]

# Vidas
encouracado_vida = 3
porta_avi_vida = 2
destroyer_vida = 1

# Início do jogo
print("Digite 1 para iniciar o jogo e 0 para sair:")
op = int(input())

if op == 0:
    quit()
elif op == 1:
    print("===========================================")
    print("Bem-vindo(a) à batalha naval!\nEscolha uma posição de 1 a 10 ou 0 para sair. Boa sorte!")

    while True:
        p = int(input("Escolha uma posição: "))

        if p == 0:
            print("Até logo!")
            break
        elif p < 1 or p > 10:
            print("Escolha uma posição de 1 a 10.")
        else:
            p -= 1 

            if p in destroyer:
                print("Navio atingido!")
                destroyer.remove(p)
                if not destroyer:
                    print("Navio afundado!")
            elif p in porta_avi:
                print("Navio atingido!")
                porta_avi.remove(p)
                if not porta_avi:
                    print("Navio afundado!")
            elif p in encouracado:
                print("Navio atingido!")
                encouracado.remove(p)
                if not encouracado:
                    print("Navio afundado!")
            else:
                print("Água!")

            if not (destroyer or porta_avi or encouracado):
                print("Parabéns! Você venceu a batalha naval!")
                break
else:
    print("Digite uma opção válida")   
    