import math
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import collections
from itertools import groupby
#from numpy  import array
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
with open('rating.csv', 'r') as f:
    reader = csv.reader(f)
    rating_list = list(reader)
del rating_list[0]

with open('cleanedratings.csv', 'r') as f:
    reader = csv.reader(f)
    ratingcleaned_list = list(reader)

ratingdist=[]
for x in range(0,len(rating_list)):
    #print(rating_list[x])
    ratingdist.append(rating_list[x][2])

for x in range(0,len(ratingdist)):
    ratingdist[x]=int(ratingdist[x])
#print(ratingdist[:20])
#a = array(ratingdist)
rd=plt.hist(ratingdist)
rd=plt.xlabel('Ratings')
rd=plt.ylabel('Count')
plt.show()
#print(ratingdist.count(9))

member=[]
for x in range(0,len(anime_list)):
    member.append(int(anime_list[x][6]))

rd=plt.hist(member,range=[1, 400000])
rd=plt.xlabel('Member count')
rd=plt.ylabel('Number of anime')
plt.show()

genre=[]
for x in range(0, len(anime_list)):
    genre.append(anime_list[x][2].replace(" ", "").split(","))
genrecount=[]
for x in range(0, len(genre)):
    genrecount.append(len(genre[x]))

gc=plt.hist(genrecount,range=[1, 10])
gc=plt.xlabel('Genre count')
gc=plt.ylabel('Number of anime')
plt.show()

