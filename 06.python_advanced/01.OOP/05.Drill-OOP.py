# %%
"""
# Drill - OOP
"""

# %%
"""
## Exercise 01 - Dog Inheritance
Create a Pets class that holds instances of dogs; this class is completely separate from the Dog class. In other words, the Dog class does not inherit from the Pets class. Then assign three dog instances to an instance of the Pets class. Start with the following code below. Save the file as pets_class.py. Your output should look like this:
````
I have 3 dogs. 
Tom is 6. 
Fletcher is 7. 
Larry is 9. 
And they're all mammals, of course.
````
"""

# %%
# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# %%
"""
## Exercise 02 - Hungry Dogs
Using the same file, add an instance attribute of is_hungry = True to the Dog class. Then add a method called eat() which changes the value of is_hungry to False when called. Figure out the best way to feed each dog and then output “My dogs are hungry.” if all are hungry or “My dogs are not hungry.” if all are not hungry. The final output should look like this:
````
I have 3 dogs. 
Tom is 6. 
Fletcher is 7. 
Larry is 9. 
And they're all mammals, of course. 
My dogs are not hungry.
````

"""

# %%


# %%
"""
## Exercise 03 - Dog Walking
Next, add a walk() method to both the Pets and Dog classes so that when you call the method on the Pets class, each dog instance assigned to the Pets class will walk(). Save this as dog_walking.py. This is slightly more difficult.

Start by implementing the method in the same manner as the speak() method. As for the method in the Pets class, you will need to iterate through the list of dogs, then call the method itself.

The output should look like this:

````
Tom is walking!
Fletcher is walking!
Larry is walking!
````
"""

# %%
"""
## Exercise 04 - Comprehension Check 
Answer the following questions about OOP to check your learning progress:

1. What’s a class?
1. What’s an instance?
1. What’s the relationship between a class and an instance?
1. What’s the Python syntax used for defining a new class?
1. What’s the spelling convention for a class name?
1. How do you instantiate, or create an instance of, a class?
1. How do you access the attributes and behaviors of a class instance?
1. What’s a method?
1. What’s the purpose of self?
1. What’s the purpose of the __init__ method?
1. Describe how inheritance helps prevent code duplication.
1. Can child classes override properties of their parents?
"""

# %%
