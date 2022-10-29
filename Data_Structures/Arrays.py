#An Array is basically like a list, but the difference between them is that an array specifically consists of data of the same data type
#Whereas a list can contain any data irrespective of it's data type
import array as a

Array = a.array('i', [1, 2, 3, 4])
print(Array) #printing an Array

#accessing the elements of an Array Via a for loop
for i in range(len(Array)):
    print(Array[i])

#The Indexes of an Array also begin from 0, just like in Lists
print(Array[0])
print(Array[3])

print(Array[1:3]) #Slicing an Array

Array.append(5) #Adding a new element to the Array, but it should be of the same data type as of the others in the array
print(Array)

Array.pop() #Removing the last element of the list
print(Array)

print(Array.typecode) #prints the type code of the Array
#A Typecode basically defines what kind of data type elements would be allowed in the array before hand.
#There's an entire list of typecodes, I myself don't remember it all :P