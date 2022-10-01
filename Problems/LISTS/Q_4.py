#WAP TO REVERSE A LIST
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in range(11, 1, -1):
    b.append(i)
print(b)
#or 
a.reverse()
print(a)