import ttkbootstrap as ttk
import sys

sys.path.append('..')
sys.path.append('/src')
from src.start_ffuf import start_ffuf
from src.create_widgets import create_widgets
sys.path.append('..')
sys.path.append('/config')
from config.config import config

def main():

    entry_url, entry_wordlist, method_var, entry_headers, entry_body, entry_cookies, entry_search, entry_fc, entry_fl, entry_fs, entry_delay, log_area = create_widgets(config.root, config.theme_var)
    
    ttk.Button(config.root, text="Scan", width=30, command=lambda: start_ffuf(config.root, entry_url, entry_wordlist, method_var, entry_headers, entry_body, entry_cookies, entry_search, entry_fc, entry_fl, entry_fs, entry_delay, log_area)).grid(row=15, column=0, columnspan=2, pady=10)
   
    config.root.mainloop()

if __name__ == "__main__":
    main()