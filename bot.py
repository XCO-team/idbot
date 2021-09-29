import os
from colorama import Fore
import time
import sys
def starter():

    os.system("clear")

    print(Fore.LIGHTRED_EX+"""\n   
 
\t\t██╗██████╗░██████╗░░█████╗░████████╗
\t\t██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
\t\t██║██║░░██║██████╦╝██║░░██║░░░██║░░░
\t\t██║██║░░██║██╔══██╗██║░░██║░░░██║░░░
\t\t██║██████╔╝██████╦╝╚█████╔╝░░░██║░░░
\t\t╚═╝╚═════╝░╚═════╝░░╚════╝░░░░╚═╝░░░

        
          """)  
def gets():
    time.sleep(0.1)
    print(Fore.RED+" ["+Fore.WHITE+"卐"+Fore.RED+"]"+Fore.CYAN+" Choose one of the options \n")
    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX+" [1] Get post's and post they again\n")
    time.sleep(0.1)
    print(Fore.RED+" [2] download instagram profile\n") 
    time.sleep(0.1)
    print(Fore.BLUE+" [3] Exit . . .\n")  
starter()
gets()
get = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"XCO"+Fore.BLUE+"~"+Fore.WHITE+Fore.LIGHTYELLOW_EX+"HTTP-instagram"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
if get == "1":
    os.system("python instagramdler.py")
if get == "2":
    os.system("python deler.py")
if get == "3":
    print("by")
else :
    os.system("python bot.py")
