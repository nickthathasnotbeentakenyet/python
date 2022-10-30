import tkinter as tk
import math
import re

COLOR = '#395778'
RESULT_COLOR = '#9f45b0'


def main():
    root = tk.Tk()
    root.geometry('400x180')
    root.iconbitmap('week12/calc.ico')
    tk.Frame(root).master.title("Area of a circle")
    f_top = tk.Frame(root)
    f_mid = tk.Frame(root)
    f_bot = tk.Frame(root)
    f_bot = tk.LabelFrame(text="Clear all input & output", fg=COLOR)

    populate_main_window(f_top,f_mid, f_bot)
    root.mainloop()
    
def populate_main_window(f_top,f_mid, f_bot):
    lbl_radius = tk.Label(f_top, text="Radius:", fg=COLOR, font=12)
    check = (f_top.register(is_valid), "%P")
    ent_radius = tk.Entry(f_top, font=12,fg=COLOR, justify=tk.RIGHT, validate="key", validatecommand=check)
    txt_result = tk.Label(f_mid, text="Result:", fg=COLOR, font=12)
    lbl_result = tk.Label(f_mid, font=12, fg=RESULT_COLOR)
    btn_clear = tk.Button(f_bot, text="Clear", fg='white', bg=COLOR, activeforeground=COLOR, font = 12)

    f_top.pack(fill=tk.X)
    f_mid.pack(fill=tk.X)
    f_bot.pack(fill=tk.X)
    lbl_radius.pack(side=tk.LEFT, padx=5,pady=10)
    ent_radius.pack(side=tk.RIGHT, padx=(0,5))
    txt_result.pack(side=tk.LEFT, padx=5, pady=10)
    lbl_result.pack(side=tk.RIGHT, padx=5, pady=10)
    btn_clear.pack(fill=tk.X, padx=5,pady=10)

    def calculate(event):
        try:
            radius = float(ent_radius.get())
            a = math.pi * radius**2
            lbl_result.config(text=f"{a:.2f}cm")
        except ValueError:
            if ent_radius.get() == '': lbl_result.config(text="") #to avoid printing error message when incorrect input erased
            else: lbl_result.config(text="Error: not a number")
    def clear():
        ent_radius.delete(0, tk.END)
        lbl_result.config(text="")
        ent_radius.focus()


    ent_radius.bind("<KeyRelease>", calculate)
    btn_clear.config(command=clear)
    ent_radius.focus()

def is_valid(newval):
    return re.match("[0-9]*\.?[0-9]*", newval) is not None
         

main()