
from cmd import Cmd
import cmd
from fnmatch import fnmatchcase
from inspect import Parameter
from pickletools import long1
from typing_extensions import Self
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
    
    def __init__(self):
        print(" ")
    
    def add_user(self):
            
        # print("            ")
        # print("**************** RATION CARD DISTRIBUTION SYSTEM ****************")
        # print("            ")
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



        '''Ration card starts'''

        # while True:

        #     self.ration_card = 123456
        #     rc = int(input("Ration card no: "))

        #     if self.ration_card == rc:
        #         print(" ")
        #         print("         *** VERIFIED ***")
        #         break
            
        #     rc = int(input("Re - enter your ration card no: "))
        #     if self.ration_card == rc:
        #         break
        #     else:
        #         print(" ")
        #         print("*** TOO MANY ATTEMPTS ***")
        #         exit()
        '''Ration card end'''

        cursor = connection.cursor()
        cursor.execute('EXEC Distributer_registration_detail ?,?,?,?,?,?',self.Fname,self.Lname,self.gender,self.area,self.city,self.phone_no)
        cursor.commit() 
        cursor.close()


    # def view_user(self):
        
    #     print("            ")
    #     print("------------------Display user ------------")
    #     print("            ")    
    #     print("Name of user is: ", self.Fname)
    #     print("Name of user is: ", self.Lname)
    #     # print("Date of birth of user is: ", self.dob)
    #     print("Gender of user is: ", self.gender)
    #     print("Area of user is: ", self.area)
    #     print("City of user is: ", self.city)
    #     print("Phone number of user is : ",self.phone_no)
        # print("Ration card no of user is: ", self.ration_card)

obj_admin = admin()

obj_admin.add_user()

# obj_admin.view_user()





