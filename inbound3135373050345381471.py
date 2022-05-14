dec =int(input("enter any number: "))
l=[]
while dec>0:
    l.append(dec%2)
    dec=dec//2
l.reverse()
for dec in l:
    print(dec,end=" ")


                
