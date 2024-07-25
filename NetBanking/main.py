# importing packages
import sqlite3
import random

#connecting db file
conn = sqlite3.connect('mydb.db')


#fetching data from db
# data = conn.execute('''select * from SBI_IFSC where ifsc_code ="SBIN0021870" ''')
# print(list(data))

amount =5000
conn.execute(f'''update AccountDetails set bank_balance = "{amount}" where username = "santhosh@gmail.com"''')
# # print(data)
conn.commit()
# print(list((zip("Hi","Hello"))))

#show profile
def showprofile(userdetails):
    print("Profile Details 👇👇\n---------------------------")
    print(f"Name : {userdetails[-1]}\n\nUsername : {userdetails[1]}\n\nAccount number : {userdetails[7]}\n\nBank Name : {userdetails[4]}\n\nBranch Name : {userdetails[3]}\n\nIFSC CODE : {userdetails[5]}")
    while True:
        option = int(input("Enter 1 to show features \nEnter option : "))
        if option ==1:
            showfeatures(userdetails)
            break
        else:
            print("Invalid Option...")
#features
def showfeatures(userdetails):
    print("1. Add amount \n2. Net Banking \n3. Check Balance \n4. Show Profile \n5. Logout")
    option = int(input("Enter your option : "))
    match option:
        case 1:
            print("Add amount")
        case 2:
            print("Net Banking")
        case 3:
            print("Check Balance")
        case 4:
            # print("Show profile")
            showprofile(userdetails)
        case 5:
            return 0 
        case _:
            print("Invalid Option")
            showfeatures()

#check user password

def checkuserpassword(username):
    print("---------------------------------")
    print("Enter password Validation ... ")
    print(f"Username : {username}")
    user_db_pass = list(conn.execute(f'''select password from AccountDetails where  username = "{username}"'''))[0][0]
    # print(user_db_pass)
    password = input("Enter Password : ")
    if password == user_db_pass:
        print("Password Validation Successfull ✅✅✅")
        userdetails = list(conn.execute(f'''select * from AccountDetails where username = "{username}"'''))
        userdetails = [i for i in userdetails[0]]
        # print(userdetails)
        showfeatures(userdetails)
    else:
        print("Password is not matching ❌❌❌")
        checkuserpassword(username)
        
        
        
#check login username
def checkloginusername():
    print("-------------------------------")
    print("Enter Login ...... ")
    user_name = input("Enter username here : ").lower()
    if user_name.endswith("@gmail.com"):
        allusernames = list(conn.execute('''select username from AccountDetails'''))
        # print(allusernames)
        allusernames = [i[0] for i in allusernames]
        if user_name in allusernames:
            print("Valid Username ✅✅✅")
            checkuserpassword(user_name)
        else:
            print("Username is not registered ❌❌❌")
            checkloginusername()
    else:
        print("Incorrect Username ❌❌❌")
        checkloginusername()
    # print(allusernames)
    # for i in allusernames:
    #     print(i[0],end=" ")

#start logic here
def start():
    option = int(input("1. Login\n2. Register\n3. Logout\nEnter Your option : "))
    match option:
        case 1:
            # print("Login Here")
            checkloginusername()
        case 2:
            print("Register")
        case 3:
            return 0
        case _:
            print("Invalid Option ❌❌❌")
            start()
start()


