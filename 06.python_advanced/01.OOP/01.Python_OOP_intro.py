# %%
"""
# Introduction to object-oriented programming in python
"""

# %%
"""
An object is a type as can be 'str' for a string, 'float' for a float integer or 'int' for a real number.

For example, below are numerical types and iterable object types
"""

# %%
type(3),type(3.),type('azerty'),type([1,2,3]),type((3,4,'GGFD')),type({'boire':'avaler un liquide'})

# %%
"""
Or other object type
"""

# %%
type(type),type(None),type(True)

# %%
"""
In practice, objects are variables that can themselves contain functions and variables.  The "functions contained in our objects" are called methods.
"""

# %%
"""
So far, we have only seen one technical aspect of the object. I would even say that what we have seen so far is only a "slightly more aesthetic" way of encoding: it is simpler and more understandable to write my_list.append(5) than append_to_list(ma_liste, 5) where append_to_list would be a function that would add an element (5) at the end of the list (ma_liste).


But behind Object-Oriented Programming, there is not only an aesthetic concern, far from it.
"""

# %%
"""
"append" is therefore a method of the list class object of which ma_liste is a part
"""

# %%
"""
A class is a bit like a model according to which we will create objects. It is in the class that we will define our methods and attributes, the attributes being variables contained in our object.

### Methods are functions defined in a class.

"""

# %%
"""
### Example

A class defines attributes and methods. 

For example, imagine a Car class that will be used to create objects that are cars. 
This class will be able to define a color attribute, a speed attribute, etc. These attributes correspond to properties that can exist for a car. 

The Car class can also define a rolling method(). A method corresponds in a way to an action, here the action of driving can be performed by a car. 

If we imagine an Aircraft class, it will be able to define a fly() method. It will also be able to define a rolling method(). 

On the other hand, the Car class will not have a steal method() because a car cannot steal. Similarly, the Aircraft class may have an altitude attribute but this will not be the case for the Car class.
"""

# %%
"""
### Let's create a car class:
"""

# %%
"""
Our Car Class is a kind of factory that creates cars.

The ``__init__()`` method is called when creating an object. This is a special method, called a constructor, that is invariably called when you want to create an object from your class.

In concrete terms, a constructor is a method of our object that is responsible for creating our attributes. In truth, it is even the method that will be called when we want to create our object.
"""

# %%
class Car:
    def __init__(self):
        self.name = "Ferrari"

# %%
"""
In our constructor, we find the instantiation of our name attribute. We create a variable self.name and give it as value Ferrari.


An object is an instance of a class. You can create as many objects as you want with a class.

Now let's create our car:
"""

# %%
# Either bombo the name of my car
bombo=Car()

# %%
# A car class object
type(bombo)

# %%
bombo.name

# %%
# You can create an attribute for your object at any time:
bombo.model = "250"

# %%
bombo.model

# %%
"""

### Let's create a new Person class 
"""

# %%
"""
We still have to make a slightly smarter manufacturer. For the moment, whatever the object created, it has the same name, 

Let's create this time, a person class with name, first name, age and place of residence. You can change them later, of course, but you can also make the constructor ``(__init__(self))`` take several parameters, let's say... the name and the first name, to start with.
"""

# %%
class Person:
    """ Class defining a person characterized by :
    - his name
    - his first name
    - his age
    - his place of residence"""
    
    def __init__(self, name, firstname):
        """Constructor our class"""
        self.name = name
        self.firstname = firstname
        self.age = 34
        self.place_residence = "Brussels"

# %%
coCoach=Person('Patho','Ludovic')
print(coCoach)

# %%
"""
Let's look in detail:

First, the definition of the class. It consists of the keyword class, the name of the class and the two ritual points ":".

The definition of our manufacturer. As you can see, this is an almost "classic" definition of a function. Its name is__init__, it is invariable: in Python, all manufacturers are called that way. Method names surrounded on either side by two underlined signs (__name method__) are special methods. Note that, in our method definition, we pass a first parameter called self.

Remember that the first parameter must be self. Apart from that, a constructor is a rather classic function: you can define parameters, by default or not, named or not. When you want to create your object, you will call the name of the class by passing in brackets the parameters to use.
"""

# %%
coCoach.name,coCoach.firstname, coCoach.age,coCoach.place_residence

# %%
# His birthday? => 24/06/1984 // Don't forget to wish me Happy Birthday that day :)
coCoach.birthday

# %%
"""
Create a new attribute, birthday, for this object
"""

# %%


# %%
coCoach.birthday

# %%
"""
#### Class attributes
In the examples we have seen so far, our attributes are contained in our object. They are specific to the object: if you create several objects, the attributes name, first name,... of each one will not necessarily be identical from one object to another. But we can also define attributes in our class. 
"""

