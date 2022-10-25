import os
print(dir(os)) #Will print all functions available in this Module

print(os.getcwd()) #Will print the location of the directory in which we're working in

os.chdir('C:/Users/HP/') #Changes the Current working Directory
print(os.getcwd()) #The CWD Changes

#We can now list the files and folders present in the CWD By the following command:
print(os.listdir())

#To make a new Folder in the CWD, here's what to type in
os.mkdir('NEW_FOLDER_2')
print(os.listdir())

os.rmdir('NEW_FOLDER_2')
print(os.listdir())

#Renaming files:
os.rename('OS_Module_1.py', 'OS_Module_One.py')
print(os.listdir())