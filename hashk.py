import os
clear = lambda: os.system('cls')
piphashlib = lambda: os.system('pip install hashlib')
piphashlib()
clear()
pipcolorama = lambda: os.system('pip install colorama')
pipcolorama()
clear()
from hashing import hashingtxt
from readhw import Readw
import time, sys
from time import sleep
from colorama import init, Fore, Back, Style

def _logo_():
    logo = '''

    ┌─┐┬    ┌─┐┌─┐┌┐┌┌─┐┬─┐┌─┐┬    ┬ ┬┌─┐┬┌┬┐┬ ┬┌─┐┌┬┐
    ├─┤│    │ ┬├┤ │││├┤ ├┬┘├─┤│    ├─┤├─┤│ │ ├─┤├─┤│││
    ┴ ┴┴─┘  └─┘└─┘┘└┘└─┘┴└─┴ ┴┴─┘  ┴ ┴┴ ┴┴ ┴ ┴ ┴┴ ┴┴ ┴
    '''
    exp = 'Telegram And Whatsapp +970597668158'
    for lo in logo:
        sleep(0.03)

        sys.stdout.write(Fore.BLUE + lo)
    for l in exp:
        sleep(0.02)
        sys.stdout.write(l)

    print('\n')
_logo_()

the_hash = str(input("the hash: "))
the_wordlist = str(input("the wordlist: "))
the_hash_type = str(input("the hash_type: "))
RR = Readw()
readall = RR.Readwlist(the_wordlist)
HH = hashingtxt()
for i in readall:
    i = i.rstrip("\n")
    hashT = HH.hashingtext(i,the_hash_type)
    if the_hash == hashT:
        print ("{}::{}".format(the_hash,i))