# %%
class Counter:
    """This class has a class attribute that is incremented at each
    time you create an object of this type"""

    
    objects_create = 0 # The counter is 0 at the start
    def __init__(self):
        """Each time we create an object, we increment the counte"""
        Counter.objects_create = Counter.objects_create + 1

# %%
"""
We define our class attribute directly in the body of the class, before the definition of the constructor. 

When you want to call it in the constructor, you prefix the name of the class attribute with the name of the class. 

And it is also accessed in this way, outside the classroom. See instead:
"""

# %%
Counter.objects_create

# %%
# Create a first object
a=Counter()
# Let's check that the counter has been incremented correctly
print(Counter.objects_create)

# %%
b=Counter()
print(b.object_create)

# %%
"""
Each time we create a Counter object, the class attribute objects_crees is incremented by 1. It can be useful to have class attributes, when all our objects must have some identical data.
"""

# %%
"""
### Method
"""

# %%
"""
Attributes are variables specific to our object, which are used to characterize it. The methods are rather actions, as we saw in the previous part, acting on the object. For example, the append method of the list class allows to add an element in the manipulated list object.
"""

# %%
"""
Let's create a Table class. Our table will have a surface (an attribute) on which we can write, read and delete. 

Create our Blackboard class and our surface attribute
"""

# %%
class Blackboard:
    """ Class defining a surface on which to write,
    that can be read and deleted, by a set of methods. The modified attribute
    is "surface" """

    
    def __init__(self):
        """By default, our surface is empty"""
        self.surface = ""

# %%
"""
We have already created a method, so you should not be too surprised by the syntax we will see. Our constructor is indeed a method, it keeps the syntax. So we will write our method write to start.
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

# %%
tab =  Blackboard()
# Check if blackboard is empty
print(tab.surface)

# %%
tab.write("Coooool ! Il love this one")
# It is good ?
print(tab.surface)

# %%
tab.write("Have a good start to the school year!")
print(tab.surface)

# %%
"""
when you create a new object, here a blackboard, the attributes of the object are specific to the created object. 
- This makes sense: if you create several blackboards, they will not all have the same surface area. So the attributes are contained in the object.

On the other hand, the methods are contained in the class that defines our object. 
- This is very important. When you type tab.write(...), Python will look for the write method not in the tab object, but in the Blackboard class. When you type tab.write(...), it is the same as if you write Blackboard.write(tab, ...).
"""

# %%
tab.write('Hello Swartz')
Blackboard.write(tab,'Hello Turing')

# %%
print(tab.surface)

# %%
# And yes, the help comes from reading the body of the associated class
help(Blackboard.write)

# %%
Blackboard.write(tab, "try")
print(tab.surface)

# %%
"""
As you can see,  
- Your self parameter is the object that calls the method. For this reason, you modify the surface of the object by calling self.surface.
- To summarize, when you have to work in a method of the object on the object itself, you will go through self.
"""

# %%
"""
We still have to code to read who will display our surface and delete, who will delete the content of our surface.

Write these two methods; one that displays the contents of the table and the other that resets it to zero or""
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
        """This method is in charge of displaying, thanks to print,
        the surface of the painting"""
        # to be completed
        
    def reset(self):
        """This method allows you to erase the surface of the table"""
        # to be completed
        

# %%
tab = Blackboard()
tab.read()

# %%
tab.write("Hello everyone")
tab.ecrire("Are you all right?")
tab.read()

# %%
tab.reset()
tab.read()

# %%
# It's worth the effort to get a good commentary on his classes, isn't it?
help(Blackboard)

# %%
"""
### Remember associated attributes / methods

The dir function returns a list containing the names of the attributes and methods of the object that is passed to it as a parameter. You can notice that everything is mixed, it's normal: for Python, methods, functions, classes, modules are objects. The first difference between a variable and a function is that a function is executable (callable). The dir function simply returns everything in the object, without distinction.
"""

# %%
dir(Blackboard)

# %%
"""
By default, when you develop a class, all objects built from that class will have a special attribute __dict__. This attribute is a dictionary that contains as keys the names of the attributes and, as values, the values of the attributes.
"""

# %%
Blackboard.__dict__

# %%
"""
### In summary
- A class is defined by following the syntaxeclass ClassName:.
- Methods are defined as functions, except that they are found in the body of the class.
- Instance methods take in first parameter self, the instance of the manipulated object.
- We build a class instance by calling its constructor, an instance method called__init__.
- The attributes of an instance are defined in the constructor of its class, following this syntax: self.name_attribute_name = value.
- All methods that start and end with double underscores like __str__ are methods common to (almost) all classes.
"""