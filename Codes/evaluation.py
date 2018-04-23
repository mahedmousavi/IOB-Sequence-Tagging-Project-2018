import subprocess 
sen=[]
lexdic={}
lex=open('lx.lex')
for line in lex: lexdic[line.split()[1]]=line.split()[0]
lex.close()
with open('test.data','r') as file:
    for line in file:
        a=line.split()
        if len(a)!=0 : sen.append(a[0])
        else: sen.append('$')
with open('test.txt','w') as output:
    for word in sen:
        if word=='$': output.write('\n')
        else: 
            output.write(str(word))
            output.write(' ')
output.close()
result=open('result.txt','w')
with open('test.txt','r') as test:
    for line in test: 
        com1 = "echo '{0}' | farcompilestrings --symbols=lx.lex --unknown_symbol='<unk>' --generate_keys=1 --keep_symbols | farextract --filename_suffix='.fst'".format(str(line).replace("'"," "))
        output = subprocess.check_output(['bash','-c', com1])
        com2= "fstcompose 1.fst uniPosTagger.fst | fstcompose - pos.lm | fstrmepsilon | fstshortestpath > all_together.fst"
        output2 = subprocess.check_output(['bash','-c', com2])
        com3= "fsttopsort all_together.fst | fstprint > fsaInfo.txt"
        output3 = subprocess.check_output(['bash','-c', com3])
        info=open('fsaInfo.txt','r')
        temp=info.readlines()
        for index in range(len(temp)-1):
            temp[index]=temp[index].replace('\t',' ')
            result.write(temp[index].split(' ')[2])
            result.write(' ')
            result.write(lexdic[temp[index].split(' ')[3]])
            result.write('\n')
        info.close()
        result.write('\n')
result.close()
with open('prediction.txt','w') as final:
    pred=open('result.txt','r')
    test=open('test.data','r')
    for target in test: 
        if len(target)!=1: 
            final.write(target.split()[0])
            final.write(' ')
            final.write(target.split()[1])
            final.write(' ')
            temp =pred.readline().split()[1]
            if '_' in temp: final.write('O')
            else: final.write(temp)
            final.write('\n')
        else:
            pred.readline()
            final.write('\n')
final.close()