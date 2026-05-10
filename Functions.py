##function
def my_function():
  print("Hello from a python class")

my_function()
###########################################
Example
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
###########################################
a = int(input("plz enter first number:"))
b = int(input("plz enter sec number:"))

def my_function(first, sec):
  print(first + sec)

my_function(a, b)
###########################################
def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
