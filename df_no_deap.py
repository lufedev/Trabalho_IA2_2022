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
CALORIAS_MIN: Final[int] = CALORIAS - (0.08*CALORIAS)
CALORIAS_MAX: Final [int] = (0.1*CALORIAS) + CALORIAS

########################################
R_prot = 0.3
R_carb = 0.5
R_fat = 0.2

prot_cal = 4
carb_cal = 4
fat_cal = 9

obj_prot = round(R_prot * CALORIAS) 
obj_carb = round(R_carb * CALORIAS)
obj_fat = round(R_fat * CALORIAS)
#####################################

#Criação do cromossomo
TAM_CROMO: Final[int] = 21
TAM_POP: Final[int] = 210

#Criação da população
pop = np.zeros((TAM_POP, TAM_CROMO))
nova_pop = np.zeros((TAM_POP, TAM_CROMO))
pais = np.zeros((2, TAM_CROMO))
filhos = np.zeros((2, TAM_CROMO))
nota_pop = np.zeros((TAM_POP, 5))



def imprime_melhor():
    print(">>> Melhor:")
    for i in range(TAM_CROMO):
        print(pop[nota_pop[0][0].astype(int)][i].astype(int), end=',')
    print(' - Nota: ', nota_pop[0][1],' - Macronutrientes: ',nota_pop[0][3], ' - (%): ', nota_pop[0][2])
    
def imprime_pior():
    print("\n>>> Pior:")
    for i in range(TAM_CROMO):
        print(pop[nota_pop[TAM_POP-1][0].astype(int)][i].astype(int), end=',')
    print(' - Nota: ', nota_pop[TAM_POP-1][1], ' - Macronutrientes: ',nota_pop[TAM_POP-1][3],' - (%): ', nota_pop[TAM_POP-1][2])
  
