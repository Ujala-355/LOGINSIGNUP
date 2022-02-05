import json
option=input("enter a 1 login| 2 signup!!")  
if option=="1":
    d={}
    username=input("create username!!")
    password=input("create pasword!!")
    lower,upper,digit,special=0,0,0,0
    if len(password)>=6:
        for i in password:
            if (i.isupper()):
                upper=1
            if (i.islower()):
                lower=1
            if (i.isdigit()):
                digit=1
            if i=="@" or i=="#" or i=="&" or i=="$" or i=="%" or i=="!" or i=="*":
                special=1
            total=lower+upper+digit+special
        if total!=4:
            print("Password should contain atleast one upper, lower,digit,special character:")
        else:
            password1=input("confirm password!!")
            if password==password1:
                hobbies=input("enter hobbies:")
                des=input("enter description:")
                d["Name"]=username
                d["Password"]=password
                d["hobbies"]=hobbies
                d["Description"]=des
                with open("mtext8.json","w") as f:
                    json.dump(d,f,indent=4)
                    print("You are login Successfully!")
            elif password!=password1:
                print("password dosn't match ,restart!!")
    else:
        print("the password should be contain 6 ch!!")
elif option=="2":
    d={}
    username=input("create username!!")
    password=input("create pasword!!")
    lower,upper,digit,special=0,0,0,0
    if len(password)>=6:
        for i in password:
            if i.isupper():
                upper=1
            if i.islower():
                lower=1
            if i>="0" and i<="9":
                digit=1
            if i=="@" or i=="#" or i=="&" or i=="$" or i=="%" or i=="!" or i=="*":
                special=1
            total=lower+upper+digit+special
        if total!=4:
            print("Password should contain atleast one upper, lower,digit,special character")
        else:
            with open("mtext8.json","r") as f:
                file=f.read()
                if username in file:
                    print("You are already login here!!")                   
                else:
                    password1=input("confirm password!!")
                    if password==password1:
                        hobbies=input("enter hobbies:")
                        des=input("enter description:")
                        d["Name"]=username
                        d["Password"]=password
                        d["hobbies"]=hobbies
                        d["Description"]=des
                        with open("mtext8.json","w") as f:
                            json.dump(d,f,indent=4)
                            print("You are signup Successfully!!")
                    elif password!=password1:
                        print("password dosn't match ,restart!!")
    else:
        print("the password should be contain 6 character!!")
            