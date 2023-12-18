import sys
from pyfiglet import Figlet
from random import choice

if len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    try:
        input_text = input('Input: ')
        custom_fig = Figlet(font=sys.argv[2])
        output = custom_fig.renderText(input_text)
        print(output)
    except Exception as e:
        print(f"Error: {e}")
elif len(sys.argv) == 1:
    input_text = input('Input: ')
    custom_fig = choice(Figlet.getFonts())
    output = custom_fig.renderText(input_text)
    print(output)
s