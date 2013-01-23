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
    array_size = len(Array_Name)
    #len() gives the number of rows
    element_size = (size(Array_Name))/array_size
    #element_size determines the number of columns in each row by dividing the total number of items in the array/number of rows
    row = 0
    vector_means = MatrixCreate(array_size,1)
    #vector_means will hold the means of each row: it is set up so that it can work with multidimensional matrices
    num_elem = 0
    while(row<array_size):
        for column in range(element_size):
            current_sum = sum(Array_Name[row,:])
            num_elem = num_elem + 1
        vector_mean = current_sum/num_elem
        vector_means[row,0] = vector_mean
        row = row+1
    return vector_means

def MatrixPerturb(Array_Name,Probability):
    random.seed()
    array_size = len(Array_Name)
    #len() gives the number of rows
    element_size = (size(Array_Name))/array_size
    #element_size determines the number of columns in each row by dividing the total number of items in the array by the number of rows
    prob_vector = MatrixCreate(array_size,element_size)
    #allocating space for new vector
    prob_vector = copy.deepcopy(Array_Name)
    #copying all of the elements from the matrix passed in to a new matrix, prob_vector

    xx = random.random()
    row = 0

    while(row<array_size):
        if(xx<Probability):
            prob_vector[row,0] = random.random()
            #Assuuming that the array from the fitness function is passed in,
            #each row of the array will only have one element thus the indexing at 0
        xx = random.random()
        #re-generate the random number
        row += 1
    return prob_vector

def testRun():
    arr = MatrixCreate(10,1)
    print arr
    print "RANDOMIZED"
    MatrixRandomize(arr)
    print arr
    jj = Fitness(arr)
    print "FITNESS"
    print jj
    ii = MatrixPerturb(jj,0.5)
    print "MATRIXPERTURB"
    print ii
    
    
