'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 26/08/24
 ATIVIDADE: Atividade 03
 ROTEIRO: ROTEIRO_PYTHON_02
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_03_5162454_Hebert Lamounier Barbosa Júnior_26_08.py
'''
import math

distancia_a = float(input("Digite a distância entre o caçador e a árvore (Distância A): "))
distancia_b = float(input("Digite a distância entre o caçador e a caverna (Distância B): "))
distancia_c = float(input("Digite a distância entre o caçador e o farol (Distância C): "))

x = (distancia_a**2 + distancia_b**2 - distancia_c**2) / (2 * distancia_a)
y = math.sqrt(distancia_b**2 - x**2)

#formatação {variavel:.casaf}
print(f"Coordenadas do baú: X = {x:.2f} metros, Y = {y:.2f} metros")