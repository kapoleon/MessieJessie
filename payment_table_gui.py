import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from payment_table import PaymentTable
from customer_table import CustomerTable


class PaymentTableGui:
    def __init__(self, parent):
        self.top_level = ctk.CTkToplevel(parent)
        self.top_level.title("Payment Table")

        self.notebook = ttk.Notebook(self.top_level)
        self.create_tabs()
        self.pack()

    def create_tabs(self):
        tab_one = TabOne(self.notebook)
        self.notebook.add(tab_one.frame, text="Add Payment")

        tab_two = TabTwo(self.notebook)
        self.notebook.add(tab_two.frame, text="View Payments")

        tab_three = TabThree(self.notebook)
        self.notebook.add(tab_three.frame, text="Payments by Customer")

    def pack(self):
        self.notebook.pack(expand=1, fill="both")

    def grab_set(self):
        self.top_level.grab_set()


# This tab is for adding a payment
class TabOne:
    def __init__(self, parent):
        self.customer_id_entry = None
        self.date_entry = None
        self.amount_entry = None
        self.frame = ctk.CTkFrame(parent)
        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_entries()
        self.create_buttons()

    def create_labels(self):
        customer_id_label = ctk.CTkLabel(self.frame, text="Customer ID:")
        customer_id_label.grid(row=0, column=0, sticky="w")

        date_label = ctk.CTkLabel(self.frame, text="Date:")
        date_label.grid(row=1, column=0, sticky="w")

        amount_label = ctk.CTkLabel(self.frame, text="Amount:")
        amount_label.grid(row=2, column=0, sticky="w")

    def create_entries(self):
        self.customer_id_entry = ctk.CTkEntry(self.frame)
        self.customer_id_entry.grid(row=0, column=1)

        self.date_entry = ctk.CTkEntry(self.frame)
        self.date_entry.grid(row=1, column=1)

        self.amount_entry = ctk.CTkEntry(self.frame)
        self.amount_entry.grid(row=2, column=1)

    def create_buttons(self):
        add_button = ctk.CTkButton(self.frame, text="Add Payment", command=self.add_payment)
        add_button.grid(row=3, column=0, columnspan=2)

    def add_payment(self):
        payment_table = PaymentTable()
        payment_table.connect()
        payment_table.create_table()
        payment_table.add_payment(self.customer_id_entry.get(), self.date_entry.get(), self.amount_entry.get())

        payment_table.disconnect()

        self.clear_entries()

    def clear_entries(self):
        self.customer_id_entry.delete(0, "end")
        self.date_entry.delete(0, "end")
        self.amount_entry.delete(0, "end")


class TabTwo:
    def __init__(self, parent):
        self.tree = None
        self.frame = ctk.CTkFrame(parent)
        self.create_widgets()

    def create_widgets(self):
        self.create_tree()
        self.create_buttons()

    def create_tree(self):
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Customer ID", "Date", "Amount"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Customer ID", text="Customer ID")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Amount", text="Amount")
        self.tree.pack(expand=1, fill="both")

    def create_buttons(self):
        view_button = ctk.CTkButton(self.frame, text="View Payments", command=self.view_payments)
        view_button.pack()

    def view_payments(self):
        payment_table = PaymentTable()
        payment_table.connect()
        payments = payment_table.get_all_payments()
        payment_table.disconnect()

        self.clear_tree()
        for payment in payments:
            self.tree.insert("", "end", values=payment)

    def clear_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)


class TabThree:
    def __init__(self, parent):
        self.customer_id_entry = None
        self.tree = None
        self.frame = ctk.CTkFrame(parent)
        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_entries()
        self.create_tree()
        self.create_buttons()

    def create_labels(self):
        customer_id_label = ctk.CTkLabel(self.frame, text="Customer ID:")
        customer_id_label.pack()

    def create_entries(self):
        self.customer_id_entry = ctk.CTkEntry(self.frame)
        self.customer_id_entry.pack()

    def create_tree(self):
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Customer ID", "Date", "Amount"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Customer ID", text="Customer ID")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Amount", text="Amount")
        self.tree.pack(expand=1, fill="both")

    def create_buttons(self):
        view_button = ctk.CTkButton(self.frame, text="View Payments", command=self.view_payments)
        view_button.pack()

    def view_payments(self):
        payment_table = PaymentTable()
        payment_table.connect()
        payments = payment_table.get_payments_by_customer(self.customer_id_entry.get())
        payment_table.disconnect()

        self.clear_tree()
        for payment in payments:
            self.tree.insert("", "end", values=payment)

    def clear_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
