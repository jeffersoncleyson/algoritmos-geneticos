# -*- coding: utf-8 -*-

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from genetic_algorithm.ga_numeric import genetic_algorithm
from BarraCoroaCircularEngastada import BarraCoroaCircularEngastada
import matplotlib.pyplot as plt

NumIndividuals = 100
IndividualSize = 24
MutationRate = 0.008

problem = BarraCoroaCircularEngastada(IndividualSize)

MaxGeneration = 40
Target = 0.00001
Elitism = True

ClassHandle  = genetic_algorithm(problem,MutationRate,Elitism)

fit,generation = ClassHandle.search(NumIndividuals, MaxGeneration, Target)

interaction=[i for i in range(generation)]
plt.plot(interaction,fit)
plt.show()  