import re
from user_addition import add
from access_control import roleOdict

special_characters = "!,@,#,$,%,?"
common_pass = ["Password1","Qwerty123","Qaz123wsx"]



def role_check():
    bool = True
    while bool:
        global role 
        role = input("Role: ") #test case user input role
        for key in roleOdict:
            if key == role:
                bool = False
        if bool:
            print("Invalid Role")
                    
def check_common(s,list_pass):
    for key in list_pass:
        if key == s:
            return True
    return False
def pass_check(username):
    while True:
        global password
        password = input("Enter password: ") #test case user input password
        if not (8 <= (len(password)) ):
            print("Make sure password is at least 8-12 characters")
        elif re.search('[0-9]', password) is None:
            print("Make sure password has a number")
        elif re.search('[A-Z]', password) is None:
            print("Make sure password has a capital letter")
        elif re.search('[a-z]', password) is None:
            print("Make sure password has a lower case letter")
        elif username == password:
            print("Make sure password is not your username")
        elif check_common(password,common_pass):
            print("Password is week,Choose a strong one")
        elif not any(c in special_characters for c in password): #       searching for any special char. in pecial_characters string:
            print("Make sure password has a special letter {!,@,#,$,%,?}")

        else:
            break
def enroll():
    print("MediaView Imaging")
    print("Medical Information Managment System")
    print("---------------------------")
    fullname = input("Enter fullname: ") #test case user input name #test case user input role
    username = input("Enter username: ") #test case user input username
    role_check()
    pass_check(username)
    add(fullname,role,username,password)
    print("Account created Sucessfully !!")
