import csv
import math
RawData = open("autos.csv","r")
FormattedData = list(csv.reader(RawData))

NecessaryData = []

for i in range(1,len(FormattedData)):
    BlankList = []
    BlankList.append(float(FormattedData[i][4]))
    BlankList.append(float(FormattedData[i][11]))
    NecessaryData.append(BlankList)
    
    TrainingData = NecessaryData[0:int(0.75*len(NecessaryData))]
    TestingData = NecessaryData[(int(0.75*len(NecessaryData))):]
    
OldTheta1 = 5
Epsilon = 0.0001
#Going to code for Differentiation of MSE with respect to theta1


for i in range(0,50000):
    OldJ = 0
    NewJ = 0
    DJ = 0
    
    for i in range(0,len(TrainingData)):
        OldJ = OldJ + math.pow(((OldTheta1*TrainingData[i][1]) - TrainingData[i][0]),2)
    OldJ = OldJ/len(TrainingData)
    
    for i in range(0,len(TrainingData)):
        DJ = DJ + 2*TrainingData[i][1]*((OldTheta1*TrainingData[i][1])-TrainingData[i][0])
    DJ = DJ/len(TrainingData)
        
    #DJ = D by DTheta1 of MSE evluated at theta1 = OldTheta1
        
    NewTheta1 = OldTheta1 - DJ
    
    for i in range(0,len(TrainingData)):
        NewJ = NewJ + math.pow(((NewTheta1*TrainingData[i][1]) - TrainingData[i][0]),2)
    NewJ = NewJ/len(TrainingData)
    
    OldTheta1 = NewTheta1
    
    if (abs(OldJ - NewJ)) < Epsilon:
        break