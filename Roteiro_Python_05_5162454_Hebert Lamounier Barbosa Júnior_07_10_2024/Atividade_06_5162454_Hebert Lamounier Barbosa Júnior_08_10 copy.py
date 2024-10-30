'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 08/10/24
 ATIVIDADE: Atividade 06
 ROTEIRO: ROTEIRO_PYTHON_05
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_06_5162454_Hebert Lamounier Barbosa Júnior_08_10.py
'''

def letra_na_string(palavra, letra):
    
   c = 0
   if palavra is not None:
        for letra in palavra:
            c += 1
            
        print(f"Na palavra '{palavra}' a letra: '{letra}', aparece {c} vezes")
  
p = input("Digite uma palavra:")     
l = input("Digite uma letra: ")

letra_na_string(p, l)
            
  
       
   




