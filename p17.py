import random
n1 = random.randint(0,10)
n2 = random.randint(0,20)
print("Numbers before swapping are:\n1.",n1,"\n2.",n2)
n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2
print("Numbers after swapping are:\n1.",n1,"\n2.",n2)