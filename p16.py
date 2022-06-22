import random
n1 = random.randint(0,10)
n2 = random.randint(0,20)
n3 = random.randint(0,30)
print("Numbers are:\n1.",n1,"\n2.",n2,"\n3.",n3)
if(n1<n2 and n1<n3):
    print(n1,"is the smallest of them all.")
elif(n2<n1 and n2<n3):
    print(n2,"is the smallest of them all.")
else:
    print(n3,"is the smallest of them all.")