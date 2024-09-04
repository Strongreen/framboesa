import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.style = ttk.Style()
    entry.style.configure('Placeholder.TEntry', foreground='grey')
    entry.configure(style='Placeholder.TEntry')

    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, END)
            entry.configure(style='TEntry')

    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry.configure(style='Placeholder.TEntry')

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
