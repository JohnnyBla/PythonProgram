# generate random token and Username
import random as rd
import string


def tokenGenerator():
    #read user input
    user = (input("What is your first name ")).strip().replace(" ", "")
    last = (input("What is your last name ")).strip().replace(" ", "")
    #random token letters and numbers
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    last2 = string.digits
    #iterate through numbers and letters return random 9 digit list
    newPass = rd.choices(chars, k=9)
    #generate new username
    nU = user[0].title()
    nU2 = last[:-1]
    newUser = (nU + nU2 + rd.choice(last2))
    #iterate through newPass to return as a string
    for i in newPass[0]:
    #generate final token to be written in plain language
            i = i.join(rd.choices(chars, k=8))
    #Check for intergers
    if user.isnumeric():
            print("Invalid Entry")
            return False
    elif last.isnumeric():
            print("Invalid Entry")
            return False
    else:
    #print results
        print(f"{user.title()} your new log in token is {i}")
        print(f"your new username is {newUser.title()}")    
tokenGenerator()