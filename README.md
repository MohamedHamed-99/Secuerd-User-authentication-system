# Secuerd-User-authentication-system
User authentication and access control system prototype
The System devlopes a full secure user authentication protoype. 
A prototype of MediaView users where added usung Role Back Access control model which maps each user to a role and each role to specific objects (access_control.py)
Then a secure passwd.txt file is created which includes an information about the users. Each line contains (usernmae:hash_salt:hash_value:fullname,role) for each user (user_addition.py)
hash function used to encrypt password given by the user and a random salt_value created for each one so it can be securly stored in our file
Enrollment mechanism is created with procative password checking to make sure the users doesn't enter a week passswrod. (enrollment.py)
Sig_in mechanism created to for useres which checks if the user is on our system or not and then checks for the given password if hashing it with the hash_salt retrives matches the hash_value or not (sigin.py)
Prototype that testes the whole system is created as well (Prototype.p)
