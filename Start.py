from calendar import isleap, month
from datetime import datetime
import pyodbc
import os
import re

# global variables
conn = pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=ZIL1134\MSSQLDEV2019A;'
                            'UID=SA;'
                            'PWD=perficient@123;'
                            'DATABASE=Project;'
                            'Trusted_Connection=no;')
# global variables end
def Fname_Input():
    Fname = input("First Name: ")
    i = 0
    while not(re.fullmatch('^[a-z A-Z]*$',Fname)):
        Fname = input("Invalid. Re-Enter First Name: ")
        if i == 2:
            print("Too many attempts")
            return False
        else:
            i = i + 1
    else:
        return Fname

def Lname_Input():
    Lname = input("Enter Last Name: ")
    i = 0
    while not(re.fullmatch('^[a-z A-Z]*$',Lname)):
        Lname = input("Invalid. Re-Enter Last Name: ")
        if i == 2:
            print("Too many attempts")
            return False
        else:
            i = i + 1
    else:
        return Lname

def Gender_Input():
    Gender = input("Enter your gender (M/F): ")
    i = 0
    while (Gender != 'M' and Gender != 'm') and (Gender != 'F' and Gender != 'f'):
        Gender = input("Invalid. Re-Enter your gender (M/F): ")
        if i == 2:
            print("Too many attempts")
            return False
        else:
            i = i + 1
    else:
        return Gender

def Date_Input():
    year = input("Enter Year (YYYY) : ")
    while (len(year) != 4) or not(year.isdecimal()):
        year = input("Invalid. Re-Enter Year(YYYY) : ")
    else:
        year = int(year)
    
    month_values = ['01','02','03','04','05','06','07','08','09','10','11','12']
    month_with_31_days = ['01','03','05','07','08','10','12']
    month = input("Enter Month(MM) : ")
    while not(month.isdecimal()) or not(month in month_values):
        month = input("Invalid. Re-Enter Month(MM) : ")


    if isleap(year) and month == '02':
        date = input("Enter Date(DD) : ")
        while True:
            if not(date.isdecimal()):
                pass
            else:
                date = int(date)
                if date >= 1 and date <=29:
                    break
            date = input("Invalid. Re-Enter Date(DD) : ")
    elif month == '02':
        date = input("Enter Date(DD) : ")
        while True:
            if not(date.isdecimal()):
                pass
            else:
                date = int(date)
                if date >= 1 and date <= 28:
                    break
            date = input("Invalid. Re-Enter Date(DD) : ")
    else:
        date = input("Enter Date(DD) : ")

        while True:
            if not(date.isdecimal()):
                pass
            elif month in month_with_31_days:
                date = int(date)
                if date >= 1 and date <= 31:
                    break
            else:
                date = int(date)
                if date >= 1 and date <= 30:
                    break
            date = input("Invalid. Re-Enter Date : ")

    return "{}-{}-{}".format(year,month,date)
        
def Date_of_Birth_Input():
    print("Enter Date of Birth")
    real_date = Date_Input()
    date = real_date[2: ]
    date = datetime.date(datetime.strptime(date, '%y-%m-%d'))

    if date < datetime.date(datetime.now()):
        return real_date
    else:
        print("Invalid. Date of birth Greater than Current Date")
        return False


def Phone_Input():
    phone_no = input("Enter Phone No. : ")
    i = 0
    while not(phone_no.isdecimal()) or len(phone_no) != 10:
        phone_no = input("Invalid. Re-Enter Phone No. : ")
        if i == 2:
            print("Too many attempts")
            return False
        else:
            i = i + 1
    else:
        return phone_no

def dist_id_input():
    dist_id = input("Distributer ID. : ")
    i = 0
    while not(dist_id.isdecimal()) or len(dist_id) != 4:
        dist_id = input("Invalid. Re-Enter Distributer ID. : ")
        if i == 2:
            print("Too many attempts")
            return False
        else:
            i = i + 1
    else:
        return dist_id

def Password_Input():
    password = input("Enter new password : ")
    i = 0
    while len(password) > 8 or len(password) < 5:
        password = input("Invalid(length must be 5 to 8). Enter New Password : ")
        if i == 2:
            print("Too many attempts")
            return False
        else:
            i = i + 1
    else:
        return password

