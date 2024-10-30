'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 08/10/24
 ATIVIDADE: Atividade 02
 ROTEIRO: ROTEIRO_PYTHON_06
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_02_5162454_Hebert Lamounier Barbosa Júnior_10_10.py
'''

def mdc_euclides(a, b):
    if b == 0:
        return a
    else:
        return mdc_euclides(b, a%b)
    
print(f"{mdc_euclides(20,18)}")