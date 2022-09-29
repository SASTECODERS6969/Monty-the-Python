#A Tuple is basically a more rigid form of a list
a = 1, 2, 3, 4
print(a)
print(a[1])

for i in a:
    print(i)

a[0] = 23 #Will return an Error, a tuple is immutable
a.append(23) #Will return an error, no Values can be added to the tuple
a.pop() #Will return an error, No value can be removed in a tuple

#tuples can be nested
b = a, (7, 8, 9, 10)
print(b)

#A Tuple, once formed can't be edited.

#A list can be for instance be changed into a tuple
mylist = [1, 2, 3, 4]
mytuple = tuple(mylist)
print(mytuple)