"""
linear search
"""
# class linearsearch():
#     def solution(self,arr,num):
#         is_present=False
#         for n in arr:
#             if n==num:
#                 is_present=True
#                 break
#         return is_present
# ls_instance=linearsearch()
# arr=[1,2,3,4,5,6,7,8,9,10]
# num=3
# print(ls_instance.solution(arr,num))
"""
binary search
"""
# arr=[1,2,3,6,5,4]
# arr.sort()
# low=0
# up=len(arr)-1
# num=int(input("enter a  number u wamt to check in arr:"))
# is_present=False
# while(low<=up):
#     mid=(low+up)//2
#     if num ==arr[mid]:
#         is_present=True
#         break
#     elif num<arr[mid]:
#         up=mid-1
#     elif num>arr[mid]:
#         low=mid+1
# print(is_present)
"""
"""
# class Binarysearch():
#     def solution(self,arr,num):
#         low=0
#         up=len(arr)-1
#         is_present=False
#         while(low<=up):
#             mid=(low+up)//2
#             if num ==arr[mid]:
#                 is_present=True
#                 break
#             elif num<arr[mid]:
#                 up=mid-1
#             elif num>arr[mid]:
#                 low=mid+1
#         return is_present
# bs_instance=Binarysearch()
# arr=[1,2,3,4,8,7,6,5,5]
# arr.sort()
# num=int(input("enter a  number u wamt to check in arr:"))
# print(bs_instance.solution(arr,num))       
"""
inheritance
"""
# class Parent:
#     def house(self):
#         print("parent class house method")
# class Child(Parent):
#     def mobile(self):
#         print("child class method")
# child_instance=Child()
# child_instance.mobile()
# child_instance.house()
"""
multilevel inheritance
"""
# class Grandparent():
#     def properties(self):
#         print("own properties")
# class Parent(Grandparent):
#     def house(self):
#         print("owned house")
# class Child(Parent):
#     pass
# child_inheritance=Child()
# child_inheritance.properties()
# child_inheritance.house()
"""
multiple inheritance
"""
# class Father():
#     def cooking(self):
#         print("father has cooking skill")
# class Mother():
#     def minimizing(self):
#         print("mother has minimizing skill")
# class Child(Father,Mother):
#     pass
# child_instance=Child()
# child_instance.cooking()
# child_instance.minimizing()
"""
constructor in inheritance
"""
# class Langauge():
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(self.name)
# class Framework(Langauge):
#     def __init__(self,name,fname):
#         super().__init__(name)
#         self.fname=fname
#     def display(self):
#         super().display()
#         print(self.fname)
# framework_instance=Framework("python","django")
# framework_instance.display()
"""
constructor in inheritance
"""
# class Brand:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(self.name)
# class Product(Brand):
#     def __init__(self,name,title,price):
#         super().__init__(name)
#         self.title=title
#         self.price=price
#     def display(self):
#         super().display()  
#         print(self.title,self.price)
# brand1=Product("apple","ipad",123124)     
# brand1.display()        
"""
polymorphism method overloading
"""
# class cal:
#     def add(self,n1,n2):
#         return n1+n2
#     def add(self,n1,n2,n3):
#         return n1+n2+n3
#     def add(self,n1,n2,n3,n4):
#         return n1+n2+n3+n4
    
# cal_instance=cal()
# print(cal_instance.add(1,2,3,4))
# print(cal_instance.add(1,2,3))
"""
polymorphism method overriding
child class redefines the method that defined in parent class
"""
# class Parent:
#     def bike(self):
#         print("splendor")
#     def car(self):
#         print("alto")
# class Child(Parent):

#     def car(self):
#         print("thar")
# child_instance=Child()
# child_instance.car()
# child_instance.bike()
"""
"""
class Shape:
    def area(self):
        print("find area of shape")
class Sqr(Shape):
    def __init__(self,n):
        self.n=n
    def area(self):
        print("area of sqr",self.n**2)
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("area of rectangle",self.l*self.b)
sqr_instance=Sqr(2)
sqr_instance.area()
rect_instance=Rectangle(2,3)
rect_instance.area()