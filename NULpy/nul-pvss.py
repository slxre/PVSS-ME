

import time
from time import sleep


print("WELCOME 2 SLxRPvSS")
time.sleep(2.5)
def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()

items = list(range(0, 50))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
for i, item in enumerate(items):
   sleep(0.1)
   loadbar(i + 1, l, prefix='Progress:', suffix='Complete', length=l)

whois = input('Enter Your Given Password?: ')

if whois == 'JAi'.lower():
    print("Welcome, Admin")
    time.sleep(2)
    print("There Are No New SLxRIVNs That Have Recently Joined. Check Back Later. ")
    time.sleep(2)
    print("You Have Conquered The World. 100% ")
    time.sleep(3)
    print("NEW MEMNER HAS JOINED THE WORLD. + 100% ")
else:
    print("Fuck Off, Peasant")