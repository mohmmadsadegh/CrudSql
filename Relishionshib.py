import pyodbc
connectshion = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "server=.;"
                          "Database=student;"
                          "Trusted_Connection=yes;")
curser = connectshion.cursor()


class Repository():
    def __init__(self) -> None:
        pass
    
    
    def crate(self, Table_Name, Col_name, val):
        try:
            curser.execute("insert into  "+Table_Name+" ("+Col_name+") values ('"+val+"')")
            curser.commit()
        except:
            return False