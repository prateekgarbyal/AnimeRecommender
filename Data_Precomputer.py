import math
import sys
import csv
from scipy import spatial
#import numpy as np

with open('anime.csv', 'r') as f:
    reader = csv.reader(f)
    anime_list = list(reader)
del anime_list[0]

with open('cleanedratings.csv', 'r') as f:
    reader = csv.reader(f)
    rating_list = list(reader)
#del rating_list[0]
#print(rating_list[:20])

ratingsmatrix = [[-2]*len(anime_list) for _ in range(1000)]
#print(len(ratingsmatrix[100]))
#print(ratingsmatrix[0])
#print(ratingsmatrix[0][0])

#print(ratingsmatrix[0][0])
count=0
for x in range (0,len(rating_list)):
    row=int(rating_list[x][0])-1
    column=int(rating_list[x][1])
    ratingsmatrix[row][column]=int(rating_list[x][2])
    #print(row)
    #print(column)
#print(count)
#print((ratingsmatrix[0]))

average=[]
for x in range (0,len(ratingsmatrix)):
    count=0
    avg=0
    for y in ratingsmatrix[x]:
        if y!=-1 and y!=-2:
            avg=avg+y
            count=count+1
    if count==0:
        average.append(0)
    else:
        average.append(avg/count)

for x in range (0,len(ratingsmatrix)):
    for y in range (0,len(ratingsmatrix[x])):
        if ratingsmatrix[x][y]!=-2 and ratingsmatrix[x][y]!=-1:
            ratingsmatrix[x][y]=ratingsmatrix[x][y]-average[x]

for x in range(0,len(ratingsmatrix)):
    for y in range (0,len(ratingsmatrix[x])):
        #print(rrow,rcol)
        if ratingsmatrix[x][y]==-2:
            ratingsmatrix[x][y]=0
        elif ratingsmatrix[x][y]==-1:
            ratingsmatrix[x][y]=0.1
        else:
            ratingsmatrix[x][y]= ratingsmatrix[x][y]+0.1

similaritymatrix = [[-2]*1000 for _ in range(1000)]

for x in range(0,len(ratingsmatrix)):
    for y in range(0,len(ratingsmatrix)):
        if similaritymatrix[x][y]==-2:
            if x==y:
                similaritymatrix[x][y]=1
            else:
                result=1 - spatial.distance.cosine(ratingsmatrix[x], ratingsmatrix[y])
                similaritymatrix[x][y]=result
                similaritymatrix[y][x]=result
    #print(x)
#print(result)

with open("similarity.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(similaritymatrix)