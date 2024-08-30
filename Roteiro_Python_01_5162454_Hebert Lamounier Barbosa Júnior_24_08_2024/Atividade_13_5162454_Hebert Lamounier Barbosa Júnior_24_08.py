'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 24/08/24
 ATIVIDADE: Atividade 13
 ROTEIRO: ROTEIRO_PYTHON_01
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_13_5162454_Hebert Lamounier Barbosa Júnior_24_08.py
'''
import random
import string
tamanho = int(input("O digite o tamanho da senha deejada entre 8 e 16: "))
caracteres = string.ascii_letters + string.punctuation

senha = ''.join(random.choice(caracteres) for i in range(tamanho))

print(senha)




 