def City_Input():
    cursor=conn.cursor()
    cursor.execute("EXEC city_info")
    response = cursor.fetchall()

    print("Available City are" )
    city_id_list = []
    for row in response:
        i = 0
        for col in row:
            if i == 0:
                city_id_list.append(str(col))
            print(col, end = ' ')
            i = i + 1
        print()
    
    city = input("Enter City ID : ")
    i = 0
    while not(city.isdecimal()) or not(city in city_id_list):
        city = input("Invalid. Re-Enter City ID : ")
        if i == 2:
            print("too many attempts")
            return False
        else:
            i = i + 1
    else:
        return int(city)


def Income_Input():
    Income = input("Enter Income (In Integer format) : ")
    i = 0
    while not(Income.isdecimal()):
        Income = input("Invalid. Re-Enter Income : ")
        if i == 2:
            print("Too many attempts")
            return False
        else:
            i = i + 1
    else:
        return Income

def Card_Type_Input(Income):
    
    if Income <= 90000:
        return "Yellow"
    else:
        return "White"

def Ration_No_Input():
    Ration_No = input("Enter Ration Number : ")
    i = 0
    while not(Ration_No.isdecimal()) or len(Ration_No) != 6:
        Ration_No = input("Invalid. Re-Enter Ration Number : ")
        if i == 2:
            print("Too many attempts")
            return False
        else:
            i = i + 1
    else:
        return Ration_No

def Area_Input(City):
    cursor=conn.cursor()
    cursor.execute("EXEC Area_info ?",City)
    response = cursor.fetchall()
    area_id_list = []

    print("Available Areas are" )
    for row in response:
        i = 0
        for col in row:
            if i == 0:
                area_id_list.append(str(col))
            print(col,end=' ')
            i = i + 1
        print()
    

    Area = input("Enter Area ID: ")
    i = 0
    while not(Area.isdecimal()) or not(Area in area_id_list):
        Area = input("Invalid. Re-Enter Area ID : ")
        if i == 2:
            print("too many attempts")
            return False
        else:
            i = i + 1
    else:
        return Area


def Add_Family_Member():
    os.system("cls")
    print("********** Add Family Member **********")

    Fname = Fname_Input()
    if Fname == False:
        return False
    
    Lname = Lname_Input()
    if Lname == False:
        return False
    
    Ration_No = Ration_No_Input()
    if Ration_No == False:
        return False

    Dob = Date_of_Birth_Input()
    if Dob == False:
        return False
    
    cursor = conn.cursor()
    cursor.execute("EXEC CHECK_RATION_AVAILABLE ?",Ration_No)
    response = cursor.fetchone()
    cursor.close()

    if response == None:
        print("Ration Card Not Found")
        return False
    elif response[0] == 1:
        cursor = conn.cursor()
        cursor.execute("EXEC IS_MEMBER_EXIST ?, ?, ?", Fname, Dob, Ration_No)
        response = cursor.fetchone()
        if response == None:
            pass
        elif response[0] == 1:
            print("Family Member already Exist")
            return False
        cursor.execute("EXEC ADD_MEMBER ?, ?, ?, ?", Fname, Lname, Dob, Ration_No)
        cursor.commit()
        cursor.close()
        return True

def admin_login():
    print("Enter Admin login Details")
    while True:
        Id = input("UserID : ")
        i = 0
        while not(Id.isdecimal()):
            Id = input("Re-Enter UserID : ")
            if i == 2:
                print("Too many attempts")
                return False
            else:
                i = i + 1

        Pass = input("Password : ")

        cursor = conn.cursor()
        cursor.execute("EXEC ADMINLOGIN ?,?",Id,Pass)
        response = cursor.fetchone()

        if response == None:
            return False
        elif response[0] == 1:
            return True

