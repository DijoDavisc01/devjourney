"""
Create two classes Dog and Cat. Both classes should have a method sound(). Print different sounds for each animal
"""
class Dog:
    def sound(self):
        print("bow bow")
class Cat(Dog):
    def sound(self):
        print("meow..")
dog_instance=Cat()
dog_instance.sound
cat_inistance=Cat()


    

        