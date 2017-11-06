import csv
import random
import numpy as n

RawData = open("autos.csv","r")
FormattedData = list(csv.reader(RawData))

NecessaryData = []
NecessaryDataPrice = []
abtest=0
for i in range(1,len(FormattedData)):
    if FormattedData[i][5]=="test":
        abtest=0
    else:
        abtest=1
    BlankList=[1,float(FormattedData[i][11]),float(FormattedData[i][9]),abtest]
    
    NecessaryData.append(BlankList)
    NecessaryDataPrice.append(float(FormattedData[i][4]))  

print(NecessaryData)
TrainingData = NecessaryData[0:int(0.75*len(NecessaryData))]

TrainingData = n.array(TrainingData)
print(TrainingData)
TestingData = NecessaryData[(int(0.75*len(NecessaryData))):]
TestingData = n.array(TestingData)

TrainingDataPrice = NecessaryDataPrice[0:int(0.75*len(NecessaryData))]
TrainingDataPrice = (n.array(TrainingDataPrice)).T
TestingDataPrice = NecessaryDataPrice[(int(0.75*len(NecessaryData))):]
TestingDataPrice = (n.array(TestingDataPrice)).T
    
Thetas = n.random.randn(3)

Epsilon = 0.0001
LR = 0.00000000005
#Going to code for Differentiation of MSE with respect to theta1

for iteration in range(0,50000):
    OldJ = 0
    NewJ = 0
    DJ = 0
    
    #for i in range(0,len(TrainingData)):
        #OldJ = OldJ + math.pow((((Thetas[0]*TrainingData[i][0]) + (Thetas[1]*TrainingData[i][1]) + (Thetas[2]*TrainingData[i][2])) - TrainingData[i][3]),2)
    #OldJ = OldJ/len(TrainingData)
    #print(TrainingData)
    IntermediateResult = n.dot(TrainingData,Thetas)
    #print(IntermediateResult)
    CloseResult = IntermediateResult - TrainingDataPrice
    s = n.size(CloseResult)    
    OldJ = (n.dot(CloseResult.T,CloseResult))/(s)   
    #print(IntermediateResult)
#    print(CloseResult)