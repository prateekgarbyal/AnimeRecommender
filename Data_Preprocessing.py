import math
import sys
import csv
#import numpy as np

with open('anime.csv', 'r') as f:
    reader = csv.reader(f)
    anime_list = list(reader)
del anime_list[0]

animeid=[]
for x in range(0,len(anime_list)):
    animeid.append(int(anime_list[x][0]))
#print(animeid)
#print(max(animeid))
#print(animeid[1709])
#print(anime_list[1709][0])
with open('reducedratings.csv', 'r') as f:
    reader = csv.reader(f)
    rating_list = list(reader)
#del rating_list[0]

array=[-1]*36000
#print(array)
for x in range (0,len(animeid)):
    array[animeid[x]]=x
#print(array)

rating_list = [[int(j) for j in i] for i in rating_list]
temp=[]
for x in range(0, len(rating_list)):
    if rating_list[x][2]!=-1:
        temp.append(rating_list[x])

for x in range(0, len(rating_list)):
    rating_list[x][1]=array[rating_list[x][1]]
#print(rating_list[:20])

with open("cleanedratings.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(rating_list)

with open("supercleanedratings.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(temp)