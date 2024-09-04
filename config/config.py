import ttkbootstrap as ttk

class Config:
    def __init__(self):
        self.root = ttk.Window(themename="cosmo")
        self.root.title("Framboesa: FFUF GUI")
        self.root.iconbitmap('icon/framboesa.ico')
        self.root.resizable(width=True, height=True)
        self.theme_var = ttk.StringVar(value="cosmo")

config = Config()