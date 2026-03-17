pwd=input("enter password:")
crt_pwd="qewrtyq12"
otp=7896
if pwd==crt_pwd:
    ur_otp=input("enter otp")
    if otp==ur_otp:
        print("login successful")
    else:
        print("wrong otp")
else:
    print("wrong pwd")
