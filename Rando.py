#Random number generator
#to be done
amount = raw_input("How many random numbers do you need: ")
Num_max = raw_input("What is the max value you need: ")
Num_min = raw_input("What is the min value you need: ")
num_list = []
from random import randint
for i in range(amount):
    num_list[i] = randint(Num_min, Num_max)

print numlist

    
