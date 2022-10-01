numbers = [1, 2, 3, 4, 5, 6]
#The following loop is going to print each individual element of the given list.
for i in numbers:
    print(i)

a = 0
#The loop will print the sum of alll the numbers of the given list
for i in numbers:
    a = a + i
    print(a)

#Looping over a range of numbers, and finding out the even and odd numbers amongst them
for i in range(1, 13):
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")

#Instead of the for loop, we can even use the sum() function, which is inbuilt
print(sum(range(1, 11)))
