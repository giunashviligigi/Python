import random
jami=0
a=random.randrange(0,10)
b=random.randrange(0,10)
print (a,b)
if a>b:
    for i in range(b,a):
        jami=jami+i
else:
    for i in range(a,b):
        jami=jami+i
        
print (jami)