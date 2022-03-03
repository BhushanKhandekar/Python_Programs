password = input()       #   ank@123

upper_case = 0
lower_case = 0
digits = 0
spl = 0

if len(password) >= 10 and len(password) <= 5:
    print("not a valid password")
else:
    for i in password:      #ank@123
        if ord(i) >= 65 and ord(i) <= 90:
            upper_case+=1
        elif ord(i) >= 97 and ord(i) <= 122:
            lower_case+=1
        elif ord(i) >= 49 and ord(i) <= 57:
            digits+=1
        else:
            spl+=1

    if upper_case != 0 and lower_case != 0 and digits != 0 and spl != 0:
        print("valid password")
    else:
        print("invalid password") 
