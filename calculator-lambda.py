##Pyhton Lambda Calculator

print("Welcome to calculator")
print("---------------------")

howManyNums = input("Would you like to input 2 or 3 numbers: ")

operatorChoice = ""

num1 = ""
num2 = ""
num3 = ""

#addition
add = lambda x, y: x + y

#subtraction
subtract = lambda x, y: x - y

#multiply
multiply = lambda x, y: x * y

#divide
divide = lambda x, y: x / y

#+ -
addSub = lambda x, y, z: x + y - z

#+ *
addMulti = lambda x, y, z: x + y * z

#+ /
addDiv = lambda x, y, z: x + y / z

#- +
subAdd = lambda x, y, z: x - y + z

#- *
subMulti = lambda x, y, z: x - y * z

#- /
subDiv = lambda x, y, z: x - y / z

#* -
multiSub = lambda x, y, z: x * y - z

#* +
multiAdd = lambda x, y, z: x * y + z

#* /
multiDiv = lambda x, y, z: x * y / z

#/ +
divAdd = lambda x, y, z: x / y + z

#/ -
divSub = lambda x, y, z: x / y - z

#/ *
divMulti = lambda x, y, z: x / y * z

#+ +
addAdd = lambda x, y, z: x + y + z

#- -
subSub = lambda x, y, z: x - y - z

#* *
multiMulti = lambda x, y, z: x * y * z

#/ /
divDiv = lambda x, y, z: x / y / z

print("Thefollowing operators are available on this calculator: +, -, *, /")
print("If you are done using the calculator, type in 'quit' instead of the operator")
print("---------------------")


if howManyNums == "3":

    while operatorChoice != "quit":
            
        num1 = float(input("Enter your first number: ")) #first number

        operatorChoice = input("Operator: ") #operator choice
            
        num2 = float(input("enter your second numebr: ")) #second number

        operatorChoice2 = input("second operator: ")

        num3 = float(input("enter your third numebr: ")) #second number

        if operatorChoice == "+" and operatorChoice2 == "-":
            print(num1, "+", num2, "-", num3, "=", addSub(num1, num2, num3))

        elif operatorChoice == "+" and operatorChoice2 == "*":
            print(num1, "+", num2, "*", num3, "=", addMulti(num1, num2, num3))  
                
        elif operatorChoice == "+" and operatorChoice2 == "/":
            print(num1, "+", num2, "/", num3, "=", addDiv(num1, num2, num3))

        elif operatorChoice == "-" and operatorChoice2 == "+":
            print(num1, "-", num2, "+", num3, "=", subAdd(num1, num2, num3))
                
        elif operatorChoice == "-" and operatorChoice2 == "*":
            print(num1, "-", num2, "*", num3, "=", subMulti(num1, num2, num3))

        elif operatorChoice == "-" and operatorChoice2 == "/":
            print(num1, "-", num2, "/", num3, "=", subDiv(num1, num2, num3))
                
        elif operatorChoice == "*" and operatorChoice2 == "+":
            print(num1, "*", num2, "+", num3, "=", multiAdd(num1, num2, num3))

        elif operatorChoice == "*" and operatorChoice2 == "-":
            print(num1, "*", num2, "-", num3, "=", multiSub(num1, num2, num3))

        elif operatorChoice == "*" and operatorChoice2 == "/":
            print(num1, "*", num2, "/", num3, "=", multiDiv(num1, num2, num3))

        elif operatorChoice == "/" and operatorChoice2 == "+":
            print(num1, "/", num2, "+", num3, "=", divAdd(num1, num2, num3))
                
        elif operatorChoice == "/" and operatorChoice2 == "-":
            print(num1, "/", num2, "-", num3, "=", divSub(num1, num2, num3))
                
        elif operatorChoice == "/" and operatorChoice2 == "*":
            print(num1, "/", num2, "*", num3, "=", divMulti(num1, num2, num3))
            
        else: 
            print("operator not found")



if howManyNums == "2":

    while operatorChoice != "quit":
            
        num1 = float(input("Enter your first number: ")) #first number

        operatorChoice = input("Enter your operator: ") #operator choice

        num2 = float(input("enter your second numebr: ")) #second number

        if operatorChoice == "+":
            print(num1, "+", num2, "=", add(num1, num2))   

        elif operatorChoice == "-":
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operatorChoice == "*":
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operatorChoice == "/":
            print(num1, "/", num2, "=", divide(num1, num2))
            
        else: 
            print("operator not found")


print("Have a good day!")
