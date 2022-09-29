#A Set is an Unordered list with curly brackets used to remark a set, and returns unique values of the set, when printed

#The set can also be used as a list, and regular functions that were used in functions can be used in a set
a = {1, 2, 3, 4, 5, 6, "Apples", "Mangoes"}

a.add("HD")
print(a)

a.pop()
print(a)

#Index related functions can't be used in a set, as It's an unordered list

#We can even access the values of the set Via a for loop
for i in a:
    print(i)

#We can even use the discard() method to remove a specific element in a set
a.discard("HD")
print(a)

