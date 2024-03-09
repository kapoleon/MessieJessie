from base_table import BaseTable
import sqlite3


class CustomerTable(BaseTable):
    def create_table(self):
        try:
            self.connect()
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS customer (
                    id INTEGER PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    address TEXT NOT NULL,
                    city TEXT NOT NULL,
                    state TEXT NOT NULL,
                    zip_code TEXT NOT NULL
                )
            """)
            self.conn.commit()
            print("Table created successfully!")
        except Exception as e:
            print(f"Error creating table: {e}")

    def add_customer(self, first_name, last_name, phone, address, city, state, zip_code):
        try:
            self.connect()
            self.cursor.execute("""
                    INSERT INTO customer (first_name, last_name, phone, address, city, state, zip_code)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (first_name, last_name, phone, address, city, state, zip_code))
            self.conn.commit()
            print("Customer added successfully!")
        except Exception as e:
            print(f"Error adding customer: {e}")

    def get_customer(self, customer_id):
        try:
            self.connect()
            self.cursor.execute("""
                SELECT * FROM customer WHERE id = ?
            """, (customer_id,))
            customer = self.cursor.fetchone()
            return customer
        except Exception as e:
            print(f"Error getting customer: {e}")

    def get_all_customers(self):
        try:
            self.connect()
            self.cursor.execute("""
                SELECT * FROM customer
            """)
            customers = self.cursor.fetchall()
            return customers
        except Exception as e:
            print(f"Error getting customers: {e}")

    def update_customer(self, customer_id, first_name, last_name, phone, address, city, state, zip_code):
        try:
            self.connect()
            self.cursor.execute("""
                UPDATE customer
                SET first_name = ?, last_name = ?, phone = ?, address = ?, city = ?, state = ?, zip_code = ?
                WHERE id = ?
            """, (first_name, last_name, phone, address, city, state, zip_code, customer_id))
            self.conn.commit()
            print("Customer updated successfully!")
        except Exception as e:
            print(f"Error updating customer: {e}")

    def delete_customer(self, customer_id):
        try:
            self.connect()
            self.cursor.execute("""
                DELETE FROM customer WHERE id = ?
            """, (customer_id,))
            self.conn.commit()
            print("Customer deleted successfully!")
        except Exception as e:
            print(f"Error deleting customer: {e}")

    def delete_all_customers(self):
        try:
            self.connect()
            self.cursor.execute("""
                DELETE FROM customer
            """)
            self.conn.commit()
            print("All customers deleted successfully!")
        except Exception as e:
            print(f"Error deleting all customers: {e}")

    def get_customer_by_name(self, first_name, last_name):
        try:
            self.connect()
            self.cursor.execute("""
                SELECT * FROM customer WHERE first_name = ? AND last_name = ?
            """, (first_name, last_name))
            customer = self.cursor.fetchone()
            return customer
        except Exception as e:
            print(f"Error getting customer: {e}")









