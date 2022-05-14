import requests
import pprint
import time
import os
ip = input("Enter victim ip address : ")
# ip = "8.8.8.8"
print("██████╗░░█████╗░██████╗░██╗███╗░░██╗")
print("██╔══██╗██╔══██╗██╔══██╗██║████╗░██║")
print("██████╔╝██║░░██║██████╦╝██║██╔██╗██║")
print("██╔══██╗██║░░██║██╔══██╗██║██║╚████║")
print("██║░░██║╚█████╔╝██████╦╝██║██║░╚███║")
print("╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝")
time.sleep(2.4)
os.system('cls')
os.system('clear')
time.sleep(2.4)
print("collceting your data....")
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

text = 'information gathering source'
colored_text = colored(255, 0, 0, text)
print(colored_text)

# or

print(colored(255, 0, 0, 'data captured'))
url = f"https://ipapi.co/{ip}/json/"

r = requests.get(url)
pprint.pprint(r.json())
