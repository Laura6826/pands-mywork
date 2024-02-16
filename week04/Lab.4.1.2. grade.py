# grade.py
# The aim of th is program is to prompt the user to enter their presentage mark
# and prints out the corresponding grade.
# Author: Laura Lyons

percentage = float (input('Please enter your percentage: '))
# print (percentage)

if percentage < 0 or percentage > 100:
    print ('Please enter a number between 0 and 100.')
elif percentage < 40:
    print ('Fail')
elif percentage > 40 and percentage<50:
    print ('Pass ')
elif percentage >50 and percentage < 60:
    print ('Merit 1')
elif percentage >60 and percentage< 70:
    print ('Merit 2')
else:
    print ('Distinction')
