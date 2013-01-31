import numpy
from scipy import *
import matplotlib.pyplot as plt
import random
from copy import deepcopy

################# ASSIGNMENT 3 #########################
def MatrixCreate(Rows,Columns):
    #Inputs: int,int
    #Output: Array of zeroes
    
    matrix_list = numpy.zeros(shape=(Rows,Columns))
    return matrix_list

def MatrixPerturb(Array_Name,Probability):
    #Input: Array, Float
    #Output: Array
    
    array_rows = len(Array_Name)
    #len() gives the number of rows
    array_columns = (size(Array_Name))/array_rows
    #element_size determines the number of columns in each row
    
    prob_vector = deepcopy(Array_Name)
    #copying all of the elements from the matrix passed in to a new matrix
    
    xx = random.random()
    for row in range(array_rows):
        for column in range(array_columns):
            if(xx<Probability):
                prob_vector[row,column] = random.uniform(-1,1)
                #Assuuming that the array from the fitness function is passed in,
                #each row of the array will only have one element thus the indexing at 0
            xx = random.uniform(-1,1)
        #print "RANDOM",row,xx
    return prob_vector

def MatrixRandomize(Array_Name):
    #Input: Array
    #Output: New Array
    random.seed()
    array_rows = len(Array_Name)
    #len() gives the number of rows
    array_columns = (size(Array_Name[0]))
    #element_size determines the number of columns in each row
    for row in range(array_rows):
        #looping through Rows
        for column in range(array_columns):
            #looping through each column(element) in the row
            Array_Name[row,column] = random.uniform(-1,1)
    return Array_Name

def VectorCreate(numNeurons):
    matrix_list = zeros(numNeurons,dtype=float)
    return matrix_list

def MeanDistance(v1,v2):
    dist = 0
    for i in range(len(v1)):
        dist += sum(pow(v1[i]-v2[i],2))
    dist = sqrt(dist)/sqrt(10)
    
    return dist

def PlotUpdate(parent):
    #Inputs: nothing
    #Outputs: Plots the strength of each neuron 
        
    jj = plt.imshow(parent, cmap=plt.get_cmap('gray'), aspect= 'auto',interpolation= 'nearest')
    plt.show(jj)


def Update(neuronValues,parent,i):
    for j in range(0,10):
        temp = 0
        for k in range(0,10):
            temp += parent[j][k]*neuronValues[i-1][k]

        if temp > 1:
            temp = 1
        elif temp < 0:
            temp = 0
        neuronValues[i][j] = temp

    return neuronValues


def Fitness(parent):
    neuronValues = numpy.zeros(shape=(10,10))
    for n in range(10):
        neuronValues[0][n] = 0.5

    for i in range(1,10):
        neuronValues = Update(neuronValues,parent,i)

    #print neuronValues
    #PlotUpdate(neuronValues)

    actualNeuronValues = neuronValues[9,:]
    
    desiredNeuronValues = VectorCreate(10)
    for j in range(0,10,2):
        desiredNeuronValues[j]=1
        
    d = MeanDistance(actualNeuronValues,desiredNeuronValues)
    fit = 1 - d
   
    return fit,neuronValues
    
def Main(Rows,Columns):
    parent = MatrixCreate(Rows,Columns)
    #:::
    parent = MatrixRandomize(parent)
    #:::
    
    parent_fitness,neuronValues = Fitness(parent)
   
    Fits = MatrixCreate(1,5000)
    #:::
    for cur_gen in range(5000):
        #print cur_gen, parent_fitness
        child = MatrixPerturb(parent,0.05)
        child_fitness,neuronValues = Fitness(child)
        for row in range(Rows):
            for column in range(Columns):
                if(child_fitness > parent_fitness):
                    parent = child
                    parent_fitness = child_fitness
                    
        Fits[0][cur_gen] = parent_fitness
    PlotUpdate(neuronValues)
    #return Fits

