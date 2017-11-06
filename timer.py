import csv
import math
import numpy as np
import time

RawData = open("autos.csv","r")
FormattedData = list(csv.reader(RawData))

NecessaryData = []
NecessaryDataPrice = []

tic = time.clock()
for i in range(1,len(FormattedData)):
    BlankList=[1,float(FormattedData[i][11]),float(FormattedData[i][9])]
    NecessaryData.append(BlankList)
    NecessaryDataPrice.append(float(FormattedData[i][4]))
    
toc = time.clock()
a= toc-tic
print(a)
    

TrainingData = NecessaryData[0:int(0.75*len(NecessaryData))]
TrainingData = np.array(TrainingData)
TestingData = NecessaryData[(int(0.75*len(NecessaryData))):]
TestingData = np.array(TestingData)
TrainingDataPrice = NecessaryDataPrice[0:int(0.75*len(NecessaryData))]
TrainingDataPrice = (np.array(TrainingDataPrice)).T
TestingDataPrice = NecessaryDataPrice[(int(0.75*len(NecessaryData))):]
TestingDataPrice = (np.array(TestingDataPrice)).T
    
Thetas = (np.array([5,5,5])).T

Epsilon = 0.0001
LR = 0.00000000005
#Going to code for Differentiation of MSE with respect to theta1


for iteration in range(0,50000):
    OldJ = 0
    NewJ = 0
    DJ = [0,0,0]
    
    #for i in range(0,len(TrainingData)):
        #OldJ = OldJ + math.pow((((Thetas[0]*TrainingData[i][0]) + (Thetas[1]*TrainingData[i][1]) + (Thetas[2]*TrainingData[i][2])) - TrainingData[i][3]),2)
    #OldJ = OldJ/len(TrainingData)
    
    
    IntermediateResult = np.dot(TrainingData,Thetas)
    CloseResult = IntermediateResult - TrainingDataPrice    
    IndividualSE = list(map(lambda x: math.pow(x,2),CloseResult))
    OldJ = sum(np.array(IndividualSE))
    
    
    #for j in range(1:len(DJ1)):
    for j in range(0,len(Thetas)):
        for i in range(0,len(TrainingData)):
            DJ[j] = DJ[j] + 2*TrainingData[i][j]*(((Thetas[0]*TrainingData[i][0])+(Thetas[1]*TrainingData[i][1])+(Thetas[2]*TrainingData[i][2]))-TrainingDataPrice[i])
        DJ[j] = DJ[j]/len(TrainingData)
        
    #DJ = D by DTheta1 of MSE evluated at theta1 = OldTheta1
    
    for i in range(0,len(Thetas)):    
        Thetas[i] = Thetas[i] - (LR * DJ[i])
        
    for i in range(0,len(TrainingData)):
        NewJ = NewJ + math.pow((((Thetas[0]*TrainingData[i][0]) + (Thetas[1]*TrainingData[i][1]) + (Thetas[2]*TrainingData[i][2])) - TrainingDataPrice[i]),2)
    NewJ = NewJ/len(TrainingData)
        
    if (abs(OldJ - NewJ)) < Epsilon:
        break
    
    print("The value of J at iteration number {} is {}".format(iteration,OldJ))   
    
print("The value of Theta0 star is {}".format(Thetas[0]))
print("The value of Theta1 star is {}".format(Thetas[1]))
print("The value of Theta2 star is {}".format(Thetas[2]))