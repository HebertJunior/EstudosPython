
'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 24/08/24
 ATIVIDADE: Trabalho_01
 ROTEIRO: Trabalho_01
 TURMA: (TERÇA)
 Nome do arquivo: Trabalho _1_5162454_Hebert Lamounier Barbosa Júnior_24_08.py
'''

def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("FIBONACCI DE NÚMEROS PRIMOS ###############################################")
n = int(input("Digite um valor de n para formar uma sequência de Fibonacci até ele: "))
lista = []

f1, f2 = 0, 1

while len(lista) < n:
    novo = f1 + f2
    f1, f2 = f2, novo
    if primo(novo):
        lista.append(novo)

if len(lista) >= n:
    print(f"Seu n-nésimo número fibonacci primo é: {lista[n-1]}")
else:
    print("-1")