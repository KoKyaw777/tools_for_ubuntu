#to install web application analysis tool
#BY KAUNG KHANT ZAW (https://web.facebook.com/kaung.k.zaw.921025)
import os
import sys
print(''' /$$$$$$                                         
 /$$___$$                                        
| $$  \ $$  /$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$$ 
| $$$$$$$$ /$$_____/|____ /$$/ /$$__  $$| $$__  $$
| $$__  $$|  $$$$$$    /$$$$/ | $$  \ $$| $$  \ $$
| $$  | $$ \____  $$  /$$__/  | $$  | $$| $$  | $$
| $$  | $$ /$$$$$$$/ /$$$$$$$$|  $$$$$$/| $$  | $$
|__/  |__/|_______/ |________/ \______/ |__/  |__/''')
print("BY KAUNG KHANT ZAW")

def function():
    print('''1. BURPSUITE 2. CUTYCAPT 3. DIRB 4. WFUZZ 5. NIKTO
6. JSQL 7. CADAVER 8. WHATWEB 9. SQLMAP 10. SKIPFISH 
11. TO INSTALL ALL PROGRAMS 
0. TO EXIT PROGRAM''')
    global get_option
    get_option = int(input('kali>>> '))
#    if get_option == 1:
#        os.system('sudo apt install wpscan')
    if get_option == 1:
        os.system('sudo apt install burpsuite')
    elif get_option == 2:
        os.system('sudo apt install cutycapt')
    elif get_option == 3:
        os.system('sudo apt install dirb')
    elif get_option == 4:
        os.system('sudo apt install wfuzz')
    elif get_option == 5:
        os.system('sudo apt install nikto')
    elif get_option == 6:
        os.system('sudo apt install jsql')
    elif get_option == 7:
        os.system('sudo apt install cadaver')
    elif get_option == 8:
        os.system('sudo apt install whatweb')
    elif get_option == 9:
        os.system('sudo apt install sqlmap')
    elif get_option == 10:
        os.system('sudo apt install skipfish')
    elif get_option == 11:
        os.system('sudo apt install burpsuite cutycapt dirb wfuzz nikto jsql cadaver whatweb sqlmap skipfish')
    elif get_option == 0:
        exit()
    else:
        print ('Invalid...')
while True:
    function()
else:
    exit()
