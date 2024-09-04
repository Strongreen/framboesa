import re
from ttkbootstrap.constants import *
from src.clean_ansi import clean_ansi

def format_output(line, log_area):
    line = clean_ansi(line)
    
    path_pattern = re.compile(r'(.*?)\s+\[Status:')
    status_pattern = re.compile(r'\[Status: (\d{3}), Size: \d+, Words: \d+, Lines: \d+, Duration: \d+ms\]')
    
    path_match = path_pattern.search(line)
    status_match = status_pattern.search(line)
    
    if path_match and status_match:
        path = path_match.group(1).strip()
        status_code = status_match.group(1).strip()
        status = status_match.group(0).strip()


        col1_width = 50 
        formatted_line = f"{path:<{col1_width}} \t\t\t\t\t\t {status}\n"


        if status_code.startswith('2'):
            tag = '200'
        elif status_code.startswith('3'):
            tag = '300'
        elif status_code.startswith('4'):
            tag = '400'
        elif status_code.startswith('5'):
            tag = '500'
        else:
            tag = None

        if tag:
            log_area.insert(END, formatted_line, tag)
        else:
            log_area.insert(END, formatted_line)
    else:
        log_area.insert(END, line)