def imprime_medio():
    print("\n>>> Medio:")
    for i in range(TAM_CROMO):
        print(pop[nota_pop[((TAM_POP - 1) // 2)][0].astype(int)][i].astype(int), end=',')
    print(' - Nota: ', nota_pop[((TAM_POP - 1) // 2)][1],' - Macronutrientes: ',nota_pop[((TAM_POP - 1) // 2)][3], ' - (%): ', nota_pop[((TAM_POP - 1) // 2)][2])
 
def imprime_pop():
    print(pop)

def calc(x):
    return x - CALORIAS

def fitness (x):
    ans = calc(x)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)

def init_pop():
    # gerar pop
    global pop
    pop = random.randint(low=1, high= 10, size=(TAM_POP, TAM_CROMO))

def avalia_pop():
    global nota_pop
    for i in range (TAM_POP):
        apt = 0
        cals = 0
        apt_prot = 0
        apt_carb = 0
        apt_fat = 0
        for j in range(TAM_CROMO):

            #Acessar todos os cromossomos da população ex: pop[qual_pop][qual_cromossomo]
            #Multiplicar o valor do cromossomo pela qttd de calorias do item da lista que ocupa a mesma posição
            #Ex: valor = pop[qual_pop][1] * products_table['Calories'].values[1]
            #
            #Após multiplicar o valor, adicionar a um total dentro de uma variavel
            #Ex: a cada iteração do exemplo acima fazer -> tot_valor = tot_valor + valor
            #   
            #Feito isso, realizar o módulo da diferença entre o valor total e o total de calorias desejadas.
            #Quanto mais próximo de zero for essa diferença, melhor será o cromossomo.
            #Ex: nota = abs(tot_valor - CALORIAS)
            #print("%d + (%d * %d)" % (apt,products_table['Calories'].values[j],pop[i][j]))
            apt = apt + ((products_table['Calories'].values[j] * pop[i][j]))

            apt_prot = apt_prot + ((products_table['Gram_Prot'].values[j] * pop[i][j]))
            apt_carb = apt_carb + ((products_table['Gram_Carb'].values[j] * pop[i][j]))
            apt_fat = apt_fat + ((products_table['Gram_Fat'].values[j] * pop[i][j]))

        
        cals = (prot_cal * apt_prot) + (carb_cal * apt_carb) + (fat_cal * apt_fat)
        
        nota_pop[i][0] = i
        nota_pop[i][1] = apt
        nota_pop[i][3] = cals

def seleciona_pais():
    global pais
    max = 0
    timeout = 0
    max = sum([nota_pop[c][2] for c in range(TAM_POP)])
    selection_probs = [nota_pop[c][2]/max for c in range(TAM_POP)]
    pais[0] = pop[random.choice(range(TAM_POP), p=selection_probs)]
    pais[1] = pop[random.choice(range(TAM_POP), p=selection_probs)]
    while (pais[0] == pais[1]).all():
        pais[1] = pop[random.choice(range(TAM_POP), p=selection_probs)]
      
       

    # global pais
    
   
def cruza_pais():
    global filhos

    r_cruza = random.random_sample(size=None)
    if(r_cruza < 0.30):
        corte = random.randint(low=0, high=TAM_CROMO-1)   
        # print("Cruzamento Feito")
        filhos[0][:corte] = pais[0][:corte]
        filhos[0][corte:] = pais[1][corte:]
        filhos[1][corte:] = pais[0][corte:]
        filhos[1][:corte] = pais[1][:corte]
    else:
        # print("NÃO HOUVE CRUZAMENTO")
        filhos[0] = pais[0]
        filhos[1] = pais[1]
   
def muta_filhos():
    global filhos

    for i in range(TAM_CROMO):
        r_muta = random.random_sample(size=None)
        if(r_muta < 0.05):
            filhos[0][i] = random.randint(low=1,high=10)

    for i in range(TAM_CROMO):
        r_muta = random.random_sample(size=None)
        if(r_muta < 0.05):
            filhos[1][i] = random.randint(low=1,high=10)

def elitismo(melhor_pop):
    global nova_pop
    print(pop[nota_pop[0][0].astype(int)])
    nova_pop[0] = melhor_pop
    print("Cheguei aqui")
  

geracao = []
melhor = []
pior = []
medio = []

init_pop()
# imprime_pop()

for i in range(2000):

    #Começo da aviliação
    avalia_pop()

    #Sort Population
    for s in range(TAM_POP):
        # soma calorias - TOT_CALORIAS
        nota_pop[s][2] = fitness(nota_pop[s][1])
        
        # soma macronutrientes - TOT_CALORIAS
        nota_pop[s][4] = fitness(nota_pop[s][3])
        
    #nota_pop = nota_pop[np.lexsort((nota_pop[:,2], nota_pop[:,4]))]
    nota_pop = nota_pop[nota_pop[:, 2].argsort()]
    nota_pop =  nota_pop[::-1]
    #End sort
    
    #dados para graficos
    geracao.append(i)
    melhor.append(abs(calc(nota_pop[0][1])))
    pior.append(abs(calc(nota_pop[TAM_POP-1][1])))
    medio.append(abs(calc(nota_pop[(TAM_POP-1)//2][1])))

    print(f"\n === Gen {i} ===")
        
 
    # if (nota_pop[0][1] == CALORIAS):
    #     print("CHEGUEI AQUI DEU BOM")
    #     break

     #Critério de parada
    if ((nota_pop[0][1] == CALORIAS) and (nota_pop[0][3] >= CALORIAS_MIN and nota_pop[0][3] <= CALORIAS_MAX)):
        print("Solução encontrada")
        break

    #Imprime informação
    imprime_melhor()
    imprime_medio()
    imprime_pior()
    #preservar n melhores
    j = 0
    melhor_pop = pop[nota_pop[0][0].astype(int)]
    
    while(j < TAM_POP):
        # print("========SELECIONA PAIS=======")
        seleciona_pais()
        # print("========CRUZA PAIS=======")
        cruza_pais()
        muta_filhos()
        nova_pop[j] = filhos[0]
        nova_pop[j+1] = filhos[1]
        j = j + 2

    #elitismo(melhor_pop)
    
    pop = nova_pop.copy()
    nova_pop = np.zeros((TAM_POP, TAM_CROMO))


plt.title("CONVERGENCIA AG")
plt.plot(geracao, melhor, label = "Melhor")
plt.plot(geracao, pior, label = "Pior")
plt.plot(geracao, medio, label = "Medio")
plt.legend()
plt.show() 

   