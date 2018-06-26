import os
from string import digits
list_files = os.listdir("C:\\Users\\lab7-14\\Desktop\\new\\prank")
os.chdir("C:\\Users\\lab7-14\\Desktop\\new\\prank")
for file in list_files:
    '''old_names = file
    #print (old_names)
    new_names = old_names.lstrip(digits)
    print (new_names)
    os.renames(old_names, new_names)'''
    new_names = file.lstrip(digits)
    print (new_names)
    os.renames(file,new_names)