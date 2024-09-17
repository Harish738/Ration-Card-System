
from fnmatch import fnmatchcase
from inspect import Parameter
from pickletools import long1
from typing_extensions import Required
import pyodbc as odbc
import re
# Trusted Connection to Named Instance
connection = odbc.connect('DRIVER={SQL Server};'
                            'SERVER=ZIL1143\MSSQLDEV2019;'
                            'UID=SA;'
                            'PWD=perficient@123;'
                            'DATABASE=Project;'
                            'Trusted_Connection=no;')


class admin():
    
    def __init__(Required):
        print(" ")
    
    def CUSTOMER_REGISTRATION(Required):
        print("------------------ Customer Registration Details------------")
        print("            ")
        print("NOTE: ALL FIELDS ARE MANDATORY")
        print("            ")
        
        pyspark = 1+*:
       

        '''Area verification starts '''    
        print("Area ID's are : " )
        cs=connection.cursor()
        cs.execute("EXEC Area_info")
        rows = cs.fetchall()
        for row in rows:
            for col in row: 
                print(col,end=' ')
            print()
            
        while True:
           

            Required.area = input("Area ID: ")
            if re.match('^[0-9]*$', Required.area):
              
                break

            Required.area = input("Re enter area ID: ")
            if re.match('^[0-9]*$', Required.area):
                break
            else:
                print(" *** TOO MANY ATTEMPTS *** ")
                exit()
        pass
        '''Area verifiation ends'''

        '''City verification starts'''
        while True:
            print("City ID's are" )
            Cmd=connection.cursor()
            Cmd.execute("EXEC city_info")
            rows = Cmd.fetchall()
            for row in rows:
                for col in row:
                    print(col,end=' ')
            print()
            

            Required.city = input("City ID : ")
            if re.match('^[0-9]*$', Required.city):
                break

            Required.city = input("Re enter City ID: ")
            if re.match('^[0-9]*$', Required.city):
                break
            else:
                print(" *** TOO MANY ATTEMPTS *** ")
                exit()

        '''city verification ends'''
        
        
        '''Phone no starts'''
        regex = "\d{10}"
        while True:
            Required.phone_no = input("Phone no: ")
            # converted_num = int(self.phone_no)
            if re.fullmatch("\d{10}", Required.phone_no):
                
                break
            
            Required.phone_no = input("Re-enter your phone-no: ")
            # converted_num = int(self.phone_no)
            if re.fullmatch("\d{10}", Required.phone_no):
                
                break
            
            else:
                pass
                print(" ")
                print("*** Too many attempts *** ")
                exit()

        '''Phone no end'''

        '''family income details'''

        while True:
            Required.income = input('Enter your income: ')

            break
            
        Cardtype = ("^(?:white|WHITE|White|yellow|Yellow|YELLOW)$")
        while True:
            Required.Card_type = input('Enter card type (white or yellow)')
            if re.fullmatch(Cardtype,Required.Card_type):
                break
            print('Wrong Credentails')
            Required.Card_type = input("Re-Enter Card Type")
            if re.fullmatch(Cardtype,Required.Card_type):
                break

        cursor = connection.cursor()
        cursor.execute('EXEC customer_registration ?,?,?,?,?',Required.area,Required.city,Required.phone_no,Required.income,Required.Card_type)
        cursor.commit() 
       


    # def view_user(self):
        
    #     print("            ")
    #     print("------------------Display user ------------")
    #     print("            ")    
    #     print("Name of user is: ", self.Fname)
    #     print("Name of user is: ", self.Lname)
    #     # print("Date of birth of user is: ", self.dob)
    #     print("Gender of user is: ", self.gender)
    #     print("Area of user is: ", self.area)
    #     print("Phone number of user is : ",self.phone_no)
    #     print("Ration card no of user is: ", self.ration_card)

obj_admin = admin()

obj_admin.add_customer()

# obj_admin.view_user()




