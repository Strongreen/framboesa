import subprocess
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Menu

def change_theme(theme_var, root):
    selected_theme = theme_var.get()
    root.style.theme_use(selected_theme)

def create_context_menu(widget):
    """Cria um menu de contexto com as opções Copiar, Colar e Cortar."""
    context_menu = Menu(widget, tearoff=0)
    context_menu.add_command(label="Copiar", command=lambda: widget.event_generate("<<Copy>>"))
    context_menu.add_command(label="Colar", command=lambda: widget.event_generate("<<Paste>>"))
    context_menu.add_command(label="Cortar", command=lambda: widget.event_generate("<<Cut>>"))
    
    widget.bind("<Button-3>", lambda event: context_menu.tk_popup(event.x_root, event.y_root))


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

def start_ffuf(entry_url, entry_wordlist, method_var,header_var, log_area):
    target_url = entry_url.get()
    wordlist = entry_wordlist.get()
    method = method_var.get()
    header = header_var.get()

    ''' para testes : http://testphp.vulnweb.com/FUZZ - quisckhits.txt '''
    command = f"ffuf -u {target_url} -w {wordlist} -X {method} -H {header}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    log_area.delete(1.0, END)

    for line in process.stdout:
        log_area.insert(END, line.decode())
        log_area.see(END)

def main():
    root = ttk.Window(themename="cosmo")

    root.title("FFUF GUI")

    theme_var = ttk.StringVar(value="cosmo")
    entry_url, entry_wordlist, method_var, log_area = create_widgets(root, theme_var)


    ttk.Button(root, text="Start", width=30, command=lambda: start_ffuf(entry_url, entry_wordlist, method_var, log_area)).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
