import os
import time
import webbrowser
import sys
import tkinter as tk

DARK_RED = "\033[31m"
DARK_BLUE = "\033[34m"
RESET = "\033[0m"


def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

print(DARK_RED +"""
    _  ______________  ___       _____ ______ _____ 
| |  | ||  _  | ___ \  \/  |      |  __ \| ___ \_   _|
| |  | || | | | |_/ / .  . |______| |  \/| |_/ / | |  
| |/\| || | | |    /| |\/| |______| | __ |  __/  | |  
\  /\  /\ \_/ / |\ \| |  | |      | |_\ \| |     | |  
 \/  \/  \___/\_| \_\_|  |_/       \____/\_|     \_/  
                                                      
                                                     """ + RESET)

print(DARK_RED +"made by ANS" + RESET)
time.sleep(2)
print(DARK_RED +"choose an option" + RESET)
print(DARK_RED +"1. attack the website" + RESET)
print(DARK_RED +"2. SQL injection" + RESET)
print(DARK_RED +"3. Build Malicous file (rat / stealer)" + RESET)
print(DARK_RED +"4. exit" + RESET)

choice = input(DARK_BLUE +"Enter your choice: " + RESET)

if choice == "1":
    webbrowser.open("https://github.com/Moham3dRiahi/XAttacker")

elif choice == "2":
  print(DARK_BLUE +"""SQL tools
  sql attack tool: https://github.com/TEAMBCT1/autosql
  sql vuln scanner: https://github.com/Bitwise-01/SQL-scanner
  other sql tools:
  sqlmap: https://github.com/sqlmapproject/sqlmap
  sqlninja: https://github.com/CHYbeta/sqlninja
  """ + RESET)

elif choice == "3":
 print(DARK_BLUE +"""stealer tools
stealer: https://github.com/passsa1337/Vare-Stealer
RATS:
NjRAT: https://github.com/livynoxl/NjRat-0.7D-Danger-Edition-Cracked-By-MMLo7
more coming soon..""" + RESET)


else:
 print(DARK_BLUE +"invalid choice get da hell out of here" + RESET)
sys.exit()
