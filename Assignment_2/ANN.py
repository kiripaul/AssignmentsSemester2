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
################# ASSIGNMENT 2 #########################
def CreateNeurons(Rows,Columns):
    #Inputs: int,int
    #Output: Rows-by-Columns array with random ints in first row
    neuron_values = MatrixCreate(Rows,Columns)

    random.seed()
    for column in range(Columns):
        neuron_values[0,column] = random.random()
    return neuron_values

def NeuronPositions(num_neurons):
    #Inputs: int
    #Output: 2-by-num_neurons Array; describes the x & y positions of neurons
    neuron_positions = MatrixCreate(2,num_neurons)
    angle = 0
    angle_update = (2*pi)/num_neurons
    for i in range(num_neurons):
        x = sin(angle)
        y = cos(angle)
        angle = angle + angle_update
        neuron_positions[0,i] = x
        neuron_positions[1,i] = y
    return neuron_positions

def PlotNeuronPos(num_neurons):
    # Plots Neuron Position
    neural_array = NeuronPositions(num_neurons)
    jj = plt.plot(neural_array[0],neural_array[1],'ko',markerfacecolor=[1,1,1],markersize=18)
    #plt.show(jj)
    return jj

def CreateSynapses(Row, Columns):
    #Inputs: int,int
    #Output: Rows-by-Columns array with random ints from -1 to 1 for each element
    syn = MatrixCreate(Row,Columns)
    for i in range(Row):
        for j in range(Columns):
            syn[i,j] = random.uniform(-1,1)
        
    return syn

def PlotNeuron_2(num_neurons):
    #Inputs: int
    #Outputs: Plots of neurons each connected: no weight to synapses

    neuron_positions = NeuronPositions(num_neurons)
    plt.plot(neuron_positions[0],neuron_positions[1],'ko',markerfacecolor=[1,1,1],markersize=18)
    #Plots just the markers

    columns = size(neuron_positions[0])
    #determines the number of columns in each row
    end = columns - 1
    for i in range(columns):
        for j in range(end):
            x1 = neuron_positions[0][i]
            x2 = neuron_positions[0][j+1]
            
            y1 = neuron_positions[1][i]
            y2 = neuron_positions[1][j+1]
            
            result = plt.plot([x1,x2],[y1,y2])
            
    #plt.show(result)
    return result

def PlotNeuron_2_Synapse(num_neurons):
    #Inputs: int
    #Outputs: Plots of neurons each connected: no weight to synapses

    neuron_positions = NeuronPositions(num_neurons)
    plt.plot(neuron_positions[0],neuron_positions[1],'ko',markerfacecolor=[1,1,1],markersize=18)
    #Plots just the markers
    
    #rows = len(neuron_positions)
    #determines the number of rows
    columns = size(neuron_positions[0])
    #determines the number of columns in each row
    end = columns - 1

    synapse = CreateSynapses(columns,columns)
    
    for i in range(columns):
        for j in range(end):
            x1 = neuron_positions[0][i]
            x2 = neuron_positions[0][j+1]
                
            y1 = neuron_positions[1][i]
            y2 = neuron_positions[1][j+1]
            if(synapse[i][j] < 0):
                result = plt.plot([x1,x2],[y1,y2],color=[.8,.8,.8])
                #result = plt.plot([x1,x2],[y1,y2],color=[.8,.8,.8],linewidth=(10*abs(synapse[i][j]))+1)
            else:
                result = plt.plot([x1,x2],[y1,y2],color=[0,0,0])
                #result = plt.plot([x1,x2],[y1,y2],color=[0,0,0],linewidth=(10*abs(synapse[i][j]))+1)

    plt.show(result)

def PlotNeuronWeight(num_neurons):
    #Inputs: int
    #Outputs: Plots of neurons each connected: no weight to synapses

    neuron_positions = NeuronPositions(num_neurons)
    plt.plot(neuron_positions[0],neuron_positions[1],'ko',markerfacecolor=[1,1,1],markersize=18)
    #Plots just the markers
    
    columns = size(neuron_positions[0])
    #determines the number of columns in each row
    end = columns - 1

    synapse = CreateSynapses(columns,columns)
    
    for i in range(columns):
        for j in range(end):
            x1 = neuron_positions[0][i]
            x2 = neuron_positions[0][j+1]
                
            y1 = neuron_positions[1][i]
            y2 = neuron_positions[1][j+1]
            if(synapse[i][j] < 0):
                w = int(10*abs(synapse[i][j]))+1
                result = plt.plot([x1,x2],[y1,y2],color=[.8,.8,.8],linewidth=w)
            else:
                w = int(10*abs(synapse[i][j]))+1
                result = plt.plot([x1,x2],[y1,y2],color=[0,0,0],linewidth=w)

    plt.show(result)
    
def Update(neuronValues,synapses,i):
    for j in range(0,10):
        temp = 0
        for k in range(0,10):
            temp += synapses[j][k]*neuronValues[i-1][k]

        if temp > 1:
            temp = 1
        elif temp < 0:
            temp = 0
        neuronValues[i][j] = temp
    return neuronValues

def PlotUpdate():
    #Inputs: nothing
    #Outputs: Plots the strength of each neuron 
    neuronValues = CreateNeurons(50,10)
    synapses = CreateSynapses(10,10)
    for i in range(1,50):
        neuronValues = Update(neuronValues,synapses,i)
        
    jj = plt.imshow(neuronValues, cmap=plt.get_cmap('gray'), aspect= 'auto',interpolation= 'nearest')
    plt.show(jj)
    



            
    
