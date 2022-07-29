
import time
#############################################################################################

print("WELCOME 2 SLXRme -V0.0.1")
time.sleep(2.5)
print("Loading Setup...")

from time import sleep
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

if user != 'gnrlaccess'.lower():
                                                            print("Invalid Password")
                                                            time.sleep(2)
                                                            print("Exiting...")
                                                            time.sleep(2)
                                                            from time import sleep
                                                            
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
                                                                        quit()
#############################################################################################

