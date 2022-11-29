import random
a=[]
luwi=[]
kenti=[]
for i in range (0, 10):
    a.append(random.randrange(0,100))
print(a)
for i in a:
    if i%2==0:
        luwi.append(i)
    else:
        kenti.append(i)
print(luwi)
