import statistics
lst = []

n = int(input("Enter number of elements : "))  
print("Enter the numbers: ")
for i in range(0, n):
    ele = float(input())
  
    lst.append(ele)
      
print("The average of the given numbers is: %.2f" % statistics.mean(lst))