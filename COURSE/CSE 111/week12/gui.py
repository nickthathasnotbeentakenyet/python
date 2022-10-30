import tkinter as tk
import number_entry as nent
import math

PI = math.pi

def main():
    root = tk.Tk()
    frm_main = tk.Frame(root, background='bisque')
    frm_main.master.title("Area of a circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    populate_main_window(frm_main)
    root.mainloop()

def populate_main_window(frm_main):
    lbl_radius = tk.Label(frm_main, text="Radius:", fg='teal', bg='bisque')
    ent_radius = nent.IntEntry(frm_main, 0, 10**10, width=20)
    txt_result = tk.Label(frm_main, text="Result:", fg='teal', bg='bisque')
    lbl_result = tk.Label(frm_main, width=15)
    btn_clear = tk.Button(frm_main, text="Clear", fg='white', bg='orange')
    

    lbl_radius.grid(row=0, column=0, padx=(10,5), pady=5, sticky="e")
    ent_radius.grid(row=0, column=1, padx=(3,5), pady=5, sticky="w")
    txt_result.grid(row=1, column=0, padx=(10,5), pady=5, sticky="e")
    lbl_result.grid(row=1, column=1, padx=(3,5), pady=5, sticky="w")
    btn_clear.grid(row=2, column=0 , padx=(10,5), pady=5)

    def calculate(event):
        try:
            radius = ent_radius.get()
            a = PI * radius**2
            lbl_result.config(text=f"{a:.2f}")
        except ValueError:
            lbl_result.config(text="")

    def clear():
        ent_radius.delete(0, tk.END)
        lbl_result.config(text="")
        ent_radius.focus()


    ent_radius.bind("<KeyRelease>", calculate)
    btn_clear.config(command=clear)
    ent_radius.focus()


if __name__ == "__main__":
    main()
