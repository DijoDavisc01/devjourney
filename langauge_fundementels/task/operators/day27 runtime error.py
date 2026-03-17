# n1=int(input("enter a num:"))
# n2=int(input("enter a num:"))
# try:
#     res=n1/n2
#     print(res)
# except Exception as a:
#     print(a)
# print("corrupt the error")


# lst=[1,2,3,4,5]
# index=int(input("enter  index:"))
# try:
#     print(lst[index])
# except Exception as a:
#     index=int(input("enter index:"))
#     print(lst[index])
#     try:
#         print(lst[index])
#     except Exception as a:
#         index=int(input("enter valid index:"))
#         print(lst[index])
# finally:

#         print("corrupt the error")


# age=int(input("enter ur age:"))
# if age<18:
#     raise Exception ("invalid age")
# else:
#     print("access granted")


"""
read a password
if length of password is<6 create error in password
"""
# pwd=input("enter input pwd:")
# if len(pwd)<6:
#     raise Exception ("invalid password!!")
# else:
#     print("grant access")

"""
Create a program that:
Takes student name
Takes course fee
Takes amount paid
Raise error if:
Fee is negative
Paid amount is negative
Paid amount is greater than fee
Handle invalid input
Always print "Registration Process Finished" using finally
"""
# name=input("enter std name:")
# fee=int(input("enter std fee:"))
# paid_fee=int(input("enter std fee:"))
# try:
#     if fee<=0:
#         raise Exception("fee is neg!!")
#     if paid_fee<=0:
#         raise Exception("invalid!!")
#     if paid_fee>fee:
#         raise Exception("fee is incorrect !!")
# except Exception as e:
#     print(e)
# finally:
#     print("registration process finished....")
# """
"""
assert
"""
# def cube(num):
#     res=0
#     res=num**3
#     return res
# assert cube(3)==2,"test case1 failed"
# assert cube(4)==64,"test case2 failed"
# print("code copied")
def max_two(n1,n2):
    res=1
    if n1>n2:
        res=n1
    else:
        res=n2
    return res
assert max_two(10,20)==20,"test case1 failed"
assert max_two(-10,5)==5,"test case2 failed"
print("code copied")