def Distributer_Registration():      
    os.system("cls")   
    print("********** Distributer Registration **********\n")
    print("NOTE: ALL FIELDS ARE MANDATORY")
    
    Fname = Fname_Input()
    if Fname == False:
        return
    
    Lname = Lname_Input()
    if Lname == False:
        return

    Gender = Gender_Input()
    if Gender == False:
        return
    
    City = City_Input()
    if City == False:
        return 

    Area = Area_Input(City)
    if Area == False:
        return

    Phone = Phone_Input()
    if Phone == False:
        return
    
    password = Password_Input()
    if password == False:
        return

    cursor = conn.cursor()
    cursor.execute("EXEC CHECK_DISTRIBUTER ?, ?",Fname,Phone)
    response = cursor.fetchone()
    if response == None:
        cursor.execute('EXEC Distributer_registration ?,?,?,?,?,?,?',Fname,Lname,Gender,City,Area,Phone,password)
        cursor.commit() 
        cursor.close()
        return True
    elif response[0] == 1:
        print("Distributer Already Exist")
        input()
        return False

def Distributer_Deletion():
    Fname = Fname_Input()
    if Fname == False:
        return False
    Phone = Phone_Input()
    if Phone == False:
        return False

    cursor = conn.cursor()
    cursor.execute("EXEC CHECK_DISTRIBUTER ?, ?",Fname,Phone)
    response = cursor.fetchone()
    cursor.close()

    if response == None:
        print("Distributer Not Found")
        return False
    elif response[0] == 1:
        print("Distributer Found")
        cursor = conn.cursor()
        
        cursor.execute("EXEC GET_DIST_ID ?, ?", Phone, Fname)
        response = cursor.fetchone()
        dist_id = response[0]

        cursor.execute("EXEC IS_DISTRIBUTER_REMOVABLE ?", dist_id)
        response = cursor.fetchone()

        if response == None:
            cursor.execute("EXEC Delete_Distributer ?, ?", Phone, Fname)
            cursor.commit()
            cursor.close()
            return True
        else:
            print("Distributer with Allocated Customer Cannot be Deleted")
            return False

def Customer_Registration():
    os.system("cls")
    print("********** Customer Registration **********\n")
    print("NOTE: ALL FIELDS ARE MANDATORY\n")
    City = City_Input()
    if City == False:
        return False
    
    Area = Area_Input(City)
    if Area == False:
        return False
    
    Phone = Phone_Input()
    if Phone == False:
        return False
    
    Income = Income_Input()
    if Income == False:
        return False
    
    Card_type = Card_Type_Input(float(Income))
    

    cursor = conn.cursor()
    cursor.execute("EXEC NEAR_BY_DISTRIBUTER ?,?", Area, City)
    response = cursor.fetchone()
    cursor.close()
    if response == None:
        print("No Distributer Found Nearby")
        return False
    else:
        Dist_id = response[0]
        cursor = conn.cursor()
        
        cursor.execute("EXEC IS_CUSTOMER_EXIST ?",Phone)
        response = cursor.fetchone()
        if response == None:
            cursor.execute('EXEC customer_registration ?,?,?,?,?,?',City, Area, Phone, Income, Card_type, Dist_id)
            cursor.commit()
            cursor.close()
            return True
        elif response[0] == 1:
            print("Customer Already Registered")
            return False

def Ration_No_Deletion():
    os.system("cls")

    print("********* Ration Number Deletion **********")
    Ration_No = Ration_No_Input()
    if Ration_No == False:
        return False
    
    cursor = conn.cursor()
    cursor.execute("EXEC CHECK_RATION_AVAILABLE ?", Ration_No)
    response = cursor.fetchone()

    if response == None:
        print("Ration Number Does not exist")
        return False
    elif response[0] == 1:
        confirm = input("Are you sure, You want to delete Ration Number? (Y/N): ")
        if confirm == 'Y' or confirm == 'y':
            cursor.execute("EXEC Delete_Customer_Record ?", Ration_No)
            cursor.commit()
            cursor.close()
            return True
        elif confirm == 'n' or 'N':
            return False
        else:
            print("Invalid Input")
            return False

def Customer_Login():
    os.system("cls")
    print("Enter details for Login")
    global Cust_Ration_No
    Cust_Ration_No = Ration_No_Input()
    if Cust_Ration_No == False:
        return False
    
    Fname = Fname_Input()
    if Fname == False:
        return False

    Dob = Date_of_Birth_Input()
    if Dob == False:
        return False
    
    cursor = conn.cursor()
    cursor.execute("EXEC IS_MEMBER_EXIST ?, ?, ?", Fname, Dob, Cust_Ration_No)
    response = cursor.fetchone()
    cursor.close()

    if response == None:
        print("Record not Found")
        return False
    elif response[0] == 1:
        return True


