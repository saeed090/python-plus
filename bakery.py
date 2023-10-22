#saeed bakery in python plus class
#this is my project
total_1 = 0
total_2 = 0
total_3 = 0     #this is add some one
total_4 = 0
total_5 = 0

breads = {
    "barbari": 1000,
    "sangak" : 3000,
    "lavash" : 500,     #this is dict
    "taftoon": 2500,
    "shirmal": 1750
}

print ("welcame to saeed bakery")
print ("Address: 22 ghaem shahr BLVD")

switch = 0
name = input ("please enter your name: ")
phone_number = input ("please enter your phone number: ")
card_number = input ("please insert your card: ")

password_1 = input ("please create your password: ")
password_2 = input ("please enter your password: ")
self_checkout = "notdefined"
##############start for password #######################
for password in range(2):
    while password_1 != password_2:
        print("wrong password")
        password_2 = input("try again")
print ("your password is accepted")

while self_checkout != "done":
    if switch == 0:
        self_checkout = input("dear customer enter your bread: ")
    else:
        self_checkout = input("please enter your next item")
    while self_checkout not in dict(breads):
        if self_checkout == "done":
            break
        self_checkout = input("please enter exsisting bread: ")
    if self_checkout == "done":
        break
    customer = int (input(f"how many {self_checkout} did you ger? "))

    if self_checkout == "barbari":
        total_1 = breads["barbari"] * customer + total_1
        print (f"total is {total_1}")

    elif self_checkout == "sangak":
        total_2 = breads["sangak"] * customer + total_2
        print (f"total is {total_2}")

    elif self_checkout == "lavash":
        total_3 = breads["lavash"] * customer + total_3
        print (f"total is {total_3}")

    elif self_checkout == "taftoon":
        total_4 = breads["taftoon"] * customer + total_4
        print (f"total is {total_4}")

    elif self_checkout == "shirmal":
        total_5 = breads["shirmal"] * customer + total_5
        print (f"total is {total_5}")

    total = total_1 + total_2 + total_3 + total_4 + total_5

    print ("your item had been enterd")
    switch=1

print (f"so your total is {total}")
