import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from customer_table import CustomerTable
from customer_table_gui import CustomerTableGui
from payment_table import PaymentTable
from payment_table_gui import PaymentTableGui


class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Messie Jessie's Cleaning Service")
        self.geometry("1000x600")
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_buttons()

    def create_labels(self):
        title_label = ctk.CTkLabel(self, text="Messie Jessie's Cleaning Service")
        title_label.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="nsew")

    def create_buttons(self):
        customer_button = ctk.CTkButton(self, text="Customer Table", command=self.open_customer_table)
        customer_button.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        payment_button = ctk.CTkButton(self, text="Payment Table", command=self.open_payment_table)
        payment_button.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

    def open_customer_table(self):
        window = CustomerTableGui(self)
        window.grab_set()

    def open_payment_table(self):
        window = PaymentTableGui(self)
        window.grab_set()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = MainApplication()
    app.run()
