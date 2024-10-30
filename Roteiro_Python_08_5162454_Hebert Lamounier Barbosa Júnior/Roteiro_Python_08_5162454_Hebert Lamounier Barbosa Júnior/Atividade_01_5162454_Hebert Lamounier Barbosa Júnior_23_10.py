'''
 RA: 5162454
 Hebert Lamounier Barbosa Júnior
 DATA: 23/10/24
 ATIVIDADE: Atividade 01
 ROTEIRO: ROTEIRO_PYTHON_08
 TURMA: TERÇA
'''

import matplotlib.pyplot as p
import pandas as pd
import math
import numpy as np

# Simulando alguns dados de vendas
dados = pd.date_range('20210101', periods=100)
vendas = pd.Series(range(100), index=dados)

p.figure(figsize=(10, 5))
p.plot(vendas.index, vendas.values)
p.title('Tendência de Vendas 2021')
p.xlabel('Data')
p.ylabel('Vendas')
p.grid(True)
p.show()


meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
vendas = [100, 200, 250, 555, 350, 700, 450, 400, 550, 200, 650, 700]
p.figure(figsize=(10, 5))
p.plot(meses, vendas, marker='o')
p.title('Vendas Mensais: ')
p.xlabel('Mês')
p.ylabel('Vendas')
p.grid(True)
p.show()


produtos = ['Produto A', 'Produto B', 'Produto C']
vendas = [300, 400, 600]
p.figure(figsize=(7, 4))
p.bar(produtos, vendas, color='blue')
p.title('Comparação de Vendas entre Produtos')
p.xlabel('Produtos')
p.ylabel('Vendas')
p.show()


horas_estudo = [10, 20, 30, 40, 50]
notas = [60, 65, 70, 80, 90]
p.figure(figsize=(8, 5))
p.scatter(horas_estudo, notas, color='red')
p.title('Relação entre Horas de Estudo e Notas')
p.xlabel('Horas de Estudo')
p.ylabel('Notas')
p.grid(True)
p.show()


# Dados para o gráfico
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3']
valores = [50, 70, 100]

p.bar(categorias, valores, color='skyblue')

p.title('Exemplo de Gráfico de Barras')
p.xlabel('Categorias')
p.ylabel('Valores')
p.show()

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 6, 8, 10]
y2 = [2, 2, 5, 10, 15]

p.plot(x, y1, label='Série 1')
p.plot(x, y2, label='Série 2')

p.legend()
p.title('Gráfico de Linhas com Múltiplas Séries')
p.xlabel('Eixo X')
p.ylabel('Eixo Y')
p.show()



angulo = math.radians(90) 
seno = math.sin(angulo) 
exponencial = math.exp(1) 
logaritmo = math.log(10) 


x = np.linspace(0, 2 * math.pi, 100)
y_seno = np.sin(x)
y_cosseno = np.cos(x)

p.figure(figsize=(10, 5))
p.plot(x, y_seno, label='seno')
p.plot(x, y_cosseno, label='cosseno')
p.title('Funções Seno e Cosseno')
p.xlabel('x (radianos)')
p.ylabel('Função')
p.legend()
p.grid(True)
p.show()


theta = np.linspace(0, 2 * np.pi, 100)
circle_x = np.cos(theta)
circle_y = np.sin(theta)

p.figure(figsize=(6, 6))
p.plot(circle_x, circle_y)
p.title('Círculo Trigonométrico')
p.axhline(0, color='black', linewidth=0.5)
p.axvline(0, color='black', linewidth=0.5)
p.grid(True)
p.axis('equal')
p.show()


x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
x = x[x != 0] 

seno = np.sin(x)
cosseno = np.cos(x)
tangente = np.tan(x)
secante = 1 / cosseno
cotangente = 1 / tangente
cossecante = 1 / seno

p.figure(figsize=(14, 10))

p.subplot(2, 3, 1)
p.plot(x, seno, label='Seno')
p.title('Função Seno')
p.axhline(0, color='black', linewidth=0.5)
p.axvline(0, color='black', linewidth=0.5)
p.grid(True)
p.ylim(-2, 2)

p.subplot(2, 3, 2)
p.plot(x, cosseno, label='Cosseno')
p.title('Função Cosseno')
p.axhline(0, color='black', linewidth=0.5)
p.axvline(0, color='black', linewidth=0.5)
p.grid(True)
p.ylim(-2, 2)

p.subplot(2, 3, 3)
p.plot(x, tangente, label='Tangente')
p.title('Função Tangente')
p.axhline(0, color='black', linewidth=0.5)
p.axvline(0, color='black', linewidth=0.5)
p.grid(True)
p.ylim(-10, 10)

p.subplot(2, 3, 4)
p.plot(x, secante, label='Secante')
p.title('Função Secante')
p.axhline(0, color='black', linewidth=0.5)
p.axvline(0, color='black', linewidth=0.5)
p.grid(True)
p.ylim(-10, 10)

p.subplot(2, 3, 5)
p.plot(x, cotangente, label='Cotangente')
p.title('Função Cotangente')
p.axhline(0, color='black', linewidth=0.5)
p.axvline(0, color='black', linewidth=0.5)
p.grid(True)
p.ylim(-10, 10)

p.subplot(2, 3, 6)
p.plot(x, cossecante, label='Cossecante')
p.title('Função Cossecante')
p.axhline(0, color='black', linewidth=0.5)
p.axvline(0, color='black', linewidth=0.5)
p.grid(True)
p.ylim(-10, 10)

p.tight_layout()
p.show()
