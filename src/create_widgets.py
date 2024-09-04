import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.create_context_menu import create_context_menu
from src.add_placeholder import add_placeholder
from src.change_theme import change_theme


def create_widgets(root, theme_var):

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    ttk.Label(root, text="Theme:").grid(row=0, column=0, padx=1, sticky="nw")
    ttk.OptionMenu(root, theme_var, *root.style.theme_names(), command=lambda _: change_theme(theme_var, root)).grid(row=0, column=0, pady=2, sticky="n")

    ttk.Label(root, text="HTTP Method:").grid(row=1, column=0, padx=1, sticky="nw")
    method_var = ttk.StringVar(value="GET")
    ttk.OptionMenu(root, method_var, "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "TRACE", "HEAD", "CONNECT").grid(row=1, column=0, pady=2, sticky="n")

    ttk.Label(root, text="Delay:").grid(row=2, column=0, padx=1, sticky="nw")
    entry_delay = ttk.Entry(root, width=5)
    entry_delay.grid(row=2, column=0, padx=10, pady=2, sticky="n")
    create_context_menu(entry_delay)

    ttk.Label(root, text="Target URL:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_url = ttk.Entry(root, width=30)
    entry_url.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    add_placeholder(entry_url, "http://testphp.vulnweb.com/FUZZ")
    create_context_menu(entry_url)

    
    ttk.Label(root, text="Wordlist:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_wordlist = ttk.Entry(root, width=30)
    entry_wordlist.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    add_placeholder(entry_wordlist, "..\\wordlists\\quickhits.txt")
    create_context_menu(entry_wordlist)

    ttk.Label(root, text="Headers:").grid(row=0, column=1, pady=10, padx=5, sticky="e")
    entry_headers = ttk.Entry(root, width=30)
    entry_headers.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    add_placeholder(entry_headers, "com esse formato: key:value,")
    create_context_menu(entry_headers)

    ttk.Label(root, text="Cookies:").grid(row=1, column=1, padx=10, pady=5, sticky="e")
    entry_cookies = ttk.Entry(root, width=30)
    entry_cookies.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    add_placeholder(entry_cookies, "com esse formato: key=value;")
    create_context_menu(entry_cookies)

    ttk.Label(root, text="Request Body:").grid(row=3, column=0, padx=1, pady=2, sticky="nw")
    entry_body = ttk.Text(root, height=5, width=35)
    entry_body.grid(row=4, column=0, padx=10, pady=2, sticky="nw")
    create_context_menu(entry_body)

    log_area = ttk.Text(root, height=15 )
    log_area.grid(row=10, column=0, ipadx=250, pady=20, rowspan=2, columnspan=4,sticky="s")
    create_context_menu(log_area)

    ttk.Label(root, text="Search:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_search = ttk.Entry(root, width=30)
    entry_search.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    create_context_menu(entry_search)
    add_placeholder(entry_search, "para usar no log")

    ttk.Label(root, text="Filter Status:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_fc = ttk.Entry(root, width=30)
    entry_fc.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    add_placeholder(entry_fc, "para usar no log")
    create_context_menu(entry_fc)

    ttk.Label(root, text="Filter Count:").grid(row=3, column=1, padx=10, pady=5, sticky="e")
    entry_fl = ttk.Entry(root, width=30)
    entry_fl.grid(row=3, column=2, padx=10, pady=5, sticky="w")
    add_placeholder(entry_fl, "para usar no log")
    create_context_menu(entry_fl)

    ttk.Label(root, text="Filter Size:").grid(row=4, column=1, padx=10, pady=5, sticky="e")
    entry_fs = ttk.Entry(root, width=30)
    entry_fs.grid(row=4, column=2, padx=10, pady=5, sticky="w")
    add_placeholder(entry_fs, "para usar no log")
    create_context_menu(entry_fs)

    return entry_url, entry_wordlist, method_var, entry_headers, entry_body, entry_cookies, entry_search, entry_fc, entry_fl, entry_fs, entry_delay, log_area