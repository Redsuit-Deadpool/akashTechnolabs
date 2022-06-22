import random
num = random.randint(-20,20)
if(num!=0):
    if(num<0):
        print(num,"is less than zero.")
    elif(num>0):
        print(num,"is greater than zero.")
else:
    print(num,"is a zero.")