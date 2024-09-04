import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from change_theme import change_theme

def create_widgets(root, theme_var):

    ttk.Label(root, text="Theme:", width=30).pack(pady=5)
    ttk.OptionMenu(root, theme_var, *root.style.theme_names(), command=lambda _: change_theme(theme_var, root)).pack(pady=5)

    ttk.Label(root, text="Target URL:").pack(pady=5)
    entry_url = ttk.Entry(root, width=50)
    entry_url.pack(pady=5)
    
    ttk.Label(root, text="Wordlist:").pack(pady=5)
    entry_wordlist = ttk.Entry(root, width=50)
    entry_wordlist.pack(pady=5)

    ttk.Label(root, text="HTTP Method:", width=30).pack(pady=5)
    method_var = ttk.StringVar(value="GET")
    ttk.OptionMenu(root, method_var, "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "TRACE", "HEAD", "CONNECT").pack(pady=5)

    log_area = ttk.Text(root, height=15)
    log_area.pack(pady=5)

    return entry_url, entry_wordlist, method_var, log_area

