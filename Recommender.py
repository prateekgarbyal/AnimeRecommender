import math
import sys
import csv
#import numpy as np

with open('anime.csv', 'r') as f:
    reader = csv.reader(f)
    anime_list = list(reader)
del anime_list[0]

with open('cleanedratings.csv', 'r') as f:
    reader = csv.reader(f)
    rating_list = list(reader)
print(rating_list[:20])

#ratingsmatrix=[[-1]*len(anime_list)]*73516
ratingsmatrix = [[-1]*len(anime_list) for _ in range(73516)]

#print(len(ratingsmatrix[100]))
#print(ratingsmatrix[0])
print(ratingsmatrix[0][0])

count=0
for x in range (0,len(rating_list)):
    #row=int(rating_list[x][0])-1
    #column=int(rating_list[x][1])
    #print (rating_list[x])
    #print(ratingsmatrix[0][0],int(rating_list[x][0])-1,int(rating_list[x][1]))
    ratingsmatrix[int(rating_list[x][0])-1][int(rating_list[x][1])]=int(rating_list[x][2])
    #print(row)
    #print(column)
    if ratingsmatrix[0][0] != -1:
        #print (row,column)
        print(rating_list[x])
        print(ratingsmatrix[0][0])
        print(ratingsmatrix[1][0])
        print(ratingsmatrix[2][0])
        a=input("stop")
print ("done")
#print(count)
#print((ratingsmatrix[0]))