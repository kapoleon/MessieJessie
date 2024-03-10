import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from customer_table import CustomerTable


class CustomerTableGui:
    def __init__(self, parent):
        self.top_level = ctk.CTkToplevel(parent)
        self.top_level.title("Customer Table")

        self.notebook = ttk.Notebook(self.top_level)
        self.create_tabs()
        self.pack()

    def create_tabs(self):
        tab_one = TabOne(self.notebook)
        self.notebook.add(tab_one.frame, text="Add Customer")

        tab_two = TabTwo(self.notebook)
        self.notebook.add(tab_two.frame, text="Update Customer")

        tab_three = TabThree(self.notebook)
        self.notebook.add(tab_three.frame, text="View Customers")

        tab_four = TabFour(self.notebook)
        self.notebook.add(tab_four.frame, text="Delete Customer")

    def pack(self):
        self.notebook.pack(expand=1, fill="both")

    def grab_set(self):
        self.top_level.grab_set()


# This tab is for adding customers to the database
class TabOne:
    def __init__(self, parent):
        self.zip_code_entry = None
        self.state_entry = None
        self.city_entry = None
        self.address_entry = None
        self.phone_entry = None
        self.last_name_entry = None
        self.first_name_entry = None
        self.frame = ctk.CTkFrame(parent)
        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_entries()
        self.create_buttons()

    def create_labels(self):
        first_name_label = ctk.CTkLabel(self.frame, text="First Name:")
        first_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        last_name_label = ctk.CTkLabel(self.frame, text="Last Name:")
        last_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        phone_label = ctk.CTkLabel(self.frame, text="Phone:")
        phone_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        address_label = ctk.CTkLabel(self.frame, text="Address:")
        address_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        city_label = ctk.CTkLabel(self.frame, text="City:")
        city_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        state_label = ctk.CTkLabel(self.frame, text="State:")
        state_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        zip_code_label = ctk.CTkLabel(self.frame, text="Zip Code:")
        zip_code_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    def create_entries(self):
        self.first_name_entry = ctk.CTkEntry(self.frame)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.last_name_entry = ctk.CTkEntry(self.frame)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.phone_entry = ctk.CTkEntry(self.frame)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.address_entry = ctk.CTkEntry(self.frame)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.city_entry = ctk.CTkEntry(self.frame)
        self.city_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.state_entry = ctk.CTkEntry(self.frame)
        self.state_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        self.zip_code_entry = ctk.CTkEntry(self.frame)
        self.zip_code_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    def create_buttons(self):
        add_button = ctk.CTkButton(self.frame, text="Add Customer", command=self.add_customer)
        add_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def add_customer(self):
        customer_table = CustomerTable()
        customer_table.connect()
        customer_table.create_table()
        customer_table.add_customer(
            self.first_name_entry.get(),
            self.last_name_entry.get(),
            self.phone_entry.get(),
            self.address_entry.get(),
            self.city_entry.get(),
            self.state_entry.get(),
            self.zip_code_entry.get()
        )
        customer_table.disconnect()

        self.clear_entries()

    def clear_entries(self):
        self.first_name_entry.delete(0, "end")
        self.last_name_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.address_entry.delete(0, "end")
        self.city_entry.delete(0, "end")
        self.state_entry.delete(0, "end")
        self.zip_code_entry.delete(0, "end")


# This tab is for updating customers in the database
class TabTwo:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent)
        self.customer_id_entry = None
        self.zip_code_entry = None
        self.state_entry = None
        self.city_entry = None
        self.address_entry = None
        self.phone_entry = None
        self.last_name_entry = None
        self.first_name_entry = None

        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_entries()
        self.create_buttons()

    def create_labels(self):
        customer_id_label = ctk.CTkLabel(self.frame, text="Customer ID:")
        customer_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        first_name_label = ctk.CTkLabel(self.frame, text="First Name:")
        first_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        last_name_label = ctk.CTkLabel(self.frame, text="Last Name:")
        last_name_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        phone_label = ctk.CTkLabel(self.frame, text="Phone:")
        phone_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        address_label = ctk.CTkLabel(self.frame, text="Address:")
        address_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        city_label = ctk.CTkLabel(self.frame, text="City:")
        city_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        state_label = ctk.CTkLabel(self.frame, text="State:")
        state_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        zip_code_label = ctk.CTkLabel(self.frame, text="Zip Code:")
        zip_code_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

    def create_entries(self):
        self.customer_id_entry = ctk.CTkEntry(self.frame)
        self.customer_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.first_name_entry = ctk.CTkEntry(self.frame)
        self.first_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.last_name_entry = ctk.CTkEntry(self.frame)
        self.last_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.phone_entry = ctk.CTkEntry(self.frame)
        self.phone_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.address_entry = ctk.CTkEntry(self.frame)
        self.address_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.city_entry = ctk.CTkEntry(self.frame)
        self.city_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        self.state_entry = ctk.CTkEntry(self.frame)
        self.state_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        self.zip_code_entry = ctk.CTkEntry(self.frame)
        self.zip_code_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    def create_buttons(self):
        update_button = ctk.CTkButton(self.frame, text="Update Customer", command=self.update_customer)
        update_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def update_customer(self):
        customer_table = CustomerTable()
        customer_table.connect()
        customer_table.create_table()
        customer_table.update_customer(
            self.customer_id_entry.get(),
            self.first_name_entry.get(),
            self.last_name_entry.get(),
            self.phone_entry.get(),
            self.address_entry.get(),
            self.city_entry.get(),
            self.state_entry.get(),
            self.zip_code_entry.get()
        )
        customer_table.disconnect()

        self.clear_entries()

    def clear_entries(self):
        self.customer_id_entry.delete(0, "end")
        self.first_name_entry.delete(0, "end")
        self.last_name_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.address_entry.delete(0, "end")
        self.city_entry.delete(0, "end")
        self.state_entry.delete(0, "end")
        self.zip_code_entry.delete(0, "end")


# This tab is for viewing customers in the database
class TabThree:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent)
        self.tree = None
        self.create_widgets()

    def create_widgets(self):
        self.create_tree()
        self.create_buttons()

    def create_tree(self):
        self.tree = ttk.Treeview(self.frame, columns=(
            "ID", "First Name", "Last Name", "Phone", "Address", "City", "State", "Zip Code"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Customer ID")
        self.tree.heading("#2", text="First Name")
        self.tree.heading("#3", text="Last Name")
        self.tree.heading("#4", text="Phone")
        self.tree.heading("#5", text="Address")
        self.tree.heading("#6", text="City")
        self.tree.heading("#7", text="State")
        self.tree.heading("#8", text="Zip Code")
        self.tree.column("#0", width=50)
        self.tree.column("#1", width=100)
        self.tree.column("#2", width=100)
        self.tree.column("#3", width=100)
        self.tree.column("#4", width=200)
        self.tree.column("#5", width=100)
        self.tree.column("#6", width=100)
        self.tree.column("#7", width=100)
        self.tree.column("#8", width=100)
        self.tree.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    def create_buttons(self):
        view_button = ctk.CTkButton(self.frame, text="View Customers", command=self.view_customers)
        view_button.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    def view_customers(self):
        customer_table = CustomerTable()
        customer_table.connect()
        customer_table.create_table()
        customers = customer_table.get_all_customers()
        customer_table.disconnect()

        self.clear_tree()
        for customer in customers:
            self.tree.insert("", "end", text=customer[0], values=customer)

    def clear_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)


# This tab is for deleting customers from the database
class TabFour:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent)
        self.customer_id_entry = None
        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_entries()
        self.create_buttons()

    def create_labels(self):
        customer_id_label = ctk.CTkLabel(self.frame, text="Customer ID:")
        customer_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    def create_entries(self):
        self.customer_id_entry = ctk.CTkEntry(self.frame)
        self.customer_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    def create_buttons(self):
        delete_button = ctk.CTkButton(self.frame, text="Delete Customer", command=self.delete_customer)
        delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def delete_customer(self):
        customer_table = CustomerTable()
        customer_table.connect()
        customer_table.create_table()
        customer_table.delete_customer(self.customer_id_entry.get())
        customer_table.disconnect()

        self.clear_entries()

    def clear_entries(self):
        self.customer_id_entry.delete(0, "end")
