from os import name
import tkinter as tk
from tkinter import messagebox
from turtle import bgcolor
from PIL import Image, ImageTk
class Product:
    def __init__(self, name, gads, menesis, diena):
        self.name = name
        self.gads = gads
        self.menesis = menesis
        self.diena=diena


class ShoppingCart:
    def __init__(self):
        self.name = []

    def add_product_to_cart(self, name):
        self.name.append(name)
        return f"Added product: {name.name}"

    
    def get_total_gads(self):
        total = sum(name.get_total_gads() for name in self.name)
        return f"Total gads: {total:.2f} EUR"

    def clear_cart(self):
        self.name.clear()
        return ""

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Calc")
        self.master.geometry("400x550")
        #self.master.configure(bg="purple")
        self.cart = ShoppingCart()

        # Create input fields
        self.virsraksts=tk.Label(master, text="Calc:", font="a",)
        self.virsraksts.grid(row=0, column=1, padx=15, pady=15)
        self.name_label = tk.Label(master, text="Vārds:")
        self.name_label.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1)

        self.gads_label = tk.Label(master, text="Gads:")
        self.gads_label.grid(row=2, column=0, padx=5, pady=5)
        self.gads_entry = tk.Entry(master)
        self.gads_entry.grid(row=2, column=1)

        self.menesis_label = tk.Label(master, text="Menesis:")
        self.menesis_label.grid(row=3, column=0, padx=5, pady=5)
        self.menesis_entry = tk.Entry(master)
        self.menesis_entry.grid(row=3, column=1)
        
        self.diena_label = tk.Label(master, text="diena:")
        self.diena_label.grid(row=4, column=0, padx=5, pady=5)
        self.diena_entry = tk.Entry(master)
        self.diena_entry.grid(row=4, column=1)

        # Add product button
        self.add_button = tk.Button(master, text="Diena", command=self.add_to_cart)
        self.add_button.grid(row=5, columnspan=2, pady=10)
        self.add_button.configure()

        # Clear cart button
        #self.clear_button = tk.Button(master, text="Clear Cart", command=self.clear_cart)
        #self.clear_button.grid(row=7, columnspan=2, pady=10)
        #self.clear_button.configure(bg="red")

        # Listbox to show cart items
        self.cart_listbox = tk.Listbox(master, width=50)
        self.cart_listbox.grid(row=6, columnspan=2, padx=5, pady=5)
        self.cart_listbox.configure()

        

        # Label to display total gads
        self.total_label = tk.Label(master, text="Total gads: 0.00 EUR")
        self.total_label.grid(row=7, columnspan=2)
        self.total_label.configure()

    def add_to_cart(self):
        name = self.name_entry.get()
        try:
            gads = float(self.gads_entry.get())
            menesis = int(self.menesis_entry.get())
            diena = int(self.diena_entry.get())
        except ValueError:
            messagebox.showerror("Ievadi pareizi")
            return

        name = Product(name, gads, menesis, diena)
        self.cart.add_product_to_cart(name)
        self.cart_listbox.insert(tk.END, f"{name} Tu esi {gads:.2f} Veca un {menesis} menesi, {diena} diena")
        self.update_total_gads()

        # Clear input fields
        self.name_entry.delete(0, tk.END)
        self.gads_entry.delete(0, tk.END)
        self.menesis_entry.delete(0, tk.END)
        self.diena_entry.delete(0, tk.END)

    
    def update_total_gads(self):
        total = self.cart.get_total_gads()
        self.total_label.config(text=total)

if __name__ == "__main__":
    master = tk.Tk()
    app = App(master)
    master.mainloop()