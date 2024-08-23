def windowDialog(txt):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw() 

    tk.messagebox.showinfo("Message", txt)