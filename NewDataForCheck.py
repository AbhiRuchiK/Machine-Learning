import csv
import math
import numpy as np
RawData = open("autos.csv","r")
FormattedData = list(csv.reader(RawData))
#TrainingDataNormalized = set(list(map(list, zip(*FormattedData)))[11])

#print(TrainingDataNormalized)

#https://www.youtube.com/watch?v=eL_0Ok_Gkas
NecessaryData = []
NecessaryDataPrice = []
abtest=0
gearbox=0
vehicletype=0
yearofregistration=0
fueltype=0
#c=max(FormattedData[11])
#print(c)
for i in range(1,len(FormattedData)):
    
    #yearofregistration=(((2016-float(FormattedData[i][7]))*12) + (13-float(FormattedData[i][12])))
    BlankList=(float(FormattedData[i][11]))
    SquareListKM = [1, BlankList, math.pow(BlankList,2), math.pow(BlankList,3) , math.pow(BlankList,4), math.pow(BlankList,5), math.pow(BlankList,6)]
    NecessaryData.append(SquareListKM)
    NecessaryDataPrice.append(float(FormattedData[i][4]))    

TrainingData = NecessaryData[0:int(0.75*len(NecessaryData))]
MaxData = np.array(max(TrainingData))
TrainingData = np.array(TrainingData/ MaxData)

'''for i in range(len(TrainingData)):
    t=[]
    for j in range(len(TrainingData[i])):
        #square = TrainingData[i][j]*TrainingData[i][j]
        t.append(TrainingData[i][j])
        t.append(TrainingData[i][j]*TrainingData[i][j])
        #t.append(square)
    TrainingDataSquare.append(t)'''

TrainingDataPrice = NecessaryDataPrice[0:int(0.75*len(NecessaryData))]
MaxData = np.array(max(TrainingDataPrice))
TrainingDataPrice = np.array(TrainingDataPrice/ MaxData)
TrainingDataPrice = (TrainingDataPrice).T

TestingData = NecessaryData[(int(0.75*len(NecessaryData))):]
MaxData = np.array(max(TestingData))
TestingData = np.array(TestingData/MaxData)

TestingDataPrice = NecessaryDataPrice[(int(0.75*len(NecessaryData))):]
MaxData = max(TestingDataPrice)
TestingDataPrice = np.array(TestingDataPrice)
TestingDataPrice = (TestingDataPrice).T

#Thetas = np.random.randn(4)
Thetas=[2,3,4,5]
ThetasSquare = np.power(Thetas,2)
Epsilon = 0.0001
LR = 0.02
Lembda = 1

#Going to code for Differentiation of MSE with respect to theta1
for iteration in range(0,3):
    OldJ = 0
    NewJ = 0
    DJ = 0
   
    IntermediateResult = ( (ThetasSquare[0]) + (2 * (Thetas[0]* Thetas[1]) ) + ( ThetasSquare[2] + (2 * (Thetas[0] * Thetas[2]) ) )+( (2 * (Thetas[0] * Thetas[3]) ) + ( 2 * (Thetas[1] * Thetas[2] ) ) ) + ( (2 * (Thetas[1] * Thetas[3]) )  +  (2 * ThetasSquare[2] )  )+ ( 2 * (Thetas[2] * Thetas[3]) ) + (ThetasSquare[3]) )
    print(IntermediateResult)

    '''BlankList =[ ( (ThetasSquare[0]) ,
        (2 * (Thetas[0]* Thetas[1]) )  ,
        ( ThetasSquare[2] + (2 * (Thetas[0] * Thetas[2]) ) ) ,
        ( (2 * (Thetas[0] * Thetas[3]) ) + ( 2 * (Thetas[1] * Thetas[2] ) ) ) ,
        ( (2 * (Thetas[1] * Thetas[3]) )  +  (2 * ThetasSquare[2] )  ) ,
        ( 2 * (Thetas[2] * Thetas[3]) ) ,
        (ThetasSquare[3]) ) ]
    IntermediateResult=[]
    for i in range(len(TrainingData)):
        IntermediateResult.append(BlankList)

    OldJ = (np.dot(IntermediateResult, TrainingData))'''
    #s = np.size(CloseResult)
    #OldJ = (np.dot(CloseResult.T,CloseResult))+(Lembda*(np.dot(Thetas.T,Thetas)))/(s)  
   
    '''DJ = np.dot(2*(IntermediateResult).T,TrainingData)
    DJ = DJ/s
   
    Thetas = Thetas - (LR * (DJ.T))
    ThetasSquare = np.power(Thetas,2)   
    IntermediateResult = np.dot(TrainingData,Thetas)
    CloseResult = IntermediateResult - TrainingDataPrice
    s = np.size(CloseResult)    
    NewJ = (np.dot(CloseResult.T,CloseResult))+(Lembda*(np.dot(Thetas.T,Thetas)))/(s)
   
    if (abs(OldJ - NewJ)) < Epsilon:
        break
   
    print("The value of J at iteration number {} is {}".format(iteration,OldJ))  
   
print("The value of Theta0 star is {}".format(Thetas[0]))
print("The value of Theta1 star is {}".format(Thetas[1]))
print("The value of Theta2 star is {}".format(Thetas[2]))
print("The value of Theta3 star is {}".format(Thetas[3]))

TestingDataThetaStar = abs(np.dot(TestingData[3], Thetas.T) )
#print(TestingDataThetaStar)

PredictedPrice = np.dot(TestingDataThetaStar,MaxData)
print(PredictedPrice)
print(TestingDataPrice[3])
FinalPrice= PredictedPrice-TestingDataPrice[3]
print(FinalPrice)'''