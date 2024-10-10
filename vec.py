import datetime
import tkinter as tk
from PIL import Image, ImageTk

logs = tk.Tk()
logs.title("Vecuma aprekinasanas kalk")
logs.geometry("400x500")

virsraksts = tk.Label(logs, text="Interneta veikals:", font="a")
virsraksts.grid(row=0, column=1, padx=15, pady=15)

vards_ievade = tk.Label(logs, text="Product vards:")
vards_ievade.grid(row=1, column=0, padx=5, pady=5)
vards_ievade = tk.Entry(logs, bg="red")
vards_ievade.grid(row=1, column=1)

gads_ievade = tk.Label(logs, text="gads:")
gads_ievade.grid(row=2, column=0, padx=5, pady=5)
gads_ievade = tk.Entry(logs, bg="red")
gads_ievade.grid(row=2, column=1)

menesis_ievade = tk.Label(logs, text="menesis:")
menesis_ievade.grid(row=3, column=0, padx=5, pady=5)
menesis_ievade = tk.Entry(logs, bg="red")
menesis_ievade.grid(row=3, column=1)

diena_ievade = tk.Label(logs, text="diena:")
diena_ievade.grid(row=4, column=0, padx=5, pady=5)
diena_ievade = tk.Entry(logs, bg="red")
diena_ievade.grid(row=4, column=1)

listbox = tk.Listbox(logs, width=50)
listbox.grid(row=6, columnspan=2, padx=5, pady=5)

def get_info():
    vards = str(vards_ievade.get())
    gads = int(gads_ievade.get())
    menesis = int(menesis_ievade.get())
    diena = int(diena_ievade.get())

    dzimsana = datetime.date(gads, menesis, diena)
    today = datetime.date.today()

    if dzimsana.month < today.month or (dzimsana.month == today.month and dzimsana.day <= today.day):
        vecums = today.year - dzimsana.year
    else:
        vecums = today.year - dzimsana.year - 1

    # Clear the listbox before adding a new entry
    listbox.delete(0, tk.END)  
    listbox.insert(tk.END, f"Sveicināti {vards}, jums ir {vecums} gadi")

    # Clear the input fields
    vards_ievade.delete(0, tk.END)
    gads_ievade.delete(0, tk.END)
    menesis_ievade.delete(0, tk.END)
    diena_ievade.delete(0, tk.END)

add_button = tk.Button(logs, text="Aprekinat", command=get_info)
add_button.grid(row=7, columnspan=2, pady=10)

logs.mainloop()
