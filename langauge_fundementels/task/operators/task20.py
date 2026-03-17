"""
Create a tuple with 5 numbers and print the second element
"""
# number=(1,2,3,4,5)
# print(number[1])
"""
Write a program to count how many times the value 10 appears in a tuple
"""
# num=(1,2,10,3,10,4,5,6,10)
# print(num.count(10))
"""
Create a tuple with different data types (int, float, string, bool) and print each element using a loop
"""
# datatypes=(1,2,3,1.2,1.5,1.1,"a","b","c",True,False)
# for dt in datatypes:
#     print(dt)
"""
Given a tuple (1, 2, 3, 4, 5), convert it into a list, add a new element, and convert it back to a tuple
"""
# num=(1,2,3,4,5)
# print(num)
# list=[]
# list.extend(num)
# print(list)
# list.append(6)
# print(list)
# num=()
# for n in list:
#     num+=(n,)
# print(num)
"""
Write a program to find the maximum and minimum value in a tuple.
"""
# num=(1,2,3,4,5)
"""
Create a set with 5 numbers and add a new number to it. Print the updated set.
"""
# num={1,2,3,4,5}
# num.add(6)
# print(num)

"""
Given two sets {1, 2, 3, 4} and {3, 4, 5, 6}, write a program to find:
* Common elements
* All unique elements from both sets
"""
# num1={1,2,3,4}
# num2={3,4,5,6}
# print("common elements:",num1.intersection(num2))
# print("all elements:",num1.union(num2))
"""
Write a program to remove a specific element from a set.
"""
# set={1,2,3,4,5}
# set.remove(3)
# print(set)
"""
Create a set from a list that contains duplicate values and print the result.
"""
# list=[1,2,3,2,4,2,3,5]
# st=set()
# for n in list:
#     st.add(n)
# print(st)
"""
Write a program to check whether a given value exists in a set or not
"""
set={1,2,3,4,5}
num=int(input("enter a num:"))
print("yes"if num in set else "no")
