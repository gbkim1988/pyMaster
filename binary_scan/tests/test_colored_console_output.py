import sys
from termcolor import colored, cprint

'''
Text Properties

    Text colors:

            grey
            red
            green
            yellow
            blue
            magenta
            cyan
            white

    Text highlights:

            on_grey
            on_red
            on_green
            on_yellow
            on_blue
            on_magenta
            on_cyan
            on_white

    Attributes:

            bold
            dark
            underline
            blink
            reverse
            concealed

'''

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
text2 = colored('Hello, World!', 'yellow', attrs=['reverse', 'blink'])
print(text + text2)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan', attrs=['underline'])
print_yellow_on_cyan = lambda x: cprint(x, 'yellow', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')
print_yellow_on_cyan('Hello, World!')
print_yellow_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)