# -*- coding: utf-8 -*-

############# REFERENCIAS UTILIZADAS PARA IMPLEMENTACAO ###############################
#### https://www.aedb.br/seget/arquivos/artigos15/30522361.pdf
#### http://www.ufjf.br/mac/files/2012/11/Apostila_Res_Mat_outubro_2012-atualizada.pdf
####
#### https://github.com/edielsonpf/genetic-algorithm/
#### https://github.com/fandery/genetic_algorithms
#######################################################################################

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from genetic_algorithm.ga_numeric import genetic_algorithm
from BarraCoroaCircularEngastada import BarraCoroaCircularEngastada
import matplotlib.pyplot as plt

#Individuos e geracao
NumIndividuals = 50
IndividualSize = 22
MaxGeneration = 40

#Taxas
MutationRate = 0.008
CrossoverRate = 0.65

#Diametros
MinD = 51
MaxD = 99
Mind = 1
Maxd = 99

#Precisao e melhor escolha
Target = 0.00005
Elitism = True

problem = BarraCoroaCircularEngastada(MinD, MaxD, Mind, Maxd, IndividualSize)
ClassHandle  = genetic_algorithm(problem,MutationRate,Elitism,CrossoverRate)
fit,generation = ClassHandle.search(NumIndividuals, MaxGeneration, Target)

interaction=[i for i in range(generation)]
plt.plot(interaction,fit)
plt.show()  