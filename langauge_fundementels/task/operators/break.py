# for i in range(1,11):
#     if i==6:
#         break
#     print(i)
# print("...")
"""
continue
"""
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)
# print("....")

"""
pgm to display 1st vowel in a word
"""
# vowels="aeiou"
# for ch in word:
#     if ch in vowels:
#         print(ch)
#         break
"""
program to find a num is prime num
"""
# num=int(input("enter a number:"))
# prime=True
# for i in range(2,num):
#     if num%i==0:
#         prime=False
#         break
# print(prime)
"""
common diviser
"""
# num=int(input("enter a number:"))
# for i in range(1,num+1):
#     if num%i==0:
#         print(i)
"""
common diviser of two number
"""
# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# if num1<num2:
#     smallest=num1
# else:
#     smallest=num2
# for i in range(1,smallest+1):
#         if num1%i==0 and num2%i==0:
#             print(i)
"""
find gcd.greatest common diviser of a digit 
"""
# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# if num1<num2:
#     smallest=num1
# else:
#     smallest=num2
# gcd=1
# for i in range(1,smallest+1):
#     if num1%i==0 and num2%i==0:
#         gcd=i
# print(gcd)
"""
common diviser of 3 numbers
"""
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))
if num1<num2 and num1<num2:
    smallest=num1
elif num2<num1 and num2<num3:
    smallest=num2
else:smallest=num3
for i in range(1,smallest+1):
    if num1%i==0 and num2%i==0 and num3%i==0:
        print(i)