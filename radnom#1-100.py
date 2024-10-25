##  User can ask for random number  ##

import random
while True:
    x = input('Press ''y'' for random number \n\nPress any other key to stop \n:')
    x = x.lower()
    if x =='y':
        print('\n'(random.randint(0,100)))
    else:
        print('END')
        break
