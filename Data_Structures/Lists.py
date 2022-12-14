numbers = [1, 2, 3, 4, 5, 6]

#Printing the entire list
print(numbers)

#Using the for loop to print all the elements of the List one by one
for i in numbers:
    print(i)

#Slicing the list
print(numbers[2:4])
print(numbers[1 : 5])

#Printing a single element using it's Index Value (The Index values of a list begins with 0 for the first element, and so on.)
#For reference:
# P Y T H O N
# 0 1 2 3 4 5
# -6 -5 -4 -3 -2 -1

print(numbers[3])
print(numbers[0])
print(numbers[-3])

#A list can consist of different data types, and it'll work the same as with the other functions given above
Random_list = ["YajnanHD", 10, "D", 78.989234]

for i in Random_list:
    print(i)

print(Random_list[-3])

#Changing the values of lists, its easy to do so
another_list = [1, 2, 3, 4, 5, 6]
another_list[4] = 67
print(another_list)

#It's also possible to nest different kinds of list into a single one
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
c = [a, b]
print(c)

#Quite the same thing as done in line 40, but here we add 2 different lists to form a new list with the combined elements of the 2 lists
d = [a + b]
print(d)

Data = [1, 2, 3, 4, "YajnanaHD", 89.323128790]
Data.append("Coder")
print(Data)

Data.pop()
print(Data)


