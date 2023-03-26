import os 
import threading
import requests, random
from dhooks import Webhook
import ctypes
import colorama
from colorama import Fore, Style
ctypes.windll.kernel32.SetConsoleTitleW("Roblox Group Finder | Made by daddy m#8718 | Running")
# Initialize colorama
colorama.init()

def groupfinder():
    id = random.randint(1000000, 1150000)
    r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") 
    if 'owned' not in r.text:
        re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
        if 'isLocked' not in re.text and 'owner' in re.text:
            if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                hook.send(f'Hit: https://www.roblox.com/groups/group.aspx?gid={id}')
                print(f"[+ +] Hit: {id}")
            else:
                print(f"[-] No Entry Allowed: {id}")
        else:
            print(f"[-] Group Locked: {id}")
    else:
        print(f"[-] Group Already Owned: {id}")


print(Fore.LIGHTBLUE_EX + """
███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝     
""" + Fore.RESET)

#your webhook
hook = input(Fore.LIGHTGREEN_EX + '[+]' + Fore.RESET + Fore.LIGHTBLUE_EX +'Enter your webhook url: ')
#number of threads
threads = int(input(Fore.LIGHTGREEN_EX + '[+]' + Fore.RESET + Fore.LIGHTBLUE_EX +'How many threads: ' + Fore.RESET))

while True:
    if threading.active_count() <= threads:
        threading.Thread(target=groupfinder).start()