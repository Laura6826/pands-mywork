# student_data.py
# The aim of this program is ot store a students data in a list and print out their data
# Author: Laura Lyons

student = {
            'name': 'Mary',
           'Modules': [ 
               {'Course_Name':'Programming',
            'grade': 45},
            {'Course_Name': 'History',
             'grade': 99} ]
             }

print ('Student: {}'.format(student['name']))
for modules in student ['Modules']:
    print ('\t {} \t: {}'.format(modules['Course_Name'], modules['grade']))