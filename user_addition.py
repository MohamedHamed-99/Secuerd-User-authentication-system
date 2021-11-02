import hashlib
import os

def add(fullname,role,username,password):
    f= open("passwd.txt","a+") #Open the password.txt file and give write and read permisson
    salt = os.urandom(32)  #random salt for this user
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000) #hashlib function PBKDF2_HMAC
    f.write(username) #storing username
    f.write(":")
    f.write(key.hex()) #stored hashedsalt
    f.write(":")
    f.write(salt.hex()) #stored salt
    f.write(":")
    f.write(fullname) #stored name
    f.write(",")
    f.write(role) #stored role
    f.write("\n")
    f.close()

def retrive(fullname):
    works = False; #check if name was found or not
    read_txt = open("passwd.txt", "r")
    with read_txt as file:
            for line in file:
                if fullname in line: #check if input fullname is valid iterating through each line in the passwd.txt and 
                    print("retriving data for "+fullname+"....\n")
                    print(line)
                    works = True
            if works == False:
                print("Invalid Name\n")
   
#add("Mohamed","Patient","mhmed","samy")

