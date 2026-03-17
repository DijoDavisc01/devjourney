"""
w.a.p to display least positive missing integer from list with +ve numbers

sample input1:
    lst=[1,2,3,5]

    o/p => 4

sample input2:
    lst=[2,3,4,5]

    o/p => 1

sample input3:
    lst=[1,2,3,4,5]
    o/p=>6
"""
# lst=[1,2,3,4,5]
# length=len(lst)
# for i in range(1,length+1):
#     if i not in lst:
#         print(i)
#         break
# else:
#     print(length+1)
"""
"""
# lst=[1,2,3,5]
# lst.sort()
# prev=0
# nxt=prev+1
# while(prev<=len(lst)-2):
#     diff=lst[nxt]-lst[prev]
#     if diff!=1:
#         print(lst[prev]+1,"is missing")
#         break
#     prev+=1
#     next=prev+1
"""
def by while
"""
# def missing_least_pos(arr):
#     arr.sort()
#     prev=0
#     nxt=prev+1
#     while(prev<=len(arr)-2):
#         diff=arr[nxt]-arr[prev]
#         if diff!=1:
#             print(arr[prev]+1,"is missing")
#             break
#         prev+=1
#         nxt=prev+1
# missing_least_pos([1,2,4])
"""
def by for
"""
# def missing_least_pos(arr):
#     arr.sort()
#     for prev in range(0,len(arr)-1):
#         nxt=prev+1
#         diff=arr[nxt]-arr[prev]
#         if diff!=1:
#             print(arr[prev]+1,"is missing")
#             break
#     else:
#         print(arr[-1]+1,"is missing")

# missing_least_pos([1,3,2,5,4])       
"""
find duplicate num without using any predifined fun
"""
# lst=[10,11,12,11,13,15,14,13]
# st=set()
# lst.sort()

# for prev in range(0,len(lst)-1):
#     nxt=prev+1
#     diff=lst[nxt]-lst[prev]
#     if diff==0:
#        st.add(lst[prev])
# print(st)
"""
def duplicate
"""
# def find_dupilcate(arr):
#     arr.sort()
#     for prev in range(0,len(arr)-1):
#         nxt=prev+1
#         diff=arr[nxt]-arr[prev]
#         if diff==0:
#             print(arr[prev])
# find_dupilcate([1,2,5,3,2,3])

"""
find duplicates from both list
"""
# lst1=[10,11,12,13,14]
# lst2=[8,11,14,15,16]

# lst1_st=set(lst1)
# lst2_st=set(lst2)
# print(lst1_st.intersection(lst2_st))


# lst1=[10,11,12,13,14]
# lst2=[8,11,14,15,16]
# print(lst1.extend(lst2))
# lst1.sort()
# for prev in range(0,len(lst1)-1):
#     nxt=prev+1
#     diff=lst1[nxt]-lst1[prev]
#     if diff==0:
#         print(lst1[prev])

# lst1=[10,11,12,13,14]
# lst2=[8,11,14,15,16]
# lst1.sort()
# lst2.sort()
# prev=0
# nxt=0
"""
two pair sum
"""
# arr=[2,3,4,5]
# arr.sort()
# lft=0
# rt=len(arr)-1
# targ=8
# for n in arr:
#     current_sum=arr[lft]+arr[rt]
#     if current_sum==targ:
#         print(arr[lft],",",arr[rt])
#         break
#     elif current_sum<targ:
#         lft+=1
#     elif current_sum>targ:
#         rt-=1
"""
"""
# arr=[2,3,4,5]
# arr.sort()

# lft=0
# rt=len(arr)-1
# targ=8

# while lft < rt:
#     current_sum = arr[lft] + arr[rt]

#     if current_sum == targ:
#         print(arr[lft], arr[rt])
#         break
#     elif current_sum < targ:
#         lft += 1
#     else:
#         rt -= 1

"""
"""
# class Shape:
#     def area(self,*args):
#         if len(args)==1:
#             r=args[0]
#             circle=3.14*(r**2)
#             print(circle)
#         elif len(args)==2:
#             l=args[0]
#             b=args[1]
#             rectangle=l*b
#             print(rectangle)
#         elif len(args)==3:
#             l=args[0]
#             b=args[1]
#             h=args[2]
#             cuboid=l*b*h
#             print(cuboid)
        
# shape=Shape()            
# shape.area(2,2)
"""
"""
# source="dijodavisc"
# target="dijo"
# present=True
# for l in target:
#     if l not in source:
#         present=False
#         break
# print(present)
"""
"""
# class Container():
#     def solution(self,source:str,target:str):
#         present=True
#         for l in target:
#             if l not in source:
#                 present=False
#                 break

#         return present
# Container_insatnce=Container()
# print(Container_insatnce.solution("dijodavisc","dijo"))
"""
"""
# shallow copy = create a copy of outer object copy().
# = points to same memory location

arun_fvt_colors = ["red","green","blue"]

hari_fvt_colors = arun_fvt_colors.copy() # shallow copy

hari_fvt_colors[0] = "purple"

print(arun_fvt_colors) #['red', 'green', 'blue']
print(hari_fvt_colors) #['purple', 'green', 'blue']

print(arun_fvt_colors is hari_fvt_colors) # False bcoz both point to separate objects, True only when both point to same objects
"""
"""
# from copy import deepcopy
# arun_fav_food=[
#     {"type":"breakfast","food":"tea"},
#     {"type":"lunch","food":"meals"},
#     {"type":"dinner","food":"salad"},
# ]
# my_fav_food=deepcopy(arun_fav_food)
# my_fav_food[0]["food"]="dosa"
# print(arun_fav_food,"\n",my_fav_food)
"""

"""
