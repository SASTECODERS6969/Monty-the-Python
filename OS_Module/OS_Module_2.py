import os
print(os.getcwd())

os.chdir('C:/Users/HP/OneDrive/Desktop')
print(os.getcwd())

#To get information about a particular file

#print(os.stat('DHARMENDRA SHARMA(Adv) Resume.docx'))

file = os.open('C:/Users/HP/OneDrive/Desktop/DHARMENDRA SHARMA(Adv) Resume.docx', os.O_RDONLY)
data = os.read(file, 16)
print(data.decode('utf-8'))