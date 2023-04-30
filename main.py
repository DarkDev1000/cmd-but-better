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

## Auto Update
url = "https://api.github.com/repos/{owner}/{repo}/releases/latest"

owner = "DarkDev1000"
repo = "cmd-but-better"

token = "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"

repo_path = "/main.py"

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url.format(owner=owner, repo=repo), headers=headers)

if response.status_code == requests.codes.ok:
    data = response.json()
    latest_version = data["tag_name"]
    download_url = data["assets"][0]["browser_download_url"]
    os.chdir(repo_path)
    os.system(f"git pull origin {latest_version}")
    os.system(f"curl -O -L {download_url}")
    os.system("unzip -o latest.zip")
    os.system(f"rm latest.zip")


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
