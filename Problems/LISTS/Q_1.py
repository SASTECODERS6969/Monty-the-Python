#Problems are on https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/?ref=lbp
#WAP To interchange the first and last elements of a list

def swapping(list):
    a = list[0] 
    b = len(list)
    c = list[b - 1]
    d = a
    list[0] = list[b - 1]
    list[b - 1] = a
    print(list)

swapping([1, 2, 3, 4, 5, 6])
#LESSON LEARNT: Before applying the code to a particular solution, it's better to project the code inside a function.
#LESSON LEARNT: In the code, I was first swapping the variables all the time, but I actually had to swap the Index values :P


