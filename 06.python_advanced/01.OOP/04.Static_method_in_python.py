# %%
"""
# What is a static method in python?

Static methods are methods within a class that have no access to anything else in the class (no self keyword or cls keyword). They cannot change or look at any object attributes or call other methods within the class. They can be thought of as a special kind of function that sits inside of the class. When we create a static method we must use something called a decorator. The decorator for a static method is "@staticmethod". In other words, you can create a callable class using the static method and use it with some restrictions.It helps developers write code in a safe architectural way to prevent conflicts in the code.

(We'll go deeper into the decorators later.)
"""

# %%
class Math:
    @staticmethod
    def Multiply(one, two):
        return one * two

# %%
math = Math()
if(12*72 == math.Multiply(12, 72)):
    print("Equal")
else:
    print("Not Equal")

# %%
"""
Check another program to use the built-in staticmethod() function.
"""

# %%
class Person:
    def Age(age):
        if(age <= 30):
            print("Young")
        elif(age>30 and age<=50):
            print("Middle Age")
        else:
            print("Senior Age")
John = Person
Type_of_age = staticmethod(John.Age(45))

# %%
