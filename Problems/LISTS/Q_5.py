#WAP TO FIND THE AVERAGE OF A LIST
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = len(a)
b = 0
for i in a:
    b = b + i
average = b / size
print(average)