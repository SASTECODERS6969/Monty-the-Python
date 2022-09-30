#WAP TO FIND THE BIGGEST NUMBER IN BETWEEN 2 NUMBERS
def comparision(a, b):
    if a > b:
        print(a, "Is greater")
    elif b > a:
        print(b, "Is greater")
    elif a == b:
        print("Both values are equal")

comparision(23, 32)