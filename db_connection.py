
import pypyodbc

# Return the sql connection 
def getConnection():
     connection=pypyodbc.connect("DRIVER={SQL Server};Server=;DATABASE=dane;Trusted_Connection=Yes")
     return connection 



