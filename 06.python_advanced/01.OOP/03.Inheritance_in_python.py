# %%
"""
# The inheritance
## Building a class from an already known one

Inheritance is an object feature that allows you to declare that a particular class will itself be modeled on another class, called the parent class. In concrete terms, if a class "b" inherits the class "a", objects created on the model of the class "b" will have access to the methods and attributes of the class "a".

Class "b" does not only use the methods and attributes of class "a": it will also be able to define others. Other methods and attributes that will be specific to it, in addition to the methods and attributes of class "a". And it will also be able to redefine the methods of the mother class.

Example: A secret agent is a person with a specificity. We can therefore create a Special Agent class that inherits from the Person class. 
"""

# %%
class Person:
    """Class representing one person"""
    def __init__(self, name,firstname):
        """Constructor our class"""
        self.name = name
        self.firstname = firstname
    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Person):
    """A class that defines a special agent.
    She inherits the class Person"""
    
    def __init__(self, name,firstname, matricule):
        """An agent is defined by his name and personnel number"""
        # We explicitly call the Person Builder:
        Person.__init__(self, name,firstname)
        self.matricule = matricule
    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return "Agent {0}. {2} {0}, matricule {1}".format(self.name, self.matricule,self.firstname)

# %%
agent_007=AgentSpecial('Do','Lu','007')
print(agent_007)

# %%
"""
- Inheritance allows one class to inherit another's behaviour by using its methods.

- The syntax of the inheritance is NewClass class (ParentClass):.

- The methods of the parent class can be accessed directly via the syntax: ParentClass.method(self).

- Multiple inheritance allows a class to inherit several Parent Classes.

- The syntax of the multiple inheritance is therefore written as follows: New Class class (ParentClass1, ParentClass2, ParentClassN):.
"""

# %%
"""
Another example : 
"""

# %%
#parent Class
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def speak(self):
        print(f"I am {self.name} and I am {self.age} Old.")
    
#child class
class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        self.type = "dog"

#call child class
t = Dog("Snoopy", 5)
t.speak()

# %%
"""
### Super() function

Python super() function allows us to refer the superclass implicitly. So, Python super makes our task easier and comfortable. While referring the superclass from the subclass, we don’t need to write the name of superclass explicitly. In the following sections, we will discuss python super function.
"""

# %%
#parent Class
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(f"I am {self.name} and I am {self.age} Old.")
    
#child class
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name,age)
        self.type = "dog"


#call child class
t = Dog("Snoopy", 5)
t.speak()

# %%
"""
### Python super function with multilevel inheritance  
As we have stated previously that Python super() function allows us to refer the superclass implicitly.

But in the case of multi-level inheritances which class will it refer? Well, Python super() will always refer the immediate superclass.

Also Python super() function not only can refer the __init__() function but also can call all other function of the superclass. So, in the following example, we will see that.
"""

# %%
class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('Printing from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)


if __name__ == '__main__':
    c = C()
    c.sub_method(1)


# %%
"""
So, from the output we can clearly see that the __init__() function of class C had been called at first, then class B and after that class A. Similar thing happened by calling sub_method() function.
"""

# %%
"""
### Why do we need Python super function
If you have previous experience in Java language, then you should know that the base class is also called by a super object there. So, this concept is actually useful for the coders. However, Python also keeps the facility for the programmer to use superclass name to refer them. And, if your program contains multi-level inheritance, then this super() function is helpful for you.

We always call the original method implementation? In theory a well designed API should make it always possible but we know that boundary cases exist: the original method may have side effect that you want to avoid and sometimes the API cannot be refactored to avoid them. In those cases you may prefer to skip the call to the original implementation of the method; Python does not make it mandatory, so feel free to walk that path if you think the situation requires it. Be sure to know what you are doing, however, and document why you are completely overwriting the method.
"""

# %%
"""
### Overriding method
What is overriding? Overriding is the ability of a class to change the implementation of a method provided by one of its ancestors.

Overriding is a very important part of OOP since it is the feature that makes inheritance exploit its full power. Through method overriding a class may "copy" another class, avoiding duplicated code, and at the same time enhance or customize part of it. Method overriding is thus a strict part of the inheritance mechanism.
"""

# %%
#parent Class
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def speak(self):
        print(f"I am {self.name} and I am {self.age} Old.")
    
#child class
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name,age)
    
    def speak(self):    # This will Override  parents class;
        print("I am A Dog")

#call child class
t = Dog("tyson", 5)
t.speak()
    

# %%
