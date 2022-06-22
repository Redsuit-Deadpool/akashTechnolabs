num = int(input("Enter the number: "))
sum = 0
if(num<=0):
    print("Enter a number that is greater than zero")
    num = int(input("Re-enter the number: "))
for i in range(1,num+1):
    sum+=i
print("Sum of all the natural numbers till given number is:",sum)