##Fisherman

import random
fish = int(input("How many kilograms of fish did you get?"))
dollars = fish*3
#1 is 100
if dollars >100:
  gift = random.randint(1,3)
if gift == 1:
    print("Congratulations you won a fisherman hat")
    print(f"You have {fish} kilograms ${dollars} is how much it costs")
elif gift == 2:
    print("Congratulations you won a boat")
    print(f"You have {fish} kilograms ${dollars} is how much it costs")
elif gift == 3:
    print("Congratulations you won a fishing rod")
    print(f"You have {fish} kilograms ${dollars} is how much it costs")
