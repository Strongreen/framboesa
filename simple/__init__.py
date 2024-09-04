import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from create_widgets import create_widgets
from start_ffuf import start_ffuf

def main():
    root = ttk.Window(themename="cosmo")
    root.title("Framboesa: FFUF GUI")
    root.iconbitmap('framboesa.ico')

    theme_var = ttk.StringVar(value="cosmo")
    entry_url, entry_wordlist, method_var, log_area = create_widgets(root, theme_var)


    ttk.Button(root, text="Start", width=30, command=lambda: start_ffuf(entry_url, entry_wordlist, method_var, log_area)).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
