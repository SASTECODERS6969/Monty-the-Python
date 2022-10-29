class A:
    
    def method_one(self):
        print("Method 1 is working")
    
    def method_two(self):
        print("Method 2 is working")

a = A()
a.method_two()
a.method_one()

class B(A): #Here, Class B Inherits all the methods which are present in class A

    def method_three(self):
        print("Method 3 is Working")
    
    def method_four(self):
        print("Method 4 is working")
    
b = B()
#All the methods available in class A Is also available and accessible for objects of class B, because Class B inherits the methods present in Class A
b.method_one()
b.method_two()
b.method_three()
b.method_four()
