#!/bin/python3

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

lenght = len(names)
result = random.randint(0,lenght - 1)
result2 = names[result]


print(f'{result2} is going to buy the meal today!')
