import numpy
from scipy import *
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import random
from copy import deepcopy

################# ASSIGNMENT 3 #########################
def Fitness(parent):
    neuronValues = numpy.zeros(shape=(10,10))
    neuronValues = neuronValues[0]
    for n in range(10):
        neuronValues[n] = 0.5

    for i in range(1,10):
        neuronValues = Update(neuronValues,parent,i)

    actualNeuronValues = neuronValues[9,:]
    
    desiredNeuronValues = VectorCreate(10)
    for j in range(0,10,2):
        desiredNeuronValues[j]=1
        
    d = MeanDistance(actualNeuronValues,desiredNeuronValues)
    fit = 1 - d
   
    return fit,neuronValues

def MatrixCreate(Rows,Columns):
    
    matrix_list = np.zeros((Rows,Columns))
    return matrix_list

def MatrixPerturb(Array_Name,Probability):
    
    array_rows = len(Array_Name)
    array_columns = (len(Array_Name[0]))
    
    prob_vector = deepcopy(Array_Name)
    
    for row in range(array_rows):
        for column in range(array_columns):
            if(random.random()<Probability):
                prob_vector[row,column] = random.uniform(-1,1)
    return prob_vector

def MatrixRandomize(Array_Name):
    random.seed()
    array_rows = len(Array_Name)
    array_columns = (size(Array_Name[0]))
    for row in range(array_rows):
        for column in range(array_columns):
            Array_Name[row,column] = random.uniform(-1,1)
    return Array_Name

def VectorCreate(numNeurons):
    matrix_list = zeros((numNeurons),dtype='f')
    return matrix_list

def MeanDistance(v1,v2):
    dist = 0
    for i in range(len(v1)):
        dist += sum(pow(v1[i]-v2[i],2))
    dist = sqrt(dist)/sqrt(10)
    
    return dist

def PlotUpdate(parent):
    plt.imshow(parent, cmap=cm.gray, aspect= 'auto',interpolation= 'nearest')
    plt.show()
    
def PlotVectorAsLine(parent):
    parent = parent[0]
    plt.plot(parent)
    #plt.ylim(0,1.1)
    plt.show()

def Update(temper,synapses,i):
    numcol = len(temper[0])
    for j in range(numcol):
        temp = 0
        for k in range(0,9):
            temp += temper[i-1,k]*synapses[j,k]

        if(temp > 1):
            temp = 1
        elif(temp < 0):
            temp = 0
        temper[i][j] = temp
    return temper


def Fitness2(synapses):
    temper = np.zeros((10,10))
    for n in range(10):
        temper[0,n] = 0.5
        
    for i in range(1,10):
        neuronValues = Update(temper,synapses,i)

    diff=0.0
    for i in range(0,9):
        for j in range(0,9):
            diff= diff + abs(neuronValues[i,j]-neuronValues[i,j+1])
            diff= diff + abs(neuronValues[i+1,j]-neuronValues[i,j])

    diff=diff/(2*9*9)

    return diff,neuronValues

    
def Main(Rows,Columns):
    parent = MatrixCreate(Rows,Columns)
    #:::
    parent = MatrixRandomize(parent)
    #:::
    
    parent_fitness,neuronValues = Fitness2(parent)

    #PlotUpdate(neuronValues)
   
    Fits = MatrixCreate(1,1000)
    Fits = Fits[0,:]
    #:::
    for cur_gen in range(1000):
        #print cur_gen, parent_fitness
        Fits[cur_gen] = parent_fitness
        child = MatrixPerturb(parent,0.05)
        child_fitness,neuronValues = Fitness2(child)
        if(child_fitness > parent_fitness):
            parent = deepcopy(child)
            parent_fitness = child_fitness

        Fits[cur_gen] = parent_fitness
        

    PlotUpdate(neuronValues)
    plt.plot(Fits)
    plt.show()

def SupaMain(runs):
    for i in range(runs):
        Main(10,10)
        print i

    print "finished"

