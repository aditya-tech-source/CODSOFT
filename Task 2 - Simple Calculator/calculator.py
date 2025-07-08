# Design a simple calcualtor with basic arithermetic opeartion .Prompt the user to input two numbers and an opeartion choice.Perform the calcualtion and display the result.
num1 = input("Enter a num1: ")
num1 = int(num1)
print("User entered num1: ",num1)
num2 = input("Enter a num2: ")
num2 = int(num2)
print("User entered nuum2: ",num2)
operationchoice = input("Enter from +,-,*,/")
if operationchoice == "+":
    print("The sum of two numbers: ",num1 + num2)
elif operationchoice == "-":
    print("The difference of two numbers: ",num1 - num2)
elif operationchoice == "*":
    print("The product of two numbers: ",num1*num2)
elif operationchoice == "/":
    if num2 != 0:
        print("The division of two numbers: ",num1/num2)
    else:
        print("Division by zero is not allowed")
else:
    print("User enetered incorrect choice.Entered from +,-,*,/")
