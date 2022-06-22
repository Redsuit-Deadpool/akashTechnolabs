num = int(input("Enter the number that you want the table of: "))
start = int(input("Where do you want to start the table from? "))
end = int(input("Where do you want to end the table? "))
print("Table of",num,"is:")
for i in range(start,end+1):
    print(num,"*",i,"=",num*i,"\n")