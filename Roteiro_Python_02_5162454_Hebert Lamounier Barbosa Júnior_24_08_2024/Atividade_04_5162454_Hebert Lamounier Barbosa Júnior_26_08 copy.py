'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 26/08/24
 ATIVIDADE: Atividade 04
 ROTEIRO: ROTEIRO_PYTHON_02
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_04_5162454_Hebert Lamounier Barbosa Júnior_26_08.py
'''
palavra = ["p", "y", "t", "h", "o", "n"]
vidas = 6
letras_corretas = []
letras_erradas = []

print("BEM-VINDO AO JOGO DA FORCA!\nDigite 1 para começar o jogo e 0 para sair: ")
op = int(input(": "))

if op == 0:
    quit()
elif op == 1:
    print("Digite uma letra:")
    print("DICA! A palavra tem 6 letras!")

    while vidas > 0:
        progresso = [letra if letra in letras_corretas else "_" for letra in palavra]
        print(" ".join(progresso))

        if progresso == palavra:
            print("Parabéns! Você acertou a palavra!\n\n")
            break

        letra = input("Digite uma letra: ")
        letra = letra.lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já escolheu essa letra")
            print('\n\n\n')
        elif letra in palavra:
            print("A letra está na palavra!")
            letras_corretas.append(letra)
            print('\n\n\n')
        else:
            print("A letra não está na palavra!")
            letras_erradas.append(letra)
            print('\n\n\n')
            vidas -= 1
            print(f"Você ainda tem {vidas} vidas.")
            print('\n\n\n')

        # Verificar se o jogador perdeu
        if vidas == 0:
            print("Você perdeu! A palavra era:", "".join(palavra))
            print('\n\n\n')
            