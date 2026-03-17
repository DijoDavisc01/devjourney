"""
Write a program to swap two tuples
"""
# tup1=(1,2,3,4)
# tup2=(5,6,7,8)
# tup3=tup1
# tup1=tup2
# tup2=tup3
# print("tup1=",tup1)
# print("tup2=",tup2)
"""
create a tuple of numbers and find the maximum and minimum values without converting it into a list.
"""
# tup=(1,2,3,4,5)
# l=len(tup)

"""
Given a tuple of integers, create a new tuple with only even numbers.
"""
# tup=(1,2,3,4,5,6,7,8)
# up_tup=()
# for n in tup:
#     if n%2==0:
#         up_tup+=(n,)
# print(up_tup)
"""
Write a program to check whether an element exists in a tuple or not
"""
tup=(1,2,3,4,5)
element=tuple(input("enter the element u wnt to check:"))
if element in tup:
    print(element,"is in",tup)   
else:
    print(element,"is not in",tup)