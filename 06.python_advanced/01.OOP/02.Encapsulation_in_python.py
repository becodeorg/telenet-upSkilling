# %%
"""
# Encapsulation in Python
"""

# %%
"""
Encapsulation is one of the fundamental concepts of object-oriented programming (OOP). It describes the idea of data encapsulation and the methods that work with data within a unit. It limits direct access to variables and methods and can prevent accidental modification of data. To prevent accidental modification, the variable of an object can only be modified by the method of an object. 

In C++, Java, or PHP things are pretty straight-forward. There are 3 magical and easy to remember access modifiers, that will do the job (public, protected and private). But there’s no such a thing in Python.  

That said, there is a way to simulate these behaviours. We are going to see how to do it.
"""

# %%
"""
## Public method 
"""

# %%
"""
All methods and attributes default to public in Python.   
So if you want to put your attributes and methods in public you don't have to do anything at all.
"""

# %%
class Blackboard:
    """ Class defining a surface on which to write,
    that can be read and deleted, by a set of methods. The modified attribute
    is "surface" """


    
    def __init__(self):
        """By default, our surface is empty"""
        self.surface = ""
        
    def write(self, message_written):
        """ Method for writing on the surface of the table.
        If the surface is not empty, we skip a line before adding
        the message to be written"""
        
        if self.surface != "":
            self.surface += '\n'
        self.surface += message_written
    
    def read(self):
        return self.surface

# %%
board = Blackboard()
board.write("an another message")
board.surface = "Hello guy's"
board.read()

# %%
"""
## Protected method
"""

# %%
"""
Protected member is (in C++ and Java) accessible only from within the class and it’s subclasses. How to accomplish this in Python?   
The answer is _ by convention. By prefixing the name of your member with a single underscore, you’re telling others “don’t touch this, unless you’re a subclass”
"""

# %%
class Blackboard:
    """ Class defining a surface on which to write,
    that can be read and deleted, by a set of methods. The modified attribute
    is "surface" """


    
    def __init__(self):
        """By default, our surface is empty"""
        self._surface = ""
        
    def write(self, message_written):
        """ Method for writing on the surface of the table.
        If the surface is not empty, we skip a line before adding
        the message to be written"""
        
        if self._surface != "":
            self._surface += '\n'
        self._surface += message_written
    
    def read(self):
        return self._surface

# %%
"""
But it's just a convention. If you try to change the attribute anyway, it won't cause an error and the attribute will change. 
"""

# %%
board = Blackboard()
board.write("an another message")
board._surface = "Hello guy's"
board.read()

# %%
"""
## Private method
If you want to make your methods and attributes inaccessible, even for child classes, then you must declare them privately. And how do you simulate a private declaration in python? 

We use the [name mangling!](https://en.wikipedia.org/wiki/Name_mangling#Name_mangling_in_Python)

And for this case, we use a double underscore.
"""

# %%
class Blackboard:
    """ Class defining a surface on which to write,
    that can be read and deleted, by a set of methods. The modified attribute
    is "surface" """


    
    def __init__(self):
        """By default, our surface is empty"""
        self.__surface = ""
        
    def write(self, message_written):
        """ Method for writing on the surface of the table.
        If the surface is not empty, we skip a line before adding
        the message to be written"""
        
        if self.__surface != "":
            self.__surface += '\n'
        self.__surface += message_written
    
    def read(self):
        return self.__surface

# %%
board = Blackboard()
board.__surface = "Hello guy's"
board.read()

# %%
"""
This time we can see that the value of the attribute self.__surface has not changed. 
"""