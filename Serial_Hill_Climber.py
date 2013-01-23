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
    element_size = size(Array_Name)
    for row in range(array_size):
        for element in range(element_size):
            Array_Name[row][element] = random.random()

    return Array_Name
