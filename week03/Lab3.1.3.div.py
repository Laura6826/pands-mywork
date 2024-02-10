# div.py
# The aim of this program is to read in two numbers and divd the first by the second.
# Author: Laura Lyons

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
answer = (x//y)
remainder = (x%y)
print ('{} divided by {} equals {} with reaminder {}'.format(x, y, answer, remainder))
