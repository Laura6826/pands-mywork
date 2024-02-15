# is_even.py
# The aim of this program is to input a number
#  and the output will tell the user if the number os even or odd.
# Author: Laura Lyons

number = int(input('Enter a number: '))
if (number %2) ==0:
    print('{} is an even number'.format(number))
else:
    print('{} is an odd number'.format(number))

