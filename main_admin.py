from cmd import Cmd
import cmd
from fnmatch import fnmatchcase
from inspect import Parameter
from pickletools import long1
from secrets import choice
from typing_extensions import Self
from colorama import Cursor
import pyodbc as odbc
import re



# Trusted Connection to Named Instance
connection = odbc.connect('DRIVER={SQL Server};'
                            'SERVER=ZIL1143\MSSQLDEV2019;'
                            'UID=SA;'
                            'PWD=perficient@123;'
                            'DATABASE=Project;'
                            'Trusted_Connection=no;')

class distributer():
    
    def __init__(self):
        print(" ")
    '''*******************Distributer registration*****************'''
    def DISTRIBUTER_REGISTRATION(self):
            
        print("------------------ Distributer Registration Details------------")
        print("            ")
        print("NOTE: ALL FIELDS ARE MANDATORY")
        
        while True :
            self.Fname = input("First Name: ")
            if re.fullmatch('^[a-z A-Z]*$',self.Fname):
                break    
            self.Fname = input
            self.Fname = input("Re enter your First name: ")
            if re.fullmatch('^[a-z A-Z]*$',self.Fname):
                break
            else:
                print("*** TOO MANY ATTEMPTS ***")
                exit()    
            
        while True :
            self.Lname = input("Last Name: ")
            if re.fullmatch('^[a-z A-Z]*$',self.Lname):
                break    
            
            self.Lname = input("Re enter your Last name: ")
            if re.fullmatch('^[a-z A-Z]*$',self.Lname):
                break
            else:
                print("*** TOO MANY ATTEMPTS ***")
                exit() 

        ''' DOB verification starts '''
       
        # Only this type of format is allowed - "dd/mm/yyyy"

        
        # regex = ("^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\|-|/)([1-9]|0[1-9]|1[0-2])(\|-|/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$|^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\|-|/)([1-9]|0[1-9]|1[0-2])(\|-|/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$")


        # while True :
        #     self.dob = input("Date of Birth: ")
        #     if re.fullmatch(regex,self.dob):
        #         break

        #     self.dob = input("Re-enter your Date of Birth:")
        #     if re.fullmatch(regex,self.dob):
        #         break
        #     else:
        #         print("*** TOO MANY ATTEMPTS ***")
        #         exit()    

        ''' DOB verification end'''


        ''' Gender validation for male starts '''
        gender_identification = ("^(?:male|Male|MALE|female|Female|FEMALE)$")
        print('ENTER MALE OR FEMALE ( M or F) NOT ALLOWED')
        while True:
            self.gender = input("Enter your gender: ")
            if re.fullmatch(gender_identification,self.gender):
                break
            
            self.gender = input("Re-enter your gender: ")
            if re.fullmatch(gender_identification,self.gender):
                break

            else:
                print(" *** TOO MANY ATTEMTS *** ")        
                exit()
        ''' Gender validation ends '''


        '''Area verification starts '''    
        while True:
            print("Area ID's are" )
            cs=connection.cursor()
            cs.execute("EXEC Area_info")
            rows = cs.fetchall()
            for row in rows:
                for col in row:
                    print(col,end=' ')
            print()
            

            self.area = input("Area ID: ")
            if re.match('^[0-9]*$', self.area):
                break

            self.area = input("Re enter area ID: ")
            if re.match('^[0-9]*$', self.area):
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
            

            self.city = input("City ID : ")
            if re.match('^[0-9]*$', self.city):
                break

            self.city = input("Re enter City ID: ")
            if re.match('^[0-9]*$', self.city):
                break
            else:
                print(" *** TOO MANY ATTEMPTS *** ")
                exit()
        pass
        '''City verification ends'''

        '''Phone no starts'''
        regex = "\d{10}"
        while True:
            self.phone_no = input("Phone no: ")
            # converted_num = int(self.phone_no)
            if re.fullmatch("\d{10}", self.phone_no):
                
                break
            
            self.phone_no = input("Re-enter your phone-no: ")
            # converted_num = int(self.phone_no)
            if re.fullmatch("\d{10}", self.phone_no):
                
                break
            
            else:
                pass
                print(" ")
                print("*** Too many attempts *** ")
                exit()

        '''Phone no end'''
        cursor = connection.cursor()
        cursor.execute('EXEC Distributer_registration_detail ?,?,?,?,?,?',self.Fname,self.Lname,self.gender,self.area,self.city,self.phone_no)
        cursor.commit() 
        cursor.close()
'''--------------------------CUSTOMER REGISTRATION----------------------'''
class customer():    
    def __init__(Required):
        print(" ")
    
    def CUSTOMER_REGISTRATION(Required):       


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
                
                cursor = connection.cursor()
                cursor.execute('SELECT Distributer_ID FROM Distributer_details WHERE AREA_ID = ?',Required.area)
                cursor.commit()
                
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
            if re.fullmatch("\d{10}", Required.phone_no):
                
                break
            
            Required.phone_no = input("Re-enter your phone-no: ")
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
            Required.income = input('Enter income: ')

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
       

'''*************************ADMIN MENU****************'''
def adminwork():
        while True:
            print('MENU :')
            print('1. Create New Distributer ')
            print('2. Delete Existing Distributer')
            print('3. Create New Customer Ration Card')
            print('4. Add family Details')
            print('5. Delete Existing Customer Details')
            print('6. Logout')

            choice = int(input("Enter the Choice : "))
            if choice == 1:
                print("----------- Distributer Registration Details---------")
                obj_distributer.DISTRIBUTER_REGISTRATION()  #calling function 
            
            elif choice == 2:
                print('Enter the distributer Id :')
                delete = int(input(""))
            
            elif choice == 3:
                print("-----------Customer Registration Details---------")
                obj_customer.CUSTOMER_REGISTRATION()
            
            elif choice == 4:
                print("Enter the Ration no. to add family details")
                addDetails = int(input(" "))
            
            elif choice == 5:
                print('Enter the Customer Ration no. :')
                delete1 = int(input(""))

            else:
                print("Logout Sucessfully !")
                exit()            


obj_distributer = distributer()
obj_customer= customer()
#######################################################################################
print("**************** RATION CARD DISTRIBUTION SYSTEM ****************")
print('1. Login As Customer')
print('2. Login AS Distributer')
print('3. Login As Admin')

choice1 = int(input("Enter your choice : "))

if choice1 == 1:
    print('Enter the following credentials')
    print("enter ration card no.")
    number = int(input(""))
    print('enter phone number')
    number1 = int(input(""))

elif choice1 == 2:
    print('Enter the Details')
    print('Enter userID')
    number2 = int(input(" "))
    print('Enter password')
    number3 = int(input(" "))

elif choice1 ==3:
    print("Enter details")
    ID = int(input("userID : "))
    password = input("Password : ")
    print("----------WELCOME ADMIN--------")
    adminwork() #calling function 
    