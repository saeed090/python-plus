#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
###################################################
ExampleGet your own Python Server
If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")
####################################################
number1 = int(input("plz enter your first number: "))
number2 = int(input("plz enter your sec number: "))

if number1 > number2:
  print("number1 is greater than number2")
####################################################
Elif
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

Example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
###################################################
user_rank = int(input("plz enter your rank: "))

if user_rank == 1:
    print("you get gold medal")
elif user_rank == 2:
    print("you get silver medal")
elif user_rank == 3:
    print("you get boronz medal")
else:
    print("plz enter number 1 or 2 or 3")
####################################################
if a > b: print("a is greater than b")
####################################################
a = 2
b = 330
print("A") if a > b else print("B")
