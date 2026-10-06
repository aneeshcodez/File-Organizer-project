import os
from pathlib import Path

folder_path = "/Users/aneesh/Desktop/Sample-Folder/"

files = os.listdir(folder_path)

os.mkdir("PDF FOLDER")

def fff():




for file in files:
    file_path = Path(os.path.join(folder_path, file))
    if(file_path.suffix == ".pdf"):
        # I have to send this file to a function which adds this particular file to the pdf folder and
        # and I also have to not to create the pdf folder again and again
        print(file_path)



'''
'Path(os.path.join(folder_path, file)) ' 
So this means  the particular path becomes the Obj of the Path Class and since its an object ,the obj has access to many methods like '.suffix' , if its not an obj it does not have access to any of the methods of Path Class 

Am I right ? I am asking this since I havent touched OOP in Python 

'''

'''
we got extension : pdf , jpg
we have to put them in respective folder -> maybe create a function and 
send it -> and in that function we call many diff respective function -> But now as 
you see we can avoid the middle function and can directly call respective function 
once we know the extension.
We should also not create folders everytime 
-> First see how you can do it simple and execute it , rest we will figure out from there
IMP : check before doing any operation
'''

# doubt : In python should we create function before itself , cannot it come after