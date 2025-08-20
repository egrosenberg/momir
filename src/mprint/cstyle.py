import os
from climage import convert, color_to_flags, color_types


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


def logStyled(text, style, end='\n'):
    os.system("")
    print(f'{style}{text}{STYLE.ENDC}', end=end)


def logImage(path):
    os.system("")
    output = convert(path, is_unicode=True, **
                     color_to_flags(color_types.truecolor))
    print(output, end='')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
