def windowDialog(txt):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()  # メインウィンドウを表示しない

    tk.messagebox.showinfo("Message", txt)