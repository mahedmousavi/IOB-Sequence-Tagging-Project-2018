dic=dict()
dicr=dict()
dicCon={}
with open('train.data','r') as file:
    for line in file: 
        if len(line)!=1:
                dic[line.split()[1]]=1 if line.split()[1] not in dic else dic[line.split()[1]]+1
for i in dic:
    if dic[i] not in dicr:
        dicr[dic[i]]=({i:0})
    else: dicr[dic[i]].update({i:0})
dic.clear()
for key in sorted(dicr.keys()):
    dic[key]=dicr[key].keys()