def Distributer_Login():
    print("Enter Details to Login")

    Phone = Phone_Input()
    if Phone == False:
        return False
    
    Password = Password_Input()
    if Password == False:
        return False
    
    cursor = conn.cursor()
    cursor.execute("EXEC DISTRIBUTER_LOGIN ?, ?", Phone, Password)
    response = cursor.fetchone()
    
    if response == None:
        print("Invalid Login Details")
        return False
    elif response[0] == 1:
        return True


def Distributer_window():
    os.system("********** Welcome to Distributer Panel **********")
    print("1. View Customer Details")
     
def Member_Deletion():
    os.system("cls")
    print("********* Family Member Deletion **********")
    Ration_No = Ration_No_Input()
    if Ration_No == False:
        return False

    Fname = Fname_Input()
    if Fname == False:
        return False

    # print("Enter Date of Birth ")
    Dob = Date_of_Birth_Input()
    if Dob == False:
        return False
    

    cursor = conn.cursor()
    cursor.execute("EXEC IS_MEMBER_EXIST ?, ?, ?", Fname, Dob, Ration_No)
    response = cursor.fetchone()
    if response == None:
        print("Family Member Does Not Exist")
        return False
    elif response[0] == 1:
        confirm = input("Are you sure, You want to delete the Member?(Y/N): ")
        if confirm == 'Y' or confirm == 'y':
            cursor.execute("EXEC Delete_Customer_Family_Member_Record ?, ?", Ration_No, Fname)
            cursor.commit()
            cursor.close()
            return True
        elif confirm == 'n' or confirm == 'Y':
            return False
        else:
            print("Invalid Input")
            return False

            
