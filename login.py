import pyodbc as odbc

connection = odbc.connect('DRIVER={SQL Server};'
                            'SERVER=ZIL1143\MSSQLDEV2019;'
                            'UID=SA;'
                            'PWD=perficient@123;'
                            'DATABASE=Project;'
                            'Trusted_Connection=no;')

class admin():
    print(" ")
    def login(self):


        self.id = input('Enter your Id : ')
        self.password = input('Enter your password :')        
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Admin_id_pass ')
        account = cursor.fetchall()
        cursor.commit()
      
obj_admin = admin()
obj_admin.login()