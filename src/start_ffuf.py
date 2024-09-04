import subprocess
from ttkbootstrap.constants import *
from src.apply_tags import apply_tags
from src.format_output import format_output


def start_ffuf(root, entry_url, entry_wordlist, method_var, entry_headers, entry_body, entry_cookies, entry_search, entry_fc, entry_fl, entry_fs, entry_delay, log_area):
    target_url = entry_url.get()
    wordlist = entry_wordlist.get()
    method = method_var.get()
    headers = entry_headers.get()
    body = entry_body.get("1.0", END).strip()
    cookies = entry_cookies.get() 
    search = entry_search.get()
    filter_status = entry_fc.get()
    filter_lines = entry_fl.get()
    filter_size = entry_fs.get() 
    delay = entry_delay.get()

    command = f"ffuf -u {target_url} -w {wordlist} -X {method} -c"
    
    if body:
        command += f" -d \"{body}\""
    if headers != "com esse formato: key:value,":
        command += f" -H \"{headers}\""
    if cookies != "com esse formato: key=value;":
        command += f" -b \"{cookies}\""
    if filter_status != "para usar no log":
        command += f" -fc {filter_status}"
    if filter_lines != "para usar no log":
        command += f" -fl {filter_lines}"
    if filter_size != "para usar no log":
        command += f" -fs {filter_size}"
    if search != "para usar no log":
        command += f" -s \"{search}\""
    if delay:
        command += f" -p {delay}"


    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    log_area.delete(1.0, END)
    
    apply_tags(log_area)

    for line in process.stdout:
        format_output(line.decode(),log_area)
        log_area.see(END)
        log_area.update_idletasks()