def admin_window():
        while True:
            os.system("cls")
            print("********** ADMIN PANEL **********")
            print('1. Register New Distributer ')
            print('2. Delete Existing Distributer')
            print('3. Register New Customer Ration Card')
            print('4. Add family Member for Ration Card')
            print('5. Delete Existing Customer Details')
            print('6. Logout')

            choice = input("Enter your Choice : ")
            i = 0
            while not(choice.isdecimal()) or (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6'):
                choice = input("Invalid. Re-Enter your Choice : ")
                if i == 2:
                    print("Too many attempts")
                    return
                else:
                    i = i + 1
            else:
                choice = int(choice)

            if choice == 1:
                regi_status = Distributer_Registration()
                if regi_status == True:
                    print("Distributer Registered Successfully")
                else:
                    print("Could not register the Distributer")
                input("Press Enter key to continue")

            elif choice == 2:
                if Distributer_Deletion():
                    print("Distributer Deleted Successfully")
                else:
                    print("Could not Delete the Distributer")
                input("Press Enter key to continue")
            
            elif choice == 3:
                if Customer_Registration():
                    print("Customer Registered Successfully")
                else:
                    print("Could not register the Customer")
                input("Press Enter key to continue")

            elif choice == 4:

                if Add_Family_Member():
                    print("Family Member Added Successfully")
                else:
                    print("Could not add Family Member")
                input("Press Enter key to continue")
            
            elif choice == 5:
                print("1. Delete A Ration Number\n2. Delete a Family Member")
                sub_choice = input("Enter Your Choice : ")

                while not(sub_choice.isdecimal()) or (sub_choice != '1' and sub_choice !='2'):
                    sub_choice = input("Invalid Re-Enter Your Choice : ")
                else:
                    sub_choice = int(sub_choice)

                if sub_choice == 1:
                    if Ration_No_Deletion():
                        print("Ration Number Deleted Successfully")
                    else:
                        print("Could Not delete the Ration Number")
                    input("Press Enter key to continue")
                
                elif sub_choice == 2:
                    if Member_Deletion():
                        print("Family Member deleted Successfully")
                    else:
                        print("Could not delete the Family Member")
                    input("Press Enter key to continue")

            else:
                print("Logout Sucessfully !")
                return         

def Customer_window():
    while True:
        global Cust_Ration_No
        os.system("cls")
        print("********** Welcome to Customer Panel **********")
        print("1. Current Month Distribution Details")
        print("2. Distribution History")
        # print("3. Check Gornment Scheme Eligibility")
        print("3. Logout")
        choice = input("Enter your choice : ")

        while not(choice.isdecimal()) or (choice != '1' and choice != '2' and choice != '3'):
            choice = input("Invalid. Re-Enter your choice : ") 
        
        if choice == '1': # option for Current month distribution
            os.system("cls")
            
            cursor = conn.cursor()
            cursor.execute("EXEC CURRENT_MOTNTH_DISTRIBUTION ?", Cust_Ration_No)
            response = cursor.fetchall()
            

            if response == None:
                print("No Details Found")
            else:
                print("RATION_NO\tITEM\t\tQUANTITY\tUNIT\t\tDATE")
                for i in response:
                    for j in i:
                        print(j, end='\t\t')
                    print()
            input("Press Enter to continue : ")
            cursor.close
        elif choice == '2': #option for distribution history
            os.system("cls")
            print("********** Distribution History **********")
            year = input("Enter Year : ")
            while not(year.isdecimal()) or (len(year) != 4):
                year = input("Invalid. Re-Enter Year: ")
            
            month_values = ['01','02','03','04','05','06','07','08','09','10','11','12']
            month = input("Enter Month : ")
            while not(month.isdecimal()) or not(month in month_values):
                month = input("Invalid. Re-Enter Month : ")

            cursor = conn.cursor()
            cursor.execute("EXEC DISTRIBUTION_HISTORY ?, ?, ?", Cust_Ration_No, month, year)
            response = cursor.fetchall()
            
            if response == None:
                print("No Details Found")
            else:
                print("RATION_NO\tITEM\t\tQUANTITY\tUNIT\t\tDATE")
                for i in response:
                    for j in i:
                        print(j, end='\t\t')
                    print()
            input("Press Enter to continue : ")
        else:
            return


def main():
    while True:
        os.system('cls')
        print("**************** RATION DISTRIBUTION SYSTEM ****************")
        print("1. Login As Customer")
        print("2. Login As Distributer")
        print("3. Login As Admin")
        print("4. Exit")

        choice = input("Enter your choice : ")

        while not(choice.isdecimal()) or (choice != '1' and choice != '2' and choice != '3' and choice != '4'): #Input validation
            choice = input("Invalid. Re-Enter your choice : ")
        else:
            choice = int(choice)

        if choice == 1: #option for Customer Login
            i =0
            while True:
                login_status = Customer_Login()

                if login_status:
                    Customer_window()
                    break
                else:
                    print("Invalid Login Details")
                    login_again = input("Press Y to Try Again? : ")

                    if login_again == 'Y' or login_again == 'y':
                        if i == 2:
                            input("Too many attempts")
                            break
                        i = i + 1
                        continue
                    else:
                        break

        elif choice == 2: #option for Distributer Login
            i =0
            while True:
                login_status = Distributer_Login()

                if login_status:
                    Distributer_window()
                    break
                else:
                    print("Invalid Login Details")
                    login_again = input("Press Y to Try Again? : ")

                    if login_again == 'Y' or login_again == 'y':
                        if i == 2:
                            input("Too many attempts")
                            break
                        i = i + 1
                        continue
                    else:
                        break
        
        elif choice == 3: # option for admin login
            i = 0
            while True:
                login_status = admin_login()

                if login_status:
                    admin_window()
                    break
                else:
                    print("Invalid Login Details")
                    login_again = input("Press Y to Try Again? : ")

                    if login_again == 'Y' or login_again == 'y':
                        if i == 2:
                            input("Too many attempts")
                            break
                        i = i + 1
                        continue
                    else:
                        break


        elif choice == 4: # option to exit
            
            exit_choice = input("Are you sure, you want to exit? (Y/N) : ")

            while True:
                if exit_choice == 'Y' or exit_choice == 'y':
                    exit()
                elif exit_choice == 'N' or exit_choice == 'n':
                    break
                else:
                    exit_choice = input("Invalid. Are you sure, you want to exit? (Y/N) : ")
import animation
main()
            