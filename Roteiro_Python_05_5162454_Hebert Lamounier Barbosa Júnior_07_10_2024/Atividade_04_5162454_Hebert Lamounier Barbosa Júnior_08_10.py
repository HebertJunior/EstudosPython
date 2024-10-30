'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 08/10/24
 ATIVIDADE: Atividade 04
 ROTEIRO: ROTEIRO_PYTHON_05
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_04_5162454_Hebert Lamounier Barbosa Júnior_08_10.py
'''

def reps(lista):
    contagem = {}
    

    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
            

    resultado = []
    
 
    for elemento, count in contagem.items():
        if count >= 2:
            resultado.append(elemento)
    
    return resultado


lista = [1, 2, 3, 2, 4, 5, 1, 6, 7, 1]
resultado = reps(lista)
print(resultado)  

