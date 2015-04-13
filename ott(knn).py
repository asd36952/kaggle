import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

PATH="C:\\Users\\SeongWooLim\\Desktop\\kaggle\\"

train=open(PATH+"train.csv","r")
test=open(PATH+"test.csv","r")

train_csv=csv.reader(train)
test_csv=csv.reader(test)

count=0
num1=0
num2=0
num3=0
num4=0
num5=0
num6=0
num7=0
num8=0
num9=0
Class_1=[0]*93
Class_2=[0]*93
Class_3=[0]*93
Class_4=[0]*93
Class_5=[0]*93
Class_6=[0]*93
Class_7=[0]*93
Class_8=[0]*93
Class_9=[0]*93

for i in train_csv:
    if count==0:
        count=count+1
        continue
    if(i[94]=="Class_1"):
        for j in range(1,94):
            Class_1[j-1]=Class_1[j-1]+int(i[j])
            num1=num1+1
    elif(i[94]=="Class_2"):
        for j in range(1,94):
            Class_2[j-1]=Class_2[j-1]+int(i[j])
            num2=num2+1
    elif(i[94]=="Class_3"):
        for j in range(1,94):
            Class_3[j-1]=Class_3[j-1]+int(i[j])
            num3=num3+1
    elif(i[94]=="Class_4"):
        for j in range(1,94):
            Class_4[j-1]=Class_4[j-1]+int(i[j])
            num4=num4+1
    elif(i[94]=="Class_5"):
        for j in range(1,94):
            Class_5[j-1]=Class_5[j-1]+int(i[j])
            num5=num5+1
    elif(i[94]=="Class_6"):
        for j in range(1,94):
            Class_6[j-1]=Class_6[j-1]+int(i[j])
            num6=num6+1
    elif(i[94]=="Class_7"):
        for j in range(1,94):
            Class_7[j-1]=Class_7[j-1]+int(i[j])
            num7=num7+1
    elif(i[94]=="Class_8"):
        for j in range(1,94):
            Class_8[j-1]=Class_8[j-1]+int(i[j])
            num8=num8+1
    elif(i[94]=="Class_9"):
        for j in range(1,94):
            Class_9[j-1]=Class_9[j-1]+int(i[j])
            num9=num9+1
        #print(i[1:93])
    count=count+1
    
for i in range(0,93):
    Class_1[i]=Class_1[i]/num1
    Class_2[i]=Class_2[i]/num2
    Class_3[i]=Class_3[i]/num3
    Class_4[i]=Class_4[i]/num4
    Class_5[i]=Class_5[i]/num5
    Class_6[i]=Class_6[i]/num6
    Class_7[i]=Class_7[i]/num7
    Class_8[i]=Class_8[i]/num8
    Class_9[i]=Class_9[i]/num9

Class=[Class_1,Class_2,Class_3,Class_4,Class_5,Class_6,Class_7,Class_8,Class_9]

def distance(data):
    result=[0]*9
    for j in range(0,9):
        for k in range(0,93):
            result[j]=result[j]+pow(int(data[k+1])-Class[j][k],2)
        result[j]=pow(result[j],0.5)
    return result

def normalize(dis):
    pro=[0]*9
    constant=max(dis)-min(dis)
    for i in range(len(dis)):
        pro[i]=(max(dis)-dis[i])/constant
    constant=sum(pro)
    for i in range(len(dis)):
        pro[i]=pro[i]/constant
    return pro

submit=open(PATH+"Submit.csv","w")
submit_csv=csv.writer(submit,delimiter=',',quotechar='|')
submit_csv.writerow(["id","Class_1","Class_2","Class_3","Class_4","Class_5","Class_6","Class_7","Class_8","Class_9"])
count=0
for i in test_csv:
    if count==0:
        count=count+1
        continue
    dist=distance(i)
    
    prob=normalize(dist)
    submit_csv.writerow([count]+prob)

   
    
    count=count+1
    
submit.close()
train.close()
test.close()

print("Finish!!!!")
