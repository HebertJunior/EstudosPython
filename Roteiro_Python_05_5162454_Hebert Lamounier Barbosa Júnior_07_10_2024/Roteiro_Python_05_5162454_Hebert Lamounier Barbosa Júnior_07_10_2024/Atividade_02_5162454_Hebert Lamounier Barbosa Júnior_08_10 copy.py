'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 08/10/24
 ATIVIDADE: Atividade 02
 ROTEIRO: ROTEIRO_PYTHON_05
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_02_5162454_Hebert Lamounier Barbosa Júnior_08_10.py
'''

def prefixos(palavra1, palavra2):
    if palavra1 in palavra2:
        print("true")
        return True

    else:
        print("false")
        return False

p1 = input("Digite uma palavra:")
p2 = input("Digite outra palavra:")
prefixos(p1,p2)