

''' THiS iS THE SLxVDR log loader'''
# The following script represents a loading bar shown in the console when triggered by action or user. #
# The script is used to show the progress of the program being executed. 'I.E. The Main Menu' #


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
