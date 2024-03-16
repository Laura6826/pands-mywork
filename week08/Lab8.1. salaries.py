# salaries.py
# Authoer: Laura Lyons

import numpy as np

#np.random.seed(1)
min_salaries = 20000
max_salaries= 80000
number_required= 10

salaries= np.random.randint (min_salaries, max_salaries, number_required)
salaries2= salaries +(5000)
salaries3= salaries *1.05
new_salaries= salaries3.astype(int)
print (salaries)
print (salaries2)
print (new_salaries)