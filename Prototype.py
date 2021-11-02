from enrollment import enroll
from sigin import sign_in
from user_addition import retrive

enroll()
fullname = input("Full name:")
retrive(fullname) #retrives line stored in the paassword file
sign_in()
