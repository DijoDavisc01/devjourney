"""
1. Write a Python program to create a list and make a shallow copy of it using the copy() method.
"""
clr=["black","white","grey","red"]
fav_clr=clr.copy()
fav_clr[0]="gold"
# print(clr,"\n",fav_clr)
"""
2. Write a program to demonstrate shallow copy using the copy module.
"""
from copy import copy
clr=["black","white","grey","red"]
fav_clr=clr.copy()
fav_clr[3]="gold"
# print(clr,"\n",fav_clr)

"""
3. Create a list containing nested lists. Perform a shallow copy and modify the inner list. Print both lists and observe the result.
"""
lst_u=[
    {"car":"benz","model":2000,"price":1000000},
    {"car":"bmw","model":2002,"price":1500000},
]
lst_a=lst_u.copy()
lst_a[0]["car"]="bmw"
# print(lst_u,"\n",lst_a)
"""
4. Write a Python program to perform deep copy using the deepcopy() function from the copy module.
"""