# random_generator.py
# The aim of this program is to print out random numbers between 1 and 10
# Author: Laura Lyons

import random
'''
number = random.randint(1,10)
print ('Here is a random number {}' .format(number))
'''

lower_limit = int(input('Enter the lower limit of your range: '))
upper_limit = int(input('Enter the upper limit of your range: '))
range_of_numbers = range(lower_limit, upper_limit)
number = random.choice(range_of_numbers)
print('Here is your number: {}' .format(number))