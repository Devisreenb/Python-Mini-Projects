from cryptography.fernet import Fernet 

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()
# run write_key() function only once 
'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def add():
    with open("password.txt","a") as f :
        user = input("Account name : ")
        pwd = input("Password : ")
        f.write(user+"|"+fer.encrypt(pwd.encode()).decode()+"\n")

def view():
    with open("password.txt","r") as f:
        for val in f.readlines() :
            user,pwd = val.rstrip().split("|")
            print("user :",user,"|","password :",fer.decrypt(pwd.encode()).decode())

while True:
    answer = input("Would you like to add or view the passwords (view, add) press q to exit ?").lower()
    if answer == "q":
        break
    elif answer == "add":
        add()
    elif answer == "view":
        view()
    else:
        print("Invalid option.")