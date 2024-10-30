'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 08/10/24
 ATIVIDADE: Atividade 08
 ROTEIRO: ROTEIRO_PYTHON_05
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_08_5162454_Hebert Lamounier Barbosa Júnior_08_10.py
'''

def lista_e_limites(lista,li,ls):
    a = 0
    t = len(lista)
    lista.sort()
    listai = []
    listas = []
    
    while a < t:
        if lista[a] <= li:
            listai.append(lista[a])
        if lista[a] >= ls:
            listas.append(lista[a])
        a += 1
        
    print(f"Lista: {lista}")
    print(f"Lista com limite superior: {listas}")
    print(f"Lista com limite inferior: {listai}")

lista = [1,2,3,4,6,7,8]
l1 = int(input("Digite o limite inferior da lista  "))
l2 = int(input("Digite o limite superior da lista  "))

lista_e_limites(lista,l1,l2)