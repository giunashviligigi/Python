import random
a=input('string')
b=random.randrange(0,10)
if b==0:
    print(a.count('l'))        
elif b==1:
    print(a.find('l'))
elif b==2:
    print(a.replace('l','*'))
elif b==3:
    print(a.replace('l',''))
elif b==4:
    print(a.upper())
elif b==5:
    print(a.lower())
elif b==6:
    print(a.capitalize())
elif b==7:
    print(a.isupper)
elif b==8:
    print(a[::-1])
elif b==9:
    print(a[1:-1])