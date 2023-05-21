import pyodbc

#connect database
server = 'DESKTOP-Q66QLBQ\SQLEXPRESS'
database = 'AIRLINE_RESERVATION'
username = 'DESKTOP-Q66QLBQ\ahmed reda'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';Trusted_Connection=yes;')
cursor = conn.cursor()