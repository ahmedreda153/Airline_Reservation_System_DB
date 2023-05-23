import pyodbc

#connect database
server = 'DESKTOP-Q66QLBQ\SQLEXPRESS' # write your server name
database = 'AIRLINE_RESERVATION' # write name of the database in your server
username = 'DESKTOP-Q66QLBQ\ahmed reda' # write your username in your server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';Trusted_Connection=yes;')
cursor = conn.cursor()