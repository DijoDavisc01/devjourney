
"""
"""
# from abc import ABC,abstractmethod
# class Bike(ABC):
#     @abstractmethod
#     def start(self):
#         print("starting method")
#     @abstractmethod
#     def stop(self):
#         print("stoping method")
# class Splendor(Bike):
#     def start(self):
#         print("splendor starting")
#     def stop(self):
#         print("splendor stoping")
# splendor_instance=Splendor()
# splendor_instance.start()
# splendor_instance.stop()
"""
"""
# from abc import ABC,abstractmethod
# class Editor(ABC):
#     @abstractmethod
#     def open(self):
#         print("open method")
#     @abstractmethod
#     def exicute(self):
#         print("exicute method")
#     @abstractmethod
#     def debug(self):
#         print("debug method")
# class Vscode(Editor):
#     def open(self):
#         print("vscode opening method")
#     def exicute(self):
#         print("vscode exicute method")
#     def debug(self):
#         print("vscode debugging method")
# vscode_instance=Vscode()
# vscode_instance.open()
# vscode_instance.exicute()
# vscode_instance.debug()

"""
*args -type of args is tuple,used in more values 
"""
# def add(*args):
#     return sum(args)
# print (add(10,20))
# print (add(10,20,20))

# def larg(*args):
#     return max(args)
# print(larg(1,2,3,4,0))
"""
"""
# def even_count(*args):
#     count=0
#     for n in args:
#         if n%2==0:
#             count+=1
#     return count 
# print(even_count(1,2,3,4,5,6))

# def odd_count(*args):
#     odds=[n for n in args if n%2!=0]
#     return len(odds)
# print(odd_count(1,2,3,4,5,6,7))
"""
"""
# def product(*args:tuple):
#     prod=1
#     for n in args:
#         prod*=n
#     return prod
# print(product(1,2,3,4,5,6,7))
"""
keyword args ,type of **kwargs is dictionary
"""        
# def emp_details(**kwargs:dict):
#     print(kwargs)
#     print(kwargs.get("sal"))
# emp_details(name="dijo",id=1001,sal=150000)
"""
*args and **kwargs combination
"""
# def cal(*args,**kwargs):
#     if kwargs.get("key")=="+":
#         return sum(args)
#     if kwargs.get("key")=="*":
#         prod=1
#         for n in args:
#             prod*=n
#         return prod
    
#     if kwargs.get("key")=="-":

#         return 
    
# print(cal(1,2,3,4,5,key="+"))
# print(cal(1,2,3,key="*"))
"""

"""
# def analyser_number(*args,**kwargs):
#     if kwargs.get("action")=="max":
#         return max(args)
#     if kwargs.get("action")=="min":
#         return min(args)
#     if kwargs.get("action")=="count":
#         return len(args)
# print(analyser_number(1,2,3,5,action="count"))
# print(analyser_number(1,2,3,5,action="max"))
# print(analyser_number(1,2,3,5,action="min"))
"""
"""
# def num_chek(*args,**kwargs):
# #     if kwargs.get("type")=="odd":
# #         for n in args:
# #             if n%2!=0:
# #                 return len(n)
# #     if kwargs.get("type")=="even":
# #         for n in args:
# #             if n%2==0:
# #                 return len(n)
# #     if kwargs.get("type")=="pos":
# #         for n in args:
# #             if n>0:
# #                 return len(n)
# #     if kwargs.get("type")=="neg":
# #         for n in args:
# #             if n<0:
# #                 return len(n)

#     type=kwargs.get("type")
#     if type=="odd":
#         odds=[n for n in args if n%2!=0]
#         return len(odds)
#     elif type=="even":
#         evens=[n for n in args if n%2==0]
#         return len(evens)
#     elif type=="pos":
#         pos=[n for n in args if n>0]
#         return len(pos)
#     elif type=="neg":
#         neg=[n for n in args if n<0]
#         return len(neg)
    
    

# print(num_chek(1,2,3,5,type="odd"))
# print(num_chek(1,2,3,5,type="even"))
# print(num_chek(1,2,3,5,-1,-2,type="pos"))     
# print(num_chek(-1,2,3,4,5,type="neg"))     
"""

"""
def mark_cal(*args,**kwargs):
                