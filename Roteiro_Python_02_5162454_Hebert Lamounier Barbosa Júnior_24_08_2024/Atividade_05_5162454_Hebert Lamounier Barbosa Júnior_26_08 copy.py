'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 26/08/24
 ATIVIDADE: Atividade 05
 ROTEIRO: ROTEIRO_PYTHON_02
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_05_5162454_Hebert Lamounier Barbosa Júnior_26_08.py
'''
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]


jogadores = ['X', 'O']
jogador_atual = 0

def exibir_tabuleiro():
    print("|---|---|---|")
    for i, linha in enumerate(tabuleiro):
        print(f"| {linha[0]} | {linha[1]} | {linha[2]} |")
        print("|---|---|---|")

def verificar_vencedor():
   
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return tabuleiro[0][i]

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return tabuleiro[0][2]

    return None

def verificar_empate():
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    return True

print("Bem-vindo ao Jogo da Velha!")

while True:
    exibir_tabuleiro()
    jogador = jogadores[jogador_atual]
    print(f"\nJogador {jogador}, faça sua jogada.")

    try:
        linha = int(input("Digite a linha (0, 1, 2): "))
        coluna = int(input("Digite a coluna (0, 1, 2): "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros.")
        continue

    if 0 <= linha < 3 and 0 <= coluna < 3:
        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogador
        else:
            print("Espaço já ocupado, tente novamente.")
            continue
    else:
        print("Coordenadas inválidas, tente novamente.")
        continue

    vencedor = verificar_vencedor()
    if vencedor:
        exibir_tabuleiro()
        print(f"\nJogador {vencedor} venceu!")
        break

    if verificar_empate():
        exibir_tabuleiro()
        print("\nEmpate!")
        break

    
    jogador_atual = 1 - jogador_atual

