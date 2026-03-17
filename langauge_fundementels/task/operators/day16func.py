
"""
deff function_name(p1,p2,,,,)
function body

funtion with no parameter and no return value
"""
# def say_hello():
#     print("hello")
# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()
"""
funtion with parameter and no return value
"""
# def addition(num1,num2):
#     result=num1+num2
#     print("addition",result)
# addition(123,456)
# def sub(num1,num2):
#     res=num1-num2
#     print(res)
# sub(200,50)
"""
cube
"""
# def cube(num1,num2):
#     res=num1**num2
#     print(res)
# cube(2,3)
"""
display largest num
"""
# def larg(num1,num2):
#     if num1>num2:
#         largest=num1
#     else:
#         largest=num2
#     print(largest)
# larg(3,2)
"""
print num when the last digit is greater 
"""
# def last_digit_max(num1,num2):
#     if num1%10>num2%10:
#         print(num1)
#     else :
#         print(num2)
# last_digit_max(12,111)
"""
funtion with  parameter and return value
"""
# def add(n1,n2):
#     result=n1+n2
#     return result
# print(add(100,10))
"""
if n1>n2 n1=n2 or n2>n1 n2-n1 use this fun in sub
"""
# def smart_sub (n1,n2):
#     if n1>n2:
#      return n1-n2
#     else:
#      return n2-n1  
# print(smart_sub(20,8)) 
# print(smart_sub(8,20))
"""
is odd print true else false
"""
# def is_odd(n1):
#     return n1%2!=0
# print(is_odd(2))
"""
is even
"""
# def is_even(num):
#     return num%2==0
# print(is_even(2))
"""
is positive
"""
def is_pos(num):
    return num>0
# print(is_pos(3))
"""
is zero
"""
# def is_zero(num):
#     return num==0
# print(is_zero(7))
"""
exponent
"""
# def expo(base,pow=2):
#     result=base**pow
#     return result
# print(expo(10,pow=3))
"""
calculator
"""
def calc(n1,n2,op):
    match op:
        case "+":print(f"{n1}+{n2}={n1+n2}")
        case "-":print(f"{n1}-{n2}={n1-n2}")
        case "/":print(f"{n1}/{n2}={n1/n2}")
        case "*":print(f"{n1}*{n2}={n1*n2}")
        case "%":print(f"{n1}%{n2}={n1%n2}")
        case _:print("....")
    return calc
print(calc(2,3,"+"))
print(calc(2,3,"*"))
print(calc(2,3,"/"))
print(calc(2,3,"%"))
print(calc(2,3,"-"))