## Import stuff
import os
import requests
import colorama
from colorama import Fore

## Initialize colorama
colorama.init(autoreset=True)

## Welcome Message
os.system("cls")

os.system("title Command Prompt but Better")

print("Welcome to Command Prompt but Better!")
print("Made by DarkDev#2048")
print("\n\n")

## Main Code
def command_line():
    while True:
        command = input(Fore.BLUE + os.getcwd() + "$ " + Fore.GREEN)
        print(Fore.WHITE)
        if command.startswith("cd "):
            directory = command[3:]
            try:
                os.chdir(directory)
            except:
                print("The system cannot find the path specified.")
        else:
            os.system(command)
        print()

command_line()
