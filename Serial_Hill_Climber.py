import numpy
from scipy import *
import matplotlib.pyplot as plt
import random

def MatrixCreate(Rows,Columns):
    matrix_list = numpy.zeros(shape=(Rows,Columns))
    return matrix_list

def MatrixRandomize(Array_Name):
    random.seed()
    array_size = len(Array_Name)
    #len() gives the number of rows
    element_size = (size(Array_Name))/array_size
    #element_size determines the number of columns in each row by dividing the total number of items in the array/number of rows
    row = 0
    while(row<array_size):
        for column in range(element_size):
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
    num_elem = 0
    while(row<array_size):
        for column in range(element_size):
            current_sum = sum(Array_Name[row,:])
            num_elem = num_elem + 1
        vector_mean = current_sum/num_elem
        vector_means[row,0] = vector_mean
        row = row+1
    return vector_means
