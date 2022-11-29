a=[1,33,44,34,56,78,89,2,668,870]
b=[]
for i in range (0, len(a)):
    if i%2==1 and a[i]%2==0:
        b.append(a[i])
print(b)


