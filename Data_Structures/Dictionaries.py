Details = {
    "Name" : "YajnanaHD",
    "Class" : 10,
    "Age" : 15,
}
#A Dictionary is a lind of Data Structure which stores data in a unique way than the other data strctures
#A Dictionary first makes a list of keys, and to each key is assigned a value

#We can access the data in the dictionaries in a manner similar to the lists
#But instead of the index numbers, we have to write down the key of that particular data

print(Details["Name"])
print(Details["Class"])
print(Details["Age"])

for i in Details:
    print(i) #We mainly get the Keys of the given Dictionary

Details["Height"] = 180
print(Details)

Details.pop("Height") #Here, while using the pop() function, we have to specify the specific key
print(Details)

#Nested Dictionary
Random_Dictionary = {
    "Name" : "Hello",
    "a" : {
        "Class" : 12,
        "RollNo" : 336548623
    }

}
print(Random_Dictionary)