#random คนที่จะต้องจ่ายค่าอาหาร

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

limit_people = len(names)
limit_people_bill = limit_people - 1
result = random.randint(0, limit_people_bill)
bill = names[result]
print(f"{bill} is going to buy the meal today!")