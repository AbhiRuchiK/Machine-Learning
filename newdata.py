import csv
import math
import numpy as np
 
RawData = open("autos.csv","r")
FormattedData = list(csv.reader(RawData))
 
NecessaryData = []
NecessaryDataPrice = []
abtest=0
c=max(FormattedData[11])
print(c)
for i in range(1,len(FormattedData)):
    if FormattedData[i][5]=="test":
        abtest=0
    else:
        abtest=1
    BlankList=[1,float(FormattedData[i][11]),math.pow(float(FormattedData[i][11]),2),abtest]
    NecessaryData.append(BlankList)
    NecessaryDataPrice.append(float(FormattedData[i][4]))    

TrainingData = NecessaryData[0:int(0.75*len(NecessaryData))]
TrainingData = np.array(TrainingData)
TestingData = NecessaryData[(int(0.75*len(NecessaryData))):]
TestingData = np.array(TestingData)
TrainingDataPrice = NecessaryDataPrice[0:int(0.75*len(NecessaryData))]
TrainingDataPrice = (np.array(TrainingDataPrice)).T
TestingDataPrice = NecessaryDataPrice[(int(0.75*len(NecessaryData))):]
TestingDataPrice = (np.array(TestingDataPrice)).T

Thetas = np.random.randn(3)
 
Epsilon = 0.0001
LR = 0.00000000005
#print(TrainingData)
#print(np.size(TrainingData),np.size(NecessaryData))

#Going to code for Differentiation of MSE with respect to theta1
for iteration in range(0,50):
    OldJ = 0
    NewJ = 0
    DJ = 0
   
    IntermediateResult = np.dot(TrainingData,Thetas)
    #print(IntermediateResult)
    CloseResult = IntermediateResult - TrainingDataPrice
    s = np.size(CloseResult)    
    OldJ = (np.dot(CloseResult.T,CloseResult))/(s)  
   
    DJ = np.dot(2*(CloseResult).T,TrainingData)
    DJ = DJ/s
   
    Thetas = Thetas - (LR * (DJ.T))
       
    IntermediateResult = np.dot(TrainingData,Thetas)
    CloseResult = IntermediateResult - TrainingDataPrice
    s = np.size(CloseResult)    
    NewJ = (np.dot(CloseResult.T,CloseResult))/(s)
   
    if (abs(OldJ - NewJ)) < Epsilon:
        break
   
    print("The value of J at iteration number {} is {}".format(iteration,OldJ))  
   
print("The value of Theta0 star is {}".format(Thetas[0]))
print("The value of Theta1 star is {}".format(Thetas[1]))
print("The value of Theta2 star is {}".format(Thetas[2]))