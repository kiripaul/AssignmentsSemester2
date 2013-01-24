import numpy
from scipy import *
import matplotlib.pyplot as plt
import random
import copy


def MatrixCreate(Rows,Columns):
    #Inputs: int,int
    #Output: Array of zeroes
    
    matrix_list = numpy.zeros(shape=(Rows,Columns))
    return matrix_list

def MatrixRandomize(Array_Name):
    #Input: Array
    #Output: New Array
    random.seed()
    array_size = len(Array_Name)
    #len() gives the number of rows
    element_size = (size(Array_Name))/array_size
    #element_size determines the number of columns in each row by dividing the total number of items in the array/number of rows
    row = 0
    while(row<array_size):
        #looping through Rows
        for column in range(element_size):
            #looping through each column(element) in the row
            Array_Name[row,column] = random.random()
        row = row+1
    return Array_Name

def Fitness(Array_Name):
    #Input: Array
    #Output: N-by-1 Dimensional Array
    array_size = len(Array_Name)
    #len() gives the number of rows
    element_size = (size(Array_Name))/array_size
    #element_size determines the number of columns in each row
    row = 0
    vector_means = MatrixCreate(array_size,1)
    #vector_means will hold the means of each row
    while(row<array_size):
        for column in range(element_size):
            current_sum = sum(Array_Name[row,:])
            vector_mean = current_sum/element_size
            vector_means[row,0] = vector_mean
        row = row+1
    return vector_means

def MatrixPerturb(Array_Name,Probability):
    #Input: Array, Float
    #Output: Array
    array_rows = len(Array_Name)
    #len() gives the number of rows
    array_columns = (size(Array_Name))/array_rows
    #element_size determines the number of columns in each row
    prob_vector = MatrixCreate(array_rows,array_columns)
    #allocating space for new vector
    prob_vector[:,:] = Array_Name[:,:]
    #copying all of the elements from the matrix passed in to a new matrix
    row = 0
    random.seed()
    xx = random.random()
    while(row<array_rows):
        if(xx<Probability):
            prob_vector[row,(range(array_columns))] = random.random()
            #Assuuming that the array from the fitness function is passed in,
            #each row of the array will only have one element thus the indexing at 0
        xx = random.random()
        #re-generate the random number
        row += 1
    return prob_vector

def SerialHillClimber(Rows,Columns,Generations):
    Parent_Array = MatrixCreate(Rows,Columns)
    #:::
    Parent_Array = MatrixRandomize(Parent_Array)
    #:::
    Parent_Fitness = Fitness(Parent_Array)
    #Child_Fitness = MatrixCreate(Rows,1)
    #:::
    for cur_gen in range(Generations):
        print cur_gen, Parent_Fitness[0][0]
        Child_Array = MatrixPerturb(Parent_Array,0.05)
        Child_Fitness = Fitness(Child_Array)
        if(Child_Fitness > Parent_Fitness):
            Parent_Array = Child_Array
            Parent_Fitness = Child_Fitness
                
    
    
    
    
        
    

def testRun():
    arr = MatrixCreate(10,1)
    print arr
    print "RANDOMIZED"
    MatrixRandomize(arr)
    print arr
    jj = Fitness(arr)
    print "FITNESS"
    print jj
    ii = MatrixPerturb(jj,0.99)
    print "MATRIXPERTURB"
    print ii
    '''
    Parent_Array = MatrixCreate(10,1)
    Child = MatrixCreate(10,1)
    MatrixRandomize(Parent_Array)
    Parent_Fitness = Fitness(Parent_Array)
    for current_gen in range(8):
        print current_gen,Parent_Fitness[0][0]
        Child = MatrixPerturb(Parent_Array,0.05)
        Child_Fitness = Fitness(Child)
        if(Child_Fitness > Parent_Fitness):
            Parent_Array = Child
            Parent_Fitness = Child_Fitness
    '''
    
    
    
