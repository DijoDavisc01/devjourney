"""
1. Create a class Student with a constructor that initializes name and age. Create an object and display the details.
"""
# class Students():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name,self.age)
# std1_instance=Students("dijo",21)
# std1_instance.display()
# std2_instance=Students("alan",21)
# std2_instance.display()

"""
2. Create a class Rectangle with a constructor that takes length and width. Write a method to calculate the area of the rectangle.
"""
# class Rectangle():
#     def area(self,len,width):
#         area_of_rectangle=len*width
#         return area_of_rectangle
# rectangle_instance=Rectangle()
# len=int(input("enter length of rectangle:"))
# width=int(input("enter width of rectangle:"))
# print(Rectangle_instance.area("area =",len,width))
"""
3. Create a class Employee with a constructor that initializes employee name and salary. Display the employee details.
"""
# class Employee():
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print(self.name,self.salary)
# employee1_instance=Employee("dijo",100000)
# employee1_instance.display()
# employee2_instance=Employee("edwin",150000)
# employee2_instance.display()
"""
4. Create a class Car with a constructor that initializes brand and model. Print the car details using a method.
"""
# class Car():
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def display(self):
#         print(self.brand,self.model)
# car1_instance=Car("maruthi",2020)
# car1_instance.display()
# car2_instance=Car("tata",2025)
# car2_instance.display()
"""
5. Create a class Circle with a constructor that takes radius. Write a method to calculate the area of the circle.
"""
# class Circle():
#     def area(self,radius):
#         area_of_circle=3.14*(radius**2)
#         return area_of_circle
# Circle_area=Circle()
# radius=int(input("enter radius:"))
# print(Circle_area.area(radius))
"""
7. Create a class Product with a constructor that initializes product name and price. Print the product details.
"""
# class Product():
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def display(self):
#         print(self.name,self.price)
# product_instance=Product("pen",5)
# product_instance.display()
"""
8. Create a class Book with a constructor that initializes title and author. Display the book details.
"""
# class Book():
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def display(self):
#         print(self.title,self.author)
# book_insatnce=Book("me dijo","dijo")
# book_insatnce.display()
"""
9. Create a class Laptop with a constructor that initializes brand and RAM size. Print the laptop specifications.
"""
# class Lap():
#     def __init__(self,brand,ram):
#         self.brand=brand
#         self.ram=ram
#     def display(self):
#         print(self.brand,self.ram)
# lap_instance=Lap("hp",256)
# lap_instance.display()
"""
10. Create a class BankAccount with a constructor that initializes account holder name and balance. Display the account details.
"""
class Bank():
    def __init__(self,name,bal):
        self.name=name
        self.bal=bal
    def display(self):
        print(self.name,self.bal)
bank_instance=Bank("dijo",150000)
bank_instance.display()
