import re

def clean_ansi(text):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*[mKJHfABCD]')
    return ansi_escape.sub('', text)