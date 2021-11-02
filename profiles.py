# login screen (using files/sql criteria)

import csv

def ExistingUser(username, password):
    FileRead = open("profiles.csv","r")
    info = csv.reader(FileRead)
    login = False
    while login == False:
        for i in info:
            if i[0] == username:
                if i[1] == password:
                    login = True
                else:
                    print("Wrong password, try again!")
                    login = True # to be removed after merge
            else:
                print("Username not found! Create account.")
                login = True # to be removed after merge
    print(login)
    FileRead.close()
            
def CreateUser(username, password):
    FileAppend = open("profiles.csv","a", newline = "")
    info = [username, password]
    Append = csv.writer(FileAppend)
    Append.writerow(info)
    FileAppend.close()

CreateUser('sohan','varier')
ExistingUser('sohan','varie')
