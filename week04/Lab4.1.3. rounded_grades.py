# rounded_grades.py
# Author: Laura Lyons

percentage = float (input('Please enter your percentage: '))
# print (percentage)

if percentage < 0 or percentage > 100:
    print ('Please enter a number between 0 and 100.')
elif percentage < 40:
    print ('Fail')
elif percentage > 40 and percentage<49.4:
    print ('Pass ')
elif percentage >50 and percentage < 59.4:
    print ('Merit 1')
elif percentage >60 and percentage< 69.4:
    print ('Merit 2')
else:
    print ('Distinction')
