'''
 RA: Hebert Lamounier Barbosa Júnior
 DATA: 24/08/24
 ATIVIDADE: Atividade 12
 ROTEIRO: ROTEIRO_PYTHON_01
 TURMA: (TERÇA)
 Nome do arquivo: Atividade_12_5162454_Hebert Lamounier Barbosa Júnior_24_08.py
'''
print("CALCULADORA IMC")
altura = float(input("Digite sua altura em metros:"))
peso = float(input("Digite seu peso:"))

if altura < 300 and peso > 1:
    print("Seus dados foram validados")
    imc = peso / (altura * altura)
    print(imc)
    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc <= 24.9:
        print("Peso normal")
    elif 25.0 <= imc <= 29.9:
        print("Excesso de peso")
    elif 30.0 <= imc <= 34.9:
        print("Obesidade grau 1")   
    elif 35.0 <= imc <= 39.9:
        print("Obesidade grau 2")
    elif imc >= 40.0:
        print("Obesidade grau 3")            
else:
    print("Digite valores válidos")




 




