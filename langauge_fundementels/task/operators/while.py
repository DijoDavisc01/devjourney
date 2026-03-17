"""write a program to display 1 to 10
"""
# i=1#intialise value of i =1
# while(i<=10):#condition to check i less than or equal to 10 
#    print(i)# to display value of i
#    i= i+1# to incriment the value of I +1
"""
write a program display number 50 to 100
"""
# i=50#intialise value of i =50
# while(i<=100):#condition to check i less than or equal to 100 
#     print(i,)# to display value of i
#     i=i+1# to incriment the value of I +1

"""
write a program to print even or odd from 1 to 10
"""
# i=1
# while(i<=10):
#    if i%2==0:
#       print(i,"even")
#    else:
#       print(i,"odd")
#    i=i+1
"""
write a program to print even or odd 50 to 100
"""
# i=50
# while(i<=100):
#    if i%2==0:
#     print(i,"even")
#    i=i+1
"""
display 1800 to 2026
"""
# i=1800
# while(i<=2026):
#     print(i)
#     i=i+1
"""
century year
"""
# i=1800
# while(i<=2026):
#     if i%100==0:
#      print(i)
#     i=i+1
"""
non century year
"""
# i=1800
# while(i<=2026):
#     if i%100!=0:
#      print(i)
#     i=i+1
"""
leap year
"""
# i=1800
# while(i<=2026):
#     if (i%100==0 and i%400==0) or (i%100!=0 and i%4==0):
#      print(i)
#     i=i+1

"""
factorial of a num
"""
# num=int(input("enter a number:"))
# i=1
# result=1
# while(i<=num):
#     result=result*i
#     i=i+1
# print("factorial of",num,"is",result)
"""
sum of given numbers
"""
# num=int(input("enter a number:"))
# i=1
# result=0
# while(i<=num):
#     result=result+i
#     i=i+1
# print("sum of",num,"is",result)
"""
sum of even num upto number
"""
# num=int(input("enter a number:"))
# i=1
# result=0
# while(i<=num):
#     if i%2==0:
#       result=result+i

#     i=i+1
# print(result)
"""
sum of odd numbers and sum of even numbers upto limit6
"""
# num=int(input("enter a number:"))
# i=1
# result_even=0
# result_odd=0
# while(i<=num):
#     if i%2==0:
#         result_even=result_even+i

#     else:
#         result_odd=result_odd+i
#     i=i+1
# print(result_even)
# print(result_odd)
"""
last digits to first digit
"""
# num=int(input("enter number:"))
# while(num!=0):
#     last_digit=num%10  #123%10=3,12%10=2,....
#     print(last_digit)
#     num=num//10   #number=123//10=12,num=12//10=1,num=1//10=0
"""
display the even last digits
"""
# num=int(input("enter a number:"))
# while(num!=0):
#     last_even_digit=num%10
#     if num%2==0:
#       print(last_even_digit)
#     num=num//10
"""
sum of the given digit
"""
# num=int(input("enter a number"))
# sum=0
# while(num!=0):
#     last_digit=num%10 #123%10=3  12%10=2 1%10=1
#     sum=sum+last_digit #sum=0 so 0=0+3=3(last digit+lastdigit )+2 +1
#     num=num//10
# print(sum)
"""
sum of qube of last digits
"""
# num=int(input("enter number:"))
# sum=0
# while(num!=0):
#     last_digit=num%10
#     sum=sum+last_digit**3
#     num=num//10
# print(sum) 
"""
count of digit
"""
num=int(input("enter a number"))
result=0
while(num!=0):
    last_digit=num%10
    result=result*10+last_digit
    num=num//10
