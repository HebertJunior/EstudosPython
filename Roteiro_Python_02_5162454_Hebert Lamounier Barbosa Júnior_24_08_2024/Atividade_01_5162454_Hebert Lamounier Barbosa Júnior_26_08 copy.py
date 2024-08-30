'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 26/08/24
 ATIVIDADE: Atividade 01
 ROTEIRO: ROTEIRO_PYTHON_02
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_01_5162454_Hebert Lamounier Barbosa Júnior_26_08.py
'''

import random

numeros = random.sample(range(1, 101), 3)

print(f"Os números sorteados são: {numeros}")

menor = min(numeros)

maior = max(numeros)

maior2 = sum(numeros) - menor - maior

if maior + maior2 > menor:
    print("A soma dos dois maiores números é maior que o menor.")
else:
    print("A soma dos dois maiores números não é maior que o menor.")