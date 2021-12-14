# ทำการสุ่มตัวเลข 

import random

test = int(input("Create a seed number "))
a = test
number = random.randint(0, a)
if number % 2 == 0:
    print("Heads")
elif number % 2 != 0:
    print("Tails")