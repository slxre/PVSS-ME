# NUL #


___COPIED SCRIPT.old__
if user == 'SLxRE':
    print("Welcome, Admin")
    time.sleep(3)
    print("There Are No New SLxRIVNs That Have Recently Joined. Check Back Later. ")
    time.sleep(4)
    print("You Have Conquered The World. + 100% ")
    time.sleep(5)
    print("NEW MEMNER HAS JOINED THE WORLD. + 100% ")
    time.sleep(1)
    print("NEW MEMNER HAS JOINED THE WORLD. + 100% ")
    time.sleep(1)
    print("NEW MEMNER HAS JOINED THE WORLD. + 100% ")
    time.sleep(1)
    print("NEW MEMNER HAS JOINED THE WORLD. + 100% ")
    time.sleep(1)
    print("NEW MEMNER HAS JOINED THE WORLD. + 100% ")
    time.sleep(1)
    user = input("Press E to Exit")
    if user == 'E'.lower():
                    print('Starting Process...')
                    user = input("Enter Your PassCode to Exit: ")
                    if user == 'SLxRE':
                            print('Exiting...')
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

                                        print("Goodbye ", whois, " See You Next Year!!")
                                        time.sleep(2)
                                        quit()

----

__OLD DATABASE__
# DATABASE / iNFO
#_________________#
# INPUTs
user = ['member', 'Agent', 'SLxRE'] # Input for initial question ("Who Are You?: ")
inputt2 = 'r'
MAC = ['gnrlaccess', 'Xi004'] #Member Access Code
UEC = ['egnrlaccess', '400iX'] #Universal Exit Code
AAC = 'SLxRExx'  # "Admin Access Code"
AEC = 'xxSLxRE' # Admin Exit Code

# EXECUTABLEs
exitt = 'E' # Executable to exit application
mact1 = True
# VERIFIERs
veriT= True
veriF = False

imq = True
mi = 'member'
msa1 = print()



msa1 = input('member').lower() == imq
