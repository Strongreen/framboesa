def change_theme(theme_var, root):
    selected_theme = theme_var.get()
    root.style.theme_use(selected_theme)