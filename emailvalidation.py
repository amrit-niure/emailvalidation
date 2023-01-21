email = input("Enter your Email : ") #g@g.in
k = 0
j = 0
d = 0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] =="."):
                for em in email:
                    if em ==em.isspace():
                        k = 1
                    elif em.isalpha():
                        if em==em.upper():
                            j = 1
                    elif em.isdigit():
                        continue
                    elif em =="_" or em == "." or em =="@":
                        continue
                    else:
                        d = 1
                if k == 1 or j ==1 or d==1:
                    print("Wrong Email [5]")
            else:
                print("Wrong Email [4]")
        else:
            print("Wrong Email [3]")
    else:
            print("Wrong Email [2]")
else:
    print("Wrong Email [1]")
