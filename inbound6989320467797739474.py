import json
infile='sa.json'
infile=open(infile,'r')
num=0
u=input('enter your name: ')
d=dict()
dic=json.load(infile)
infile.close()
for k,v in dic.items():
    print(k)
    a=input()
    if a == v:
        num+=1
        d[k]=v
d[u]=num
print(d)
outfile='sar.json'
outfile=open(outfile,'w')
json.dump(d,outfile)
outfile.close()
