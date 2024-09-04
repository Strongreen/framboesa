from tkinter import Menu

def create_context_menu(widget):
    context_menu = Menu(widget, tearoff=0)
    context_menu.add_command(label="Copiar", command=lambda: widget.event_generate("<<Copy>>"))
    context_menu.add_command(label="Colar", command=lambda: widget.event_generate("<<Paste>>"))
    context_menu.add_command(label="Cortar", command=lambda: widget.event_generate("<<Cut>>"))
    
    widget.bind("<Button-3>", lambda event: context_menu.tk_popup(event.x_root, event.y_root))
