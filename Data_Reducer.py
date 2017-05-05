import math
import sys
import csv

with open('rating.csv', 'r') as f:
    reader = csv.reader(f)
    rating_list = list(reader)
del rating_list[0]

updated=[]
for x in range(0,len(rating_list)):
    if int(rating_list[x][0])<=1000:
        updated.append(rating_list[x])

with open("reducedratings.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(updated)