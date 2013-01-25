import numpy
from scipy import *
import matplotlib.pyplot as plt
import random
from copy import deepcopy


def MatrixCreate(Rows,Columns):
    #Inputs: int,int
    #Output: Array of zeroes
    
    matrix_list = numpy.zeros(shape=(Rows,Columns))
    return matrix_list

def MatrixRandomize(Array_Name):
    #Input: Array
    #Output: New Array
    random.seed()
    array_rows = len(Array_Name)
    #len() gives the number of rows
    array_columns = (size(Array_Name))/array_rows
    #element_size determines the number of columns in each row
    for row in range(array_rows):
        #looping through Rows
        for column in range(array_columns):
            #looping through each column(element) in the row
            Array_Name[row,column] = random.random()
    return Array_Name

def Fitness(Array_Name):
    #Input: Array
    #Output: N-by-1 Dimensional Array
    array_row = len(Array_Name)
    #len() gives the number of rows
    array_column = (size(Array_Name))/array_row
    #element_size determines the number of columns in each row
    vector_means = MatrixCreate(array_row,1)
    #vector_means will hold the means of each row
    for row in range(array_row):
        current_sum = sum(Array_Name[row,:])
        vector_mean = current_sum/array_column
        vector_means[row,0] = vector_mean            
    return vector_means

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
                prob_vector[row,column] = random.random()
                #Assuuming that the array from the fitness function is passed in,
                #each row of the array will only have one element thus the indexing at 0
            xx = random.random()
        #print "RANDOM",row,xx
    return prob_vector

def SerialHillClimber(Rows,Columns,Generations):
    Parent_Array = MatrixCreate(Rows,Columns)
    #:::
    Parent_Array = MatrixRandomize(Parent_Array)
    #:::
    Parent_Fitness = Fitness(Parent_Array)
    Fits = MatrixCreate(Generations,1)
    #:::
    for cur_gen in range(Generations):
        #print "PARENT FITNESS", Parent_Fitness[0][0]
        #print cur_gen, Parent_Fitness[0][0]
        Child_Array = MatrixPerturb(Parent_Array,0.05)
        Child_Fitness = Fitness(Child_Array)
        #print "CHILD FITNESS",Child_Fitness[0][0]
        for row in range(Rows):
            for column in range(Columns):
                if(Child_Fitness > Parent_Fitness):
                    Parent_Array = Child_Array
                    Parent_Fitness = Child_Fitness
                    
        Fits[cur_gen] = Parent_Fitness
        
    return Fits
    
def PlotVectorAsLine(Array_Name):
    plotted_results = plt.plot(Array_Name)
    return plotted_results

def PlotHC(Rows,Columns,Generations,Lineages):
    for yy in range(0,Lineages):
        graph_me = SerialHillClimber(Rows,Columns,Generations)
        ii = PlotVectorAsLine(graph_me)   
    plt.show(ii)

def Genes(Rows,Columns,Generations):
    genes = MatrixCreate(Columns,Generations)
    #:::
    Parent_Array = MatrixCreate(Rows,Columns)
    #:::
    Parent_Array = MatrixRandomize(Parent_Array)
    #:::
    Parent_Fitness = Fitness(Parent_Array)
    #:::
    Fits = MatrixCreate(Generations,1)
    #:::
    for cur_gen in range(Generations):
        Child_Array = MatrixPerturb(Parent_Array,0.05)
        Child_Fitness = Fitness(Child_Array)
        for row in range(Rows):
            for column in range(Columns):
                if(Child_Fitness > Parent_Fitness):
                    Parent_Array = Child_Array
                    Parent_Fitness = Child_Fitness          
                genes[column][cur_gen] = Parent_Array[row][column]
                
    jj = plt.imshow(genes, cmap=plt.get_cmap('gray'), aspect= 'auto',interpolation= 'nearest')
    plt.show(jj)

def testRun():
    arr = MatrixCreate(2,10)
    print arr
    print "RANDOMIZED"
    MatrixRandomize(arr)
    print arr
    jj = Fitness(arr)
    print "FITNESS"
    print jj
    ii = MatrixPerturb(arr,0.5)
    print "MATRIXPERTURB"
    print ii
    print arr == ii
    
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
    
    
    
