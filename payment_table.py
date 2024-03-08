import sqlite3
from base_table import BaseTable
from customer_table import CustomerTable


class PaymentTable(BaseTable):

    def create_table(self):
        try:
            self.connect()
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS payment (
                    id INTEGER PRIMARY KEY,
                    customer_id INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    amount INTEGER NOT NULL
                )
            """)
            self.conn.commit()
            print("Table created successfully!")
        except Exception as e:
            print(f"Error creating table: {e}")

    def add_payment(self, customer_id, date, amount):
        try:
            self.connect()
            self.cursor.execute("""
                INSERT INTO payment (customer_id, date, amount)
                VALUES (?, ?, ?)
            """, (customer_id, date, amount))
            self.conn.commit()
            print("Payment added successfully!")
        except Exception as e:
            print(f"Error adding payment: {e}")

    def get_payment(self, payment_id):
        try:
            self.connect()
            self.cursor.execute("""
                SELECT * FROM payment WHERE id = ?
            """, (payment_id,))
            payment = self.cursor.fetchone()
            return payment
        except Exception as e:
            print(f"Error getting payment: {e}")

    def get_all_payments(self):
        try:
            self.connect()
            self.cursor.execute("""
                SELECT * FROM payment
            """)
            payments = self.cursor.fetchall()
            return payments
        except Exception as e:
            print(f"Error getting payments: {e}")

    def get_payments_by_customer(self, customer_id):
        try:
            self.connect()
            self.cursor.execute("""
                SELECT * FROM payment WHERE customer_id = ?
            """, (customer_id,))
            payments = self.cursor.fetchall()
            return payments
        except Exception as e:
            print(f"Error getting payments: {e}")

    def update_payment(self, payment_id, customer_id, date, amount):
        try:
            self.connect()
            self.cursor.execute("""
                UPDATE payment
                SET customer_id = ?, date = ?, amount = ?
                WHERE id = ?
            """, (customer_id, date, amount, payment_id))
            self.conn.commit()
            print("Payment updated successfully!")
        except Exception as e:
            print(f"Error updating payment: {e}")

    def delete_payment(self, payment_id):
        try:
            self.connect()
            self.cursor.execute("""
                DELETE FROM payment WHERE id = ?
            """, (payment_id,))
            self.conn.commit()
            print("Payment deleted successfully!")
        except Exception as e:
            print(f"Error deleting payment: {e}")
