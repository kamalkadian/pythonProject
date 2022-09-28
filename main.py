def registration():
    print("#########   You are in registration    #########")
    print("*******    Please enter the email    ******** ")
    email = input()
    lis = list(email)
    if ("@" in email) and (email.count("@") >= 1):
        if ("." in email) and (email.count(".") >= 1):
            if (lis.index("@")<lis.index(".")):
                if (email[0].isalpha()):
                    if "@""." not in email:
                        print("Email Id has been created")

    mail = email
    ######Passsword
    import re
    print("********    please enter the password    ********")
    a = input()
    if (5 < len(a) < 16):
        if (re.search("\d", a)):
            if re.search(r'[~#$%^&*()@_+"]', a):
                if re.search("[A-Z]", a):
                    if re.search("[a-z]", a):
                        print("Password has been set")

    store = {}
    key = mail
    value = a
    file = open("Login.txt", "a")
    file.write(key)
    file.write(",")
    file.write(a)
    file.write("\n")
    file.close()
    store.update({key: a})

def login():
    print("######    You are in login    #######")
    print("********    please enter the register email and password    ********")
    Id_please = input()
    passuward = input()

    file=open("Login.txt","r")
    flag=0
    for line in file:
        if (line==""):
            break
        userpass=line.split(",")
        username=userpass[0]
        password=userpass[1]
        if (username in Id_please) and (passuward in password):
            print("$$$$$$$$$  Welcome  $$$$$$$$$")
            flag=1
            break
        if (username in Id_please) and (passuward not in password):
            print("********Wrong Password******")
            print("Your password is ", userpass[1])
            flag=1
            break

    if flag==0:

        print("******    please register    *******")
        registration()

print("******   press 1 for log in  OR   press 2 for registration   *******")
l=int(input())
if l==1:
    login()
elif l==2:
    registration()
else:
    print("wrong input")
