import os
from pathlib import Path

folder_path = "/Users/aneesh/Desktop/Sample-Folder/"

files = os.listdir(folder_path)

for file in files:
    file_path = Path(os.path.join(folder_path, file))
    print(file_path.suffix)

'''
'Path(os.path.join(folder_path, file)) ' 
So this means  the particular path becomes the Obj of the Path Class and since its an object ,the obj has access to many methods like '.suffix' , if its not an obj it does not have access to any of the methods of Path Class 

Am I right ? I am asking this since I havent touched OOP in Python 

'''