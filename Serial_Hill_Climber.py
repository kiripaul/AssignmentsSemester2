import numpy
from scipy import *
import matplotlib.pyplot as plt
import random

def MatrixCreate(Rows,Columns):
    matrix_list = numpy.zeros(shape=(Rows,Columns))
    return matrix_list

'''
def MatrixRandomize(ArrayName):
    random.seed()
    arraySize = size(ArrayName)
    for element in range(arraySize):
        ArrayName[element] = random.random()
    return ArrayName  
'''
def MatrixRandomize(Array_Name):
    random.seed()
    array_size = len(Array_Name)
    element_size = (size(Array_Name))/array_size
    #element size determines the number of columns in each row by dividing the total number of items in the array/number of rows
    row = 0
    while(row<array_size):
        for column in range(element_size):
            Array_Name[row,column] = random.random()
        row = row+1
    return Array_Name
