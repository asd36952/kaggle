import csv
import numpy as np
import matplotlib.pyplot as plt
import theano

PATH="C:\\Users\\SeongWooLim\\Desktop\\kaggle\\"

train=open(PATH+"train.csv","r")
test=open(PATH+"test.csv","r")

train_csv=csv.reader(train)
test_csv=csv.reader(test)


train.close()
test.close()

print("Finish!!!!")
