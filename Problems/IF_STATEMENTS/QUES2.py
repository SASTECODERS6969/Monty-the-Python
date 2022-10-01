#WAP TO COMPARE 3 NUMBERS
def comparision(a, b, c):
    if (a > b) & (a > c):
        print(a, "Is greater")
    elif (b > a) & (b > c):
        print(b, "Is greater")
    elif (c > a) & (c > b):
        print(c, "Is greater")

print(comparision(23, 12, 45))