a=input("insert the password to quit")
tries=1
while a!="wavedi":
    a=input("you are still in, insert the password to quit")
    tries=tries+1
    if tries>5:
        break
if tries>5:
    print("you are blocked")
else:
    print ("welcome back")