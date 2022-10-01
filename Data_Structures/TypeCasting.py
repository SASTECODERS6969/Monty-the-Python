#TypeCasting is the process in which we change one form of Data Structure into another Data Structure

#TypeCasting a list into Different Data Structures
a1 = [1, 2, 3, 4, 5, 6, 6, 7]
b = set(a1)
print(b) #Will return a set b
c = dict(a1)
print(c) #Will return an error

#TypeCasting a Dictionary into different Data Structures
number_names = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3,
}
print(number_names)

other_list = list(number_names)
print(other_list) #Will return a list

other_set = set(number_names)
print(other_set) #Will return a set

#TypeCasting a Set into different Data Structures
names = {"Rinki", "Pinki", "Chinki", "Minki", "Munni"}
print(names)

collection_of_names = list(names)
print(collection_of_names)

name_of_girls = dict(names)
print(name_of_girls) #Returns an error?