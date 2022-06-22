print("      1. Addition")
print("      2. Substraction")
print("      3. Multiplication")
print("      4. Division")
action = int(input("Select the action that you want to perform: "))
match action:
    case 1:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("Addition of numbers is:",num1+num2)
    case 2:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("Substraction of numbers is:",num1-num2)
    case 3:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("Multiplication of numbers is:",num1*num2)
    case 4:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))        
        print("Division of numbers is:",num1/num2)


    