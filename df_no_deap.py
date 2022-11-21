import sys
import numpy as np
import pandas as pd
from numpy import random
from typing import Final
import matplotlib.pyplot as plt


products_table = pd.DataFrame.from_records([
    ['Banana 1u', 89, 1, 0, 23],
    ['Mandarin 1u', 40, 1, 0, 10],
    ['Ananas 100g', 50, 1, 0, 13],
    ['Grapes 100g',  76, 1, 0, 17],
    ['Chocolate 1 bar',  230, 3, 13, 25],
    ['Hard Cheese 100g', 350, 28, 26, 2],
    ['Soft Cheese 100g', 374, 18, 33, 1],
    ['Pesto 100g',  303, 3, 30, 4],
    ['Hoummous 100g', 306, 7, 25, 11],
    ['Aubergine Paste 100g', 228, 1, 20, 8],
    ['Protein Shake', 160, 30, 3, 5],
    ['Veggie Burger 1',220, 21, 12, 3],
    ['Veggie Burger 2', 165, 16, 9, 2],
    ['Boiled Egg', 155, 13, 11, 1],
    ['Backed Egg', 196, 14, 15, 1],
    ['Baguette Bread Half',274, 10, 0, 52],
    ['Square Bread 1 slice',  97, 3, 1, 17],
    ['Cheese Pizza 1u',  903, 36, 47, 81],
    ['Veggie Pizza 1u', 766, 26, 35, 85],
    ['Soy Milk 200ml', 115, 8, 4, 11],
    ['Soy Chocolate Milk 250ml', 160, 7, 6,20],
])
products_table.columns = ['Name', 'Calories', 'Gram_Prot', 'Gram_Fat', 'Gram_Carb']

#Quanto maior a lista mais balanceada será a dieta

#Função Objetivo
        #Obter uma lista balanceada com total de 17500 calorias
CALORIAS: Final[int] = 2500*7
#percentage_prot = 0.3
#percentage_carb = 0.5
#percentage_fat = 0.2
####################
#Criação do cromossomo
TAM_CROMO: Final[int] = 21
TAM_POP: Final[int] = TAM_CROMO * 2

#Criação da população
pop = np.zeros((TAM_POP, TAM_CROMO))
nova_pop = np.zeros((TAM_POP, TAM_CROMO))
pais = np.zeros((2, TAM_CROMO))
filhos = np.zeros((2, TAM_CROMO))
nota_pop = np.zeros((TAM_POP, 3))

def init_pop():
    global pop 
    pop = random.randint(low=0, high= 10, size=(TAM_POP, TAM_CROMO))
    #print(pop)


def avalia_pop():
    global nota_pop
    soma_apt = 0
    for i in range (TAM_POP):
       
        apt = 0
        for j in range(TAM_CROMO):
            #Eu preciso pegar a qttd de caloria do item * pelo valor da população
            #Em teoria seria algo como 
            # apt = products_table['Calories'].values[j] * pop[i][j] 
            # print(products_table['Calories'].values[j] * pop[i][j])
            apt = apt + ((products_table['Calories'].values[j] * pop[i][j] - CALORIAS)**2)
            print("%d + ((%d * %d) - %d)^2)" % (apt,products_table['Calories'].values[j],pop[i][j]))
            print("apt = %d" % (apt))
     
        nota_pop[i][0] = i
        nota_pop[i][1] = apt
        nota_pop[i][2] = -1
        soma_apt = soma_apt + apt
        print("nota_pop[i][0] = %d" % (i))
        print("nota_pop[i][1] = %d" % (apt))
        print("nota_pop[i][2] = -1")
        print("soma_apt = %d + %d" % (soma_apt, apt))
        print("==============================================")
    minsum = 0
    nota_pop = nota_pop[nota_pop[:, 1].argsort()]
    print(nota_pop)
    for i in range(TAM_POP):
        if(soma_apt > 0 ) and (nota_pop[i][1] > 0):
            nota_pop[i][2] = ((1 / nota_pop[i][1])/ soma_apt)*100
        else:
            nota_pop[i][2] = 0
        minsum = minsum + nota_pop[i][2] / minsum

    for i in range(TAM_POP):
        print(minsum)
        if(minsum > 0):
            nota_pop[i][2] = nota_pop[i][2] / minsum
        else:
            nota_pop[i][2] = 0
            
            
            

init_pop()
avalia_pop()