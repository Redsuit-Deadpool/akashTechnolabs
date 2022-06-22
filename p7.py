num = int(input("Enter the number that you want to check: "))
if(num!=0):
    if(num<0):
        print(num,"is less than zero.")
    elif(num>0):
        print(num,"is greater than zero.")
else:
    print(num,"is a zero.")