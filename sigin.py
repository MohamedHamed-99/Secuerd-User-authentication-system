from access_control import roleOdict

import hashlib

def username_line(username): #To return the line that has the credentials for our user
    works = False;
    read_txt = open("passwd.txt", "r") #open the file

    with read_txt as file:
            for line in file:
                if username in line: #for each line check if the username in or not
                    break
            read_txt.close()  #close the file
            return line #return the line of the username in the database
def username_check(username): #To check if the uder is in the system or not
    read_txt = open("passwd.txt", "r")

    with read_txt as file:
            for line in file:
                if username in line: #check if sequence of input username matches the input of the user
                    w=0
                    x=""            # if yes, we store the username in the passwd file for checking
                    while line[w] != ":":
                        x += line[w]
                        w+=1
                    if x == username: # if we find a macth then the user in the system
                        return True
                    else:
                        return False # we didn't that the sequence matches but still that's not the full username, so the system returns invalid
    read_txt.close()
    return False #Also if there was no match we have an invalid username
def print_access(fullname,role):
    for key in roleOdict: #dic for roles and objects is accessed
        if key == role: #if the user role matches one of the keys in the dict 
            y = roleOdict.get(key) #need to get the objects, storedin unhashable object
            print(fullname+ ":\nrole:"+role+"\nAccess Granted to:"+str(y)+"\n") #print the object in str() since unhashable objects need to be converted first to be able to print it
            break
                    
def password_check(salt_value,salt_hash):  #procative password check
    sas = False #check if the pass check passed or failled
    count = 0    #count for max attempts
    while True:  #looping until correct or max attempts reached
        password = input("Enter password: ")
        passwd = password.encode('utf-8')  #encoding pass for hashing with the sv aquired earlier
        key = hashlib.pbkdf2_hmac('sha256', passwd, salt_value, 100000) #hashlib function PBKDF2_HMAC
        if salt_hash == key: #if we found a match with the salt hash aquired before then the password is correct
            sas = True #password check passed
            break #break the loop no need to iterate anymore
        count+=1 # increment pass attempts
        if count == 3: # 3 is the max attempts user can reach before going out
            print("Maximum attempts reached!")
            break #break when maz attempts reached
        else:
            print("invalid password") #else print invalid pass
    return sas #return if the pass_check passed or failed
def retrive_data(line): #retreing all the data needed from the line we have in our database
    for i in range(len(line)):  #retreiving the salt_hash stored
        if line[i] == ":": #iterate unril firts ":" is found for sh
            z = 1
            sh = ""   #salt_hash   
            j=0
            while line[i+j+1] != ":":  #while the second ":" is no here we are still in the sh
                sh += line[i+z]
                z+=1
                j+=1
            break    # when second ":" is found sh is done
    w = i+z+1
    sv = ""       #salt_value    
    while line[w] != ":": #retreiving the salt_value stored until third ":" is reached
        sv += line[w]
        w+=1
    w+=1
    fullname = "" #full name after third ":"
    while line[w] != ",": #retreiving the fullname stored
        fullname += line[w]
        w+=1
    w+=1
    role = "" #role which is after the ","
    while line[w] != "\n": #retreiving the role stored until the new line we wrote when creating password is reached
        role += line[w]
        w+=1
    return sv,sh,fullname,role #retriving all the data we got



def sign_in(): #Sig in function for users
    print("MediaView Imaging")
    print("Medical Information Managment System")
    print("---------------------------")
    bool = True
    while bool:
        username = input("Enter username: ") #test case user input username 
        if username_check(username): # check if user is in out database (passwd.txt)
            bool = False
        else:
            print("Username is not valid")
    line = username_line(username) #outputline 
    sv, sh, fullname, role = retrive_data(line)
    salt_value = bytes.fromhex(sv) #converting salt_value back to bytes 
    salt_hash = bytes.fromhex(sh) #converting salt_hash back to bytes 

    if password_check(salt_value,salt_hash): # procative password checking
        print_access(fullname,role) #printing the objects for the user


# enroll()
# enroll()
# enroll()
# sign_in()
# sign_in()
# sign_in()
# sign_in()
# sign_in()
# sign_in()