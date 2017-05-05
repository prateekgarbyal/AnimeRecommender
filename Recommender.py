import math
import sys
import csv
import itertools
import collections
from scipy import spatial

with open('anime.csv', 'r') as f:
    reader = csv.reader(f)
    anime_list = list(reader)
del anime_list[0]

with open('similarity.csv', 'r') as f:
    reader = csv.reader(f)
    similarity = list(reader)

with open('supercleanedratings.csv', 'r') as f:
    reader = csv.reader(f)
    rating_list = list(reader)

with open('cleanedratings.csv', 'r') as f:
    reader = csv.reader(f)
    watched_list = list(reader)

animeid=[]
for x in range(0,len(anime_list)):
    animeid.append(int(anime_list[x][0]))

array=[-1]*36000
#print(array)
for x in range (0,len(animeid)):
    array[animeid[x]]=x

for x in range (0,len(similarity)):
    for y in range(0,len(similarity[x])):
        similarity[x][y]=float(similarity[x][y])

#print(similarity[0])
#userid = 99
userid=input("Enter User number you want Recommendations for")
userid=int(userid)

temp=[i for i in sorted(similarity[userid-1],reverse=True)][:11]
#list(similarity[userid-1])
#print(temp)

closestid=[]
for x in range(0,len(temp)):
    for y in range(0,len(similarity[userid-1])):
        if temp[x]==similarity[userid-1][y]:
            closestid.append(y)
#if similarity[userid-1][i] in temp:
#closestid.append(i)
closestid.remove(userid-1)
#print(closestid)

ratingsmatrix = [[-2]*len(anime_list) for _ in range(1000)]
for x in range (0,len(rating_list)):
    row=int(rating_list[x][0])-1
    column=int(rating_list[x][1])
    ratingsmatrix[row][column]=int(rating_list[x][2])


topanime=[]
for x in range(0,len(closestid)):
    topanime.append(sorted(range(len(ratingsmatrix[closestid[x]])), key=lambda i: ratingsmatrix[closestid[x]][i], reverse=True)[:10])
#print(topanime)
mergedtop = list(itertools.chain.from_iterable(topanime))
#print(mergedtop)

watched=[]
for x in range(0,len(watched_list)):
    if int(watched_list[x][0])==userid:
        watched.append(int(watched_list[x][1]))
#print(watched)

#print(watched)
notwatched = [x for x in mergedtop if x not in watched]
#print(notwatched)
counts = collections.Counter(notwatched)
new_list = sorted(notwatched, key=counts.get, reverse=True)
#print(new_list)
finalreco=[]
for x in range(0,len(new_list)):
    if new_list[x] not in finalreco:
        finalreco.append(new_list[x])
#print(finalreco)

animetyp=[]
for x in range (0,len(anime_list)):
    animetyp.append(anime_list[x][2].split(","))
merged = list(itertools.chain.from_iterable(animetyp))
#print(len(merged))
animetyp=list(set(merged))
#print(len(animetyp))
#print(animetyp)

top=[]
top.append(sorted(range(len(ratingsmatrix[userid-1])), key=lambda i: ratingsmatrix[userid-1][i], reverse=True)[:5])
#print(top)
top=top[0]
#print(top)

topprofile=[]
for x in range(0,len(top)):
    a = (anime_list[top[x]][2].replace(" ", "").split(","))
    #print (a)
    #topprofile.append(anime_list[top[x]][2])
    topprofile.append(a)
#print(topprofile)

flattend = list(itertools.chain.from_iterable(topprofile))
flattend=list(set(flattend))
#print(flattend)
#print(finalreco)

scores=[]

for x in range(0,len(finalreco)):
    scores.append(len(list(set(anime_list[finalreco[x]][2].replace(" ", "").split(",")) - set(flattend))))
#print(scores)
#print(finalreco)

finalreco=[x for (y,x) in sorted(zip(scores,finalreco))]
#print(finalreco)

print("TOP 5 ANIME WATCHED BY THE USER:")
for x in range(0,len(top)):
    print(anime_list[top[x]][1])

print("\nRECOMMENDED ANIME:")
for x in range(0,len(finalreco)):
    print(anime_list[finalreco[x]][1])