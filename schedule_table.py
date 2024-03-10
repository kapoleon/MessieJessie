from base_table import BaseTable
import sqlite3


class ScheduleTable(BaseTable):

    def create_table(self):
        try:
            self.connect()
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS schedule (
                    id INTEGER PRIMARY KEY,
                    customer_id INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL
                )
            """)
            self.conn.commit()
            print("Table created successfully!")
        except Exception as e:
            print(f"Error creating table: {e}")

    def add_schedule(self, customer_id, date, time):
        try:
            self.connect()
            self.cursor.execute("""
                    INSERT INTO schedule (customer_id, date, time)
                    VALUES (?, ?, ?)
                """, (customer_id, date, time))
            self.conn.commit()
            print("Schedule added successfully!")
        except Exception as e:
            print(f"Error adding schedule: {e}")

    def get_schedule(self, schedule_id):
        try:
            self.connect()
            self.cursor.execute("""
                SELECT * FROM schedule WHERE id = ?
            """, (schedule_id,))
            schedule = self.cursor.fetchone()
            return schedule
        except Exception as e:
            print(f"Error getting schedule: {e}")

    def get_all_schedules(self):
        try:
            self.connect()
            self.cursor.execute("""
                SELECT * FROM schedule
            """)
            schedules = self.cursor.fetchall()
            return schedules
        except Exception as e:
            print(f"Error getting schedules: {e}")

    def get_schedule_by_customer_id(self, customer_id):
        try:
            self.connect()
            self.cursor.execute("""
                SELECT * FROM schedule WHERE customer_id = ?
            """, (customer_id,))
            schedules = self.cursor.fetchall()
            return schedules
        except Exception as e:
            print(f"Error getting schedules: {e}")

    def update_schedule(self, schedule_id, customer_id, date, time):
        try:
            self.connect()
            self.cursor.execute("""
                UPDATE schedule
                SET customer_id = ?, date = ?, time = ?
                WHERE id = ?
            """, (customer_id, date, time, schedule_id))
            self.conn.commit()
            print("Schedule updated successfully!")
        except Exception as e:
            print(f"Error updating schedule: {e}")

    def delete_schedule(self, schedule_id):
        try:
            self.connect()
            self.cursor.execute("""
                DELETE FROM schedule WHERE id = ?
            """, (schedule_id,))
            self.conn.commit()
            print("Schedule deleted successfully!")
        except Exception as e:
            print(f"Error deleting schedule: {e}")
