import random
import numpy as np
bigrams = []
pos_freq={}
tag=[]
tagdistro=[]
totalTagCount = 0
data = ("train.data",'r')
test= ('test.data','r')
with open('train.data','r') as file:
    for line in file:
        a=line.split()
        if len(a)!=0 : 
            bigrams.append(str(a[0]+' '+a[1]))
            pos_freq[a[1]] = 1. if a[1] not in pos_freq else pos_freq[a[1]] + 1
            totalTagCount+=1
        else: a.append('$')
for Tag, count in pos_freq.items():
    tag.append(Tag)
    tagdistro.append(count/totalTagCount)
file.close()
   
randresult = open("rand.txt", "w")
distroresult = open("distro.txt", "w")
major = open("major.txt", "w")
majInO = open("majorO.txt", "w")

with open("test.data", "r") as file:
    for line in file:
        a=line.split()
        if len(a)==0:
            randresult.write(line)
            distroresult.write(line)
            major.write(line)
            majInO.write(line)
        else:
            randresult.write("%s %s %s\n" % (a[0], a[1], random.choice(tag)))
            distroresult.write("%s %s %s\n" % (a[0], a[1], np.random.choice(tag, 1, p=tagdistro)))
            major.write("%s %s %s\n" % (a,a[1], "I-movie.name"))
            majInO.write("%s %s %s\n" % (a, a[1], "O"))
randresult.close()
distroresult.close()
majInO.close()
major.close()