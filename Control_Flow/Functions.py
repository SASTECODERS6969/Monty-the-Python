
#A Function to greet
def greeting():
    print("Hola! Hope you're doing great!")

greeting()

#A function to add 2 numbers
def addition(a, b, c):
    print(a + b + c)

addition(23, 23, 432)

#A Function to compare 2 Numbers
def comparison(a = int, b = int):
    if a > b:
        print(a, "Is greater")
    elif b > a:
        print(b, "Is greater")
    else:
        print("both are equal")

comparison(1, 1)

#A Function to add 2 numbers
def addition(a = int, b = int):
    c = a + b
    return c

a, b = 5, 13
d = addition(a, b)
print(d)

#Function to check whether a number is prime or not, Also, sorry if the code is a bit messy :P
def prime_number_checker(n):
    for i in range(2, n):
        if n % i == 0:
            a = n // i
            print(a, i, "Are the factors of the given number")
        else:
            print("The number is prime")
prime_number_checker(5)

#Defualt Argument, here it's not even necessary to add the value to y here as the defualt value is given, it can change if the value in y is specified
def random(x, y = 25):
    print(x)
    print(y)

random(1)
random(2, 50)

#Function to print out the name of a student
def name_of_student(firstname, lastname):
    print(firstname)
    print(lastname)
#Keyword Arguments
name_of_student(firstname= "Rahul", lastname = "Sharma")

#Nested function
def func():
    a = "Hello"
    def another_func(a):
        print(a)
    another_func(a)
func()