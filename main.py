# Import stuff
import os
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from pygments.lexers import PowerShellLexer
from pygments.styles import get_style_by_name

# Welcome message
os.system("cls")
os.system("title Command Prompt but Better")
print("Welcome to Command Prompt but Better!")
print("Made by DarkDev#2048")
print("\n\n")

# Custom style for syntax highlighting
style = Style.from_dict({
    "prompt": "#1EAF50",
    "output": ""
})

# Execute & highlight code
def command_line():
    session = PromptSession(lexer=PygmentsLexer(PowerShellLexer), completer=PathCompleter(), style=style)
    while True:
        try:
            command = session.prompt(os.getcwd() + "~"  + "$ ")
            if command.startswith("cd "):
                directory = command[3:]
                try:
                    os.chdir(directory)
                except:
                    print("The system cannot find the path specified.")
            else:
                os.system(command)

            if ":" in command and command.index(":") > 0 and not "cd" in command:
                print("To \'CD\' into a drive, please use \'CD DRIVE:\\\' instead.")

        except KeyboardInterrupt:
            print("Keyboard Interrupt..\n")
            break

command_line()
