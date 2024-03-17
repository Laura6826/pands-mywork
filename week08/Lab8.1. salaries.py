# salaries.py
# Authoer: Laura Lyons

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
min_salaries = 20000
max_salaries= 80000
number_required= 10

salaries= np.random.randint (min_salaries, max_salaries, number_required)
salaries2= salaries +(5000)
salaries3= salaries *1.05
new_salaries= salaries3.astype(int)
#print (salaries)
#print (salaries2)
#print (new_salaries)

#plt.hist(salaries)
ages= np.random.randint(low=21, high=65, size= number_required)
plt.scatter(ages, salaries)

xpoints= np.array(range(1,101))
ypoints=(xpoints*xpoints)
plt.plot(xpoints, ypoints, color='red', label = "x squared")
plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()
plt.show() 
plt.savefig('Pretty ploy.png')

#end 