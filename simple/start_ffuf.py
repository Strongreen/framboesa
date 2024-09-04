import subprocess
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def start_ffuf(entry_url, entry_wordlist, method_var, log_area):
    target_url = entry_url.get()
    wordlist = entry_wordlist.get()
    method = method_var.get()

    command = f"ffuf -u {target_url} -w {wordlist} -X {method}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    log_area.delete(1.0, END)

    for line in process.stdout:
        log_area.insert(END, line.decode())
        log_area.see(END)
        log_area.update_idletasks()