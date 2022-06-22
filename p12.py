import random
num = random.randint(-500,500)
if(num<100):
    if(num%2==0):
        print(num,"is less than 100 and even.")
    else:
        print(num,"is less than 100 and odd.")
else:
    print(num,"is greater than 100.")