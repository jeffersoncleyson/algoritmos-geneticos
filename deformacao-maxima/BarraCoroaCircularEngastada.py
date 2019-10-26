import numpy as np
from math import pi as PI

class BarraCoroaCircularEngastada(object):

    def __init__(self,MinD, MaxD, Mind, Maxd, individual_size):
        self.MinD = MinD
        self.MaxD = MaxD
        self.Mind = Mind
        self.Maxd = MaxD
        self.individual_size = individual_size
        self.max_symbol = 1
        self.min_symbol = 0

        self.F = 2000
        self.L = 300

    '''
    @param self: 
    @param F: força aplicada em Newton
    @param L: Comprimento da barra engastada
    @param D: Diâmetro externo
    @param d: Diâmetro interno
    @param E: Módulo de Young
        Módulo de Young utilizado 2,05 x 10^5 N/mm²

    @return : Formula de deformação da estrutura
    '''
    def funcao_Deformacao(self, D, d):
        return (32 * self.F * self.L * D) / (2.065e5 * PI * (D**4 - d**4))

    def DReal(self, D):
        Precision = (self.MaxD - self.MinD)/((2.0**(self.individual_size/2)) - 1)
        return self.MinD+(Precision)*D
    
    def dReal(self, d):
        Precision = (self.Maxd - self.Mind)/((2.0**(self.individual_size/2)) - 1)
        return self.Mind+(Precision)*d

    '''
    @param num_individual: numero de individuos da população
    '''
    def initPopulation(self, num_individuals):

        population = []
        #Semente geradora
        randomWithSeed = np.random.RandomState(seed=0)
        #Create all individuals and then add an array population
        for i in range(num_individuals):
            individual = randomWithSeed.binomial(1,0.5,self.individual_size)
            population.append(individual.tolist())

        return population
    
    '''
        @param bin_x: representação binária
        @return : numero inteiro resultado da conversão
    '''
    def bin_to_dec(self,bin_x):
        s=''.join(str(x) for x in bin_x)
        return(int(s,2))

    def fitness(self,population):
        fitnessPop=[]
        #calculate the fitness for each individual of population
        for individual in population:
            calcFit = self.getFitness(individual)
            fitnessPop.append(calcFit)

        return fitnessPop

    def getFitness(self,individual):

        # size_div = self.individual_size/4

        # dec_ind_F = self.bin_to_dec(individual[:int(size_div)])
        # dec_ind_L = self.bin_to_dec(individual[int(size_div):int(2*size_div)])
        # dec_ind_D = self.bin_to_dec(individual[int(2*size_div):int(3*size_div)])
        # dec_ind_d = self.bin_to_dec(individual[int(3*size_div):])

        size_div = self.individual_size/2

        auxD = self.bin_to_dec(individual[:int(size_div)])
        auxd = self.bin_to_dec(individual[int(size_div):])

        dec_ind_D = self.DReal(auxD)
        dec_ind_d = self.dReal(auxd)

        
        fitness = self.funcao_Deformacao(dec_ind_D,dec_ind_d)
        

        return fitness


    def printSolution(self,solution):
        
        print('Solution:')

        print(solution)

        size_div = self.individual_size/2

        auxD = self.bin_to_dec(solution[:int(size_div)])
        auxd = self.bin_to_dec(solution[int(size_div):])

        dec_ind_D = self.DReal(auxD)
        dec_ind_d = self.dReal(auxd)



        print('F=%g'%self.F)
        print('L=%g'%self.L)
        print('D=%g'%dec_ind_D)
        print('d=%g'%dec_ind_d)
        print('f(F,L,D,d)=%g'%self.funcao_Deformacao(dec_ind_D,dec_ind_d)) 

    
    '''Getters and Setters'''
    def getIndividualSize(self):
        return self.individual_size
    
    def getMaxGeneSymbol(self):
        return self.max_symbol
    
    def getMinGeneSymbol(self):
        return self.min_symbol

    