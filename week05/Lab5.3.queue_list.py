# queue_list.py
# The aim of this program is to call up the next number on a list, in order.
# Author: Laura Lyons

import random
queue = []
number_of_numbers = 10

for n in range(0, number_of_numbers):
    queue.append(random.randint(0,100))

print (f'Queue is {queue}')
while len(queue)!= 0:
    current_number=queue.pop(0)
    print (f'Current number is, {current_number} and the queue is, {queue}')
else:
    print ('The queue is now empty')
