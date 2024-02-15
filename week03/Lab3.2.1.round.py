# round.py
# The aim of this programm is to read in a float and output an integer,
# rounded up or down
# Author: Laura Lyons

number_to_round = float(input('Enter a float \'decimal\' number: '))
rounded_number = round(number_to_round)
print ('{} rounded is {}' .format(number_to_round, rounded_number))