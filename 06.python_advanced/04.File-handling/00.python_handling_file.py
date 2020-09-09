# %%
"""
# Read and write files
"""

# %%
"""
We have made good progress and now we can get down to the serious business of manipulating data files. This is one of the very important points concerning this training. 

"""

# %%
"""
To open/edit a file in python we use the "open()" function.

This function takes as first parameter the path of the file (relative * or absolute *) and as second parameter the type of opening

*A relative path in computing is a path that takes into account the reading location.*

*An absolute path is a complete path that can be read regardless of the reading location.*


"""

# %%
file = open("./data/data.txt", "r") # r for "read"

# %%
"""
* r, for a read opening (READ).

* w, for a write opening (WRITE), each time the file is opened, the content of the file is overwritten. If the file does not exist, python creates it.

* a, for an opening in add mode at the end of the file (APPEND). If the file does not exist, python creates it.

* x, creates a new file and opens it for writing
"""

# %%
"""
Like any open element, it must be closed again once the instructions have been completed. To do this, we use the close() method.
"""

# %%
file.close()

# %%
# Let's find out what's going on there
file = open("./data/data.txt", "r")
print (file.read())
file.close()

# %%
"""
Other possibility of opening without closing
"""

# %%
with open("./data/data.txt", "r") as fichier:
    print (fichier.read())

# %%
"""
Can you put the contents of this file in the form of a list in which each element is a sentence ?  
*(Use .split() for example...)*
"""

# %%


# %%
"""
To write in a file, just open a file (existing or not), write in it and close it, we impose "a" so that what is written is after the content of this file
"""

# %%
file = open("./data/write.txt", "a")
file.write("Hi everyone, I'm adding sentences to the file !")
file.close()

# %%
"""
Can you take the content of the data.txt file from the data directory, capitalize all the words and write them in the writing file after the existing one ?

"""

# %%
# It's up to you to write the end 
arr =[]
with open("./data/write.txt", "r") as fichier:
    return # Add your code




# %%
"""
## Management of directory paths...
"""

# %%
"""
This module is a library dedicated to file and folder management needs.
"""

# %%
import os

# %%
"""
Each file or folder is associated with a kind of address that makes it easy to find it without errors. It is not possible to identically name a file in the same folder (except if the extension is different).

There are two types of paths: the absolute path from the root of your file system and the relative path from the folder being read.
"""

# %%
# For python a path is a string, so there are methods to manipulate it.
import os.path

# %%
"""
By looking with the help function, we can see the available methods
"""

# %%
help(os.path)

# %%
"""
To know your current absolute path
"""

# %%
path=os.path.abspath('')
print(path)

# %%
"""
 The directory in which you work
"""

# %%
print(os.path.basename(path))

# %%
"""
Add a directory "text" in path
"""

# %%
rep_text=os.path.join(path, "text")
print(rep_text)

# %%
"""
It is possible to retrieve all the elements of a folder in a list using the listdir() method
"""

# %%
# Items are returned to a list and include folders and hidden files.
print(os.listdir("../"))

# %%
"""
### How to display all the elements of a folder as well as its child folders? 

With the function walk()
```
walk(top, topdown=True, onerror=None, followlinks=False)
```



"""

# %%
folder_path

# %%
import os
path=os.path.abspath('../')
folder_path = path

for path, dirs, files in os.walk(folder_path):
    for filename in files:
        print(filename)

# %%
"""
Put all the files in the text directory in a variable (check that they are only.txt files).

And copy the content of this variable into a file in the text directory that you will name: final.txt

"""

# %%



# %%
"""
And then, can you open all the files in your data directory and save all their contents in a variable, using a loop?
"""

# %%


# %%
"""
Finally, save this concatenated information (assemblies) in a new file 
"""

# %%
