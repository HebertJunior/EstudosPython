'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 08/10/24
 ATIVIDADE: Atividade 07
 ROTEIRO: ROTEIRO_PYTHON_05
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_07_5162454_Hebert Lamounier Barbosa Júnior_08_10.py
'''

def contar_subs(palavra):
    c = 0
    v = "-"  
    palavra = list(palavra) 

    for i in range(len(palavra)): 
        palavra[i] = v 
        c += 1  

    print(c)  
    print(' '.join(palavra))  
       

p = "palavra"
contar_subs(p)
  
       
   




