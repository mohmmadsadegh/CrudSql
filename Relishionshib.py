import pyodbc

class Repository:
    def __init__(self):
        self.connection = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "server=.;"
            "Database=student2;"
            "Trusted_Connection=yes;"
        )
        self.cursor = self.connection.cursor()

    def create(self, table_name, col_names, values):
        try:
            query = f"INSERT INTO {table_name} ({col_names}) VALUES ({values})"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error in create: {e}")
            return False

    def read(self, table_name, col_names="*"):
        try:
            query = f"SELECT {col_names} FROM {table_name}"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error in read: {e}")
            return []

    def update(self, table_name, set_clause, where_clause):
        try:
            query = f"""UPDATE {table_name} SET {set_clause}
            WHERE {where_clause}"""
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error in update: {e}")
            return False

    def delete(self, table_name, where_clause):
        try:
            query = f"DELETE FROM {table_name} WHERE {where_clause}"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error in delete: {e}")
            return False
