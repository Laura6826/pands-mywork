# floor.py
# The aim of this program is to read in a float and output a integer, rounded down.
# Author: Laura Lyons

import math
number_to_floor = float(input('Enter a float\'decimal\' number: '))
floored_number = math.floor(number_to_floor)
print ('{} floored is {}'.format(number_to_floor, floored_number))