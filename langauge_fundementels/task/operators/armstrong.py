# num=int(input("enter a number:"))
# number=num
# result=0
# length=len(str(num))
# while(num!=0):
#     digit=num%10
#     expo=digit**length
#     result=result+expo
#     num=num//10
# if number==result:
#     print(number,"is armstrong")
# else:
#     print(number,"is not armstrong")
"""
palindrom
"""
num=int(input("enter a number:"))
number=num
result=0
while(num!=0):
    digit=num%10
    result=result*10+digit
    num=num//10
if result==number:
    print(number,"is palindrome")
else:
    print(number,"is not palindrome")
    