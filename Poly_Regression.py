import csv
import numpy as np
RawData = open("autos.csv","r")
FormattedData = list(csv.reader(RawData))
#TrainingDataNormalized = set(list(map(list, zip(*FormattedData)))[11])

#print(TrainingDataNormalized)

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
    if FormattedData[i][5]=="test":
        abtest=1
    else:
        abtest=2
    if FormattedData[i][8]=="automatik":
        gearbox=1
    else:
        gearbox=2
    if FormattedData[i][6]=="coupe":
        vehicletype=1
    elif FormattedData[i][6]=="suv":
        vehicletype=2
    elif FormattedData[i][6]=="kleinwagen":
        vehicletype=3
    elif FormattedData[i][6]=="limousine":
        vehicletype=4
    elif FormattedData[i][6]=="cabrio":
        vehicletype=5
    elif FormattedData[i][6]=="bus":
        vehicletype=6
    elif FormattedData[i][6]=="kombi":
        vehicletype=7
    elif FormattedData[i][6]=="andere":
        vehicletype=8
    else:
        vehicletype=9
    
    if FormattedData[i][13]=="benzin":
        fueltype=1
    else:
        fueltype=2
    yearofregistration=(((2016-float(FormattedData[i][7]))*12) + (13-float(FormattedData[i][12])))
    BlankList=[1,float(FormattedData[i][11]),float(FormattedData[i][9]),abtest,gearbox,vehicletype,yearofregistration,fueltype]
    NecessaryData.append(BlankList)
    NecessaryDataPrice.append(float(FormattedData[i][4]))    

TrainingData = NecessaryData[0:int(0.75*len(NecessaryData))]
MaxData = np.array(max(TrainingData))
TrainingData = np.array(TrainingData/ MaxData)
TrainingDataSquare=[]

for i in range(len(TrainingData)):
    t=[]
    for j in range(len(TrainingData[i])):
        t.append(TrainingData[i][j])
        t.append(TrainingData[i][j]*TrainingData[i][j])
        
    TrainingDataSquare.append(t)

print(TrainingDataSquare[2])



TrainingDataPrice = NecessaryDataPrice[0:int(0.75*len(NecessaryData))]
MaxData = np.array(max(TrainingDataPrice))
TrainingDataPrice = np.array(TrainingDataPrice/ MaxData)
TrainingDataPrice = ((TrainingDataPrice))

TestingData = NecessaryData[(int(0.75*len(NecessaryData))):]
MaxData = np.array(max(TestingData))
TestingData = np.array(TestingData/MaxData)

TestingDataPrice = NecessaryDataPrice[(int(0.75*len(NecessaryData))):]
MaxData = max(TestingDataPrice)
TestingDataPrice = np.array(TestingDataPrice)
TestingDataPrice = (TestingDataPrice).T
print(TestingDataPrice)

Thetas = np.random.randn(8) 
Epsilon = 0.0001
LR = 0.02
Lembda = 1

#print(TrainingData)
#print(np.size(TrainingData),np.size(NecessaryData))
#Going to code for Differentiation of MSE with respect to theta1
for iteration in range(0,500):
    OldJ = 0
    NewJ = 0
    DJ = 0
    
    IntermediateResult = np.dot(TrainingData,Thetas)
    CloseResult = IntermediateResult - TrainingDataPrice
    s = np.size(CloseResult)    
    OldJ = (np.dot(CloseResult.T,CloseResult))+(Lembda*(np.dot(Thetas.T,Thetas)))/(s)  
   
    DJ = np.dot(2*(CloseResult).T,CloseResult)
    DJ = DJ/s

    print("\n value of DJ = {}".format(DJ))
    
    Thetas = Thetas - (LR * (DJ.T))
    
    IntermediateResult = np.dot(TrainingData,Thetas)
    CloseResult = IntermediateResult - TrainingDataPrice    
    NewJ = (np.dot(CloseResult.T,CloseResult))+(Lembda*(np.dot(Thetas.T,Thetas)))/(s)
    
    if (abs(OldJ - NewJ)) < Epsilon:
        break
   
    print("The value of J at iteration number {} is {}".format(iteration,OldJ))  
   
print("The value of Theta0 star is {}".format(Thetas[0]))
print("The value of Theta1 star is {}".format(Thetas[1]))
print("The value of Theta2 star is {}".format(Thetas[2]))
print("The value of Theta3 star is {}".format(Thetas[3]))
print("The value of Theta4 star is {}".format(Thetas[4]))
print("The value of Theta5 star is {}".format(Thetas[5]))
print("The value of Theta6 star is {}".format(Thetas[6]))
print("The value of Theta7 star is {}".format(Thetas[7]))

TestingDataThetaStar = abs(np.dot(TestingData[3], Thetas.T) )
#print(TestingDataThetaStar)

PredictedPrice = np.dot(TestingDataThetaStar,MaxData)
print(PredictedPrice)
print(TestingDataPrice[3])
FinalPrice= PredictedPrice-TestingDataPrice[3]
print(FinalPrice)