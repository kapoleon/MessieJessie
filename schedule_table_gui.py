import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from schedule_table import ScheduleTable


class ScheduleTableGui:
    def __init__(self, parent):
        self.top_level = ctk.CTkToplevel(parent)
        self.top_level.title("Schedule Table")

        self.notebook = ttk.Notebook(self.top_level)
        self.create_tabs()
        self.pack()

    def create_tabs(self):
        tab_one = TabOne(self.notebook)
        self.notebook.add(tab_one.frame, text="Add Schedule")

        tab_two = TabTwo(self.notebook)
        self.notebook.add(tab_two.frame, text="View Schedule")

        tab_three = TabThree(self.notebook)
        self.notebook.add(tab_three.frame, text="Update Schedule")

        tab_four = TabFour(self.notebook)
        self.notebook.add(tab_four.frame, text="Delete Schedule")

    def pack(self):
        self.notebook.pack(expand=True, fill="both")

    def grab_set(self):
        self.top_level.grab_set()


class TabOne:
    def __init__(self, parent):
        self.customer_id_entry = None
        self.date_entry = None
        self.time_entry = None
        self.frame = ctk.CTkFrame(parent)
        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_entries()
        self.create_buttons()

    def create_labels(self):
        customer_id_label = ctk.CTkLabel(self.frame, text="Customer ID:")
        customer_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        date_label = ctk.CTkLabel(self.frame, text="Date:")
        date_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        time_label = ctk.CTkLabel(self.frame, text="Time:")
        time_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    def create_entries(self):
        self.customer_id_entry = ctk.CTkEntry(self.frame)
        self.customer_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.date_entry = ctk.CTkEntry(self.frame)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.time_entry = ctk.CTkEntry(self.frame)
        self.time_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    def create_buttons(self):
        add_button = ctk.CTkButton(self.frame, text="Add Schedule", command=self.add_schedule)
        add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def add_schedule(self):
        customer_id = self.customer_id_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        schedule_table = ScheduleTable()
        schedule_table.connect()
        schedule_table.create_table()
        schedule_table.add_schedule(customer_id, date, time)

        schedule_table.disconnect()

        self.clear_entries()

    def clear_entries(self):
        self.customer_id_entry.delete(0, "end")
        self.date_entry.delete(0, "end")
        self.time_entry.delete(0, "end")


# This tab is for viewing schedules
class TabTwo:
    def __init__(self, parent):
        self.tree = None
        self.frame = ctk.CTkFrame(parent)
        self.create_widgets()

    def create_widgets(self):
        self.create_tree()
        self.create_buttons()

    def create_tree(self):
        self.tree = ttk.Treeview(self.frame, columns=("Customer ID", "Date", "Time"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("Customer ID", text="Customer ID")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Time", text="Time")
        self.tree.column("#0", width=50)
        self.tree.column("Customer ID", width=100)
        self.tree.column("Date", width=100)
        self.tree.column("Time", width=100)
        self.tree.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.populate_tree()

    def create_buttons(self):
        refresh_button = ctk.CTkButton(self.frame, text="Refresh", command=self.populate_tree)
        refresh_button.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    def populate_tree(self):
        schedule_table = ScheduleTable()
        schedule_table.connect()
        schedule_table.create_table()
        schedules = schedule_table.get_all_schedules()
        schedule_table.disconnect()

        self.clear_tree()

        for schedule in schedules:
            self.tree.insert("", "end", text=schedule[0], values=(schedule[1], schedule[2], schedule[3]))

    def clear_tree(self):
        for record in self.tree.get_children():
            self.tree.delete(record)


# This tab is for updating schedules
class TabThree:
    def __init__(self, parent):
        self.schedule_id_entry = None
        self.customer_id_entry = None
        self.date_entry = None
        self.time_entry = None
        self.frame = ctk.CTkFrame(parent)
        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_entries()
        self.create_buttons()

    def create_labels(self):
        schedule_id_label = ctk.CTkLabel(self.frame, text="Schedule ID:")
        schedule_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        customer_id_label = ctk.CTkLabel(self.frame, text="Customer ID:")
        customer_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        date_label = ctk.CTkLabel(self.frame, text="Date:")
        date_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        time_label = ctk.CTkLabel(self.frame, text="Time:")
        time_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    def create_entries(self):
        self.schedule_id_entry = ctk.CTkEntry(self.frame)
        self.schedule_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.customer_id_entry = ctk.CTkEntry(self.frame)
        self.customer_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.date_entry = ctk.CTkEntry(self.frame)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.time_entry = ctk.CTkEntry(self.frame)
        self.time_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    def create_buttons(self):
        update_button = ctk.CTkButton(self.frame, text="Update Schedule", command=self.update_schedule)
        update_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def update_schedule(self):
        schedule_id = self.schedule_id_entry.get()
        customer_id = self.customer_id_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        schedule_table = ScheduleTable()
        schedule_table.connect()
        schedule_table.create_table()
        schedule_table.update_schedule(schedule_id, customer_id, date, time)
        schedule_table.disconnect()

        self.clear_entries()

    def clear_entries(self):
        self.schedule_id_entry.delete(0, "end")
        self.customer_id_entry.delete(0, "end")
        self.date_entry.delete(0, "end")
        self.time_entry.delete(0, "end")


# This tab is for deleting schedules
class TabFour:
    def __init__(self, parent):
        self.schedule_id_entry = None
        self.frame = ctk.CTkFrame(parent)
        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_entries()
        self.create_buttons()

    def create_labels(self):
        schedule_id_label = ctk.CTkLabel(self.frame, text="Schedule ID:")
        schedule_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    def create_entries(self):
        self.schedule_id_entry = ctk.CTkEntry(self.frame)
        self.schedule_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    def create_buttons(self):
        delete_button = ctk.CTkButton(self.frame, text="Delete Schedule", command=self.delete_schedule)
        delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def delete_schedule(self):
        schedule_id = self.schedule_id_entry.get()

        schedule_table = ScheduleTable()
        schedule_table.connect()
        schedule_table.create_table()
        schedule_table.delete_schedule(schedule_id)
        schedule_table.disconnect()

        self.clear_entries()

    def clear_entries(self):
        self.schedule_id_entry.delete(0, "end")
