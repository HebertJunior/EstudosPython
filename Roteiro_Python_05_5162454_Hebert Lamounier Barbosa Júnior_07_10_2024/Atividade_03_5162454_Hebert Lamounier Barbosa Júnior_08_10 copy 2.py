'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 08/10/24
 ATIVIDADE: Atividade 03
 ROTEIRO: ROTEIRO_PYTHON_05
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_03_5162454_Hebert Lamounier Barbosa Júnior_08_10.py
'''

def calculo_10(valor_total):
    
    if valor_total > 0:
        t = valor_total #guarda o total
        valor_total = valor_total * 10/100
        g = valor_total
        valor_total = g + t
        
        print(f"O valor total sem os 10% é: R${round(t,2)}")
        print(f"Os 10% resultaram em: R${round(g,2)}")
        print(f"O valor total é de: R${round(valor_total,2)}")
        
    else:
        print("O valor total da compra está zerado")


total = float(100.67)
calculo_10(total)

