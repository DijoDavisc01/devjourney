pin=1234
bal=10000
mpin=int(input("enter pin:"))
if pin==mpin:
    amt=int(input("withdrawl amount:"))
    if bal>=amt:
        print("withdrawl successful")
    else:
        print("insufficient bal")
else:
    print("incorrect pin")