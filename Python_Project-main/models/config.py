import pyodbc
def connection():
    con_str = """
    DRIVER={SQL Server};
    SERVER=DESKTOP-OGOQI3D\אילת;
    DATABASE=Final_Python_Project;
    Trusted_Connection=yes;
    """
    # יצירת חיבור באמצעות pyodbc.connect()
    conn = pyodbc.connect(con_str)
    return conn
