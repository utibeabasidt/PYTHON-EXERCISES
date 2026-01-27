'''It is used to perform multiple tasks at the same time.. It is good for Input?Output bound tasks like reading files, or doing banking system, or fetching data from APIs'''

import threading
from time import sleep # making the function to wait some time before before performing

def walk_the_dog(name):
  sleep(7)
  print(f'You finished walking the {name} dog')

def dump_the_refuse():
  sleep(2)
  print('You dumped the refuse')

def get_the_mail():
  sleep(4)
  print('You got the mail')

# walk_the_dog() 
# dump_the_refuse()
# get_the_mail()
'''All these are moving on the same thread, meaning that we need to wait for one function to finish before doing another'''

# Solution using threads with target function and argument, if any
chore1 = threading.Thread(target=walk_the_dog, args=('German Shepherd',)) # args accepts value in tuples, so we add a comma to indicate
chore1.start()
chore2 = threading.Thread(target = dump_the_refuse)
chore2.start()
chore3 = threading.Thread(target = get_the_mail)
chore3.start()
'''This runs on one thread. While we are waiting to walk the dog, We have dumped the refuse, then we get the mail, then we now finish walking with the dog.
Disadvantage is that any code under the threads will start running even when the threads are not finished yet'''

'''We do not want any other program under the thread to run before the threads, so we have to join it. This enables the threads to run first before any other code below'''
chore1.join()
chore2.join()
chore3.join()

print('Tasks finished') # becuase of the join method, all codes under the thread will have to wait till the threads are over