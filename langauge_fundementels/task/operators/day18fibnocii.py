"""
fibonacci
"""
# prev=0
# cur=1
# print(prev,cur)
# for i in range(1,22):
#     next=prev+cur
#     print(next)
#     prev=cur
#     cur=next
"""
check 9 is in fibo
"""
# def is_fib(num):
#     is_fib=False
#     prev=0
#     curr=1
#     next=prev+curr
#     while(next<=num):
#         next=prev+curr
#         prev=curr
#         curr=next
#         if next==num:
#             is_fib=True
#             break
#     return is_fib
# print(is_fib(9))
# print(is_fib(3))

"""
string is sequence of character
"""
# name="dijo*davis"
# print(name.capitalize())
# print(name.casefold())
# print(name.index("jo"))
# print(name.rfind("d"))
# print(name.find("d"))
# print(name.count("i"))
# print(name.isalpha())
# print(name.isalnum())
# print(name.isdigit())
# print(name.startswith("di"))#to chek the word start with the given letter
# print(name.endswith("is"))#to chek the word ends with the given letter
# print(name.strip("\n"))# is used to remove the space from both ends like form the left and the right
# new_name=name.lstrip("\n")
# new_name=name.rstrip("\t")
# print(new_name)
"""
write pgm to display digits in sentance
"""
# text="i have1penand2pencilonecar"
# for ch in text:
#     if ch.isdigit():
#         print(ch)
"""
pgm to display the count of alphabet,count of digit,count of special char given below string
"""
text="aman##aplan**panamawith2car1bike"
count_digit=0
count_char=0
count_special=0
for ch in text:
    if ch.isalpha:
        count_char=count_char+1
    elif ch.isdigit:
        count_char=count_digit+1
    elif not ch.isalnum:
        count_special=count_special+1
print(f"count of digit{count_digit}count of alphabet{count_char}count of specila character{count_special}")
    