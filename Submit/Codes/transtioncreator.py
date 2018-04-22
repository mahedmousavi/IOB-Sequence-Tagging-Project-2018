import math
bigrams = []
pos_freq={}

#clean=open('clean.data','w')
#with open('train.data','r') as file:
#    for line in file:
#        a=line.split()
#        if len(a)!=0 : 
#            if a[1]=='O': 
#                clean.write(str(a[0]+' '+'_'+a[0]))
#                clean.write('\n')
#            
#            else: 
#                clean.write(str(a[0]+' '+a[1]))
#                clean.write('\n')
#        else: clean.write('\n')
#clean.close()
with open('clean.data','r') as file:
    for line in file:
        a=line.split()
        if len(a)!=0 : 
            bigrams.append(str(a[0]+' '+a[1]))
            pos_freq[a[1]] = 1. if a[1] not in pos_freq else pos_freq[a[1]] + 1
        else: a.append('$')
##        's cleaned, _word did
#bigrams_freqs = {}
#for pair in bigrams:
#    bigrams_freqs[pair] = 1. if pair not in bigrams_freqs else bigrams_freqs[pair] + 1
#bigrams_prob = {}
##
#for key in bigrams_freqs.keys():
#    a=key.split()
#    bigrams_prob[key]= round(-math.log(bigrams_freqs[key]/pos_freq[a[1]]),2)
#    
#with open('uniPosTagger.txt','w') as output:
#    for key in bigrams_prob.keys():
#        output.write('0 0 ')
#        output.write(str(key))
#        output.write(' ')
#        output.write(str(bigrams_prob[key]))
#        output.write('\n')
#    for key in pos_freq.keys():
#        output.write('0 0 ')
#        output.write('<unk>')
#        output.write(' ')
#        output.write(str(key))
#        output.write(' ')
#        output.write('3.71')
#        output.write('\n')
#    output.write('0')
#output.close()    
#pos=[]
#with open('clean.data','r') as file:
#    for line in file:
#        a=line.split()
#        if len(a)!=0 : 
#            pos.append(a[1])
#        else: pos.append('$')
#
#with open('pos.txt','w') as output:
#    for tag in pos:
#        if tag=='$': output.write('\n')
#        else: 
#            output.write(str(tag))
#            output.write(' ')
#output.close()
