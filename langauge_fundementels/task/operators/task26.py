"""
1. Write a lambda function to find the square of a number.
"""
# sqr=lambda num:num**2
# print(sqr(3))
"""
2. Create a lambda function to check whether a number is even or odd.
"""
# odd=lambda num:num%2!=0
# print(odd(3))
"""
3. Use a lambda function to find the maximum of two numbers.
"""
# maximum=lambda n1,n2:max(n1,n2)
# print(maximum(8,3))
"""
4. Write a Python program to sort a list of tuples based on the second element using a lambda function.
"""
# lst=[("q",1),("b",2),("c",3),]
# lst.sort(key=lambda tp:tp[1])
# print(lst)
# print(sorted(lst,key=lambda tp:tp[1],reverse=True))

"""
5. Use a lambda function with filter() to get all even numbers from a list.
"""
lst=[1,2,3,4,5,6,7,8,9,10]

# sqr_lst=list(map(lambda n:n**2,lst))
# print(even_lst)
# even_lst=list(filter(lambda n:n%2==0,lst))
# print(even_lst)