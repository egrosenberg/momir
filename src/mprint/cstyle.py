import os
import climage


class STYLE:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


def logStyled(text, style):
    os.system("")
    print(f'{style}{text}{STYLE.ENDC}')


def logImage(path):
    os.system("")
    output = climage.convert(path, is_unicode=True)
    print(output, end='')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
