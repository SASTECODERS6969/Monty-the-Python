#A Constructor Is something which determines the amount of memory which should be allocated to an Object.
#The word 'Self' acts as a pointer, which points towards a particular thing.
class BioMetric_Information:
    def __init__(self, name, age, height, gender):
        self.Name = name
        self.Age = age
        self.Height = height
        self.Gender = gender

    def data(self):
        #Tried to make this dictionary global, Is there any way to do so?
        Data = {
            "Name" : self.Name,
            "Age" : self.Age,
            "Height" : self.Height,
            "Gender" : self.Gender,
        }
        print(Data)

    def update_name(self, name):
        self.Name = name
    
    def compare(self, other):
        if self.Name == other.Name : print("The Names are same")
        else:
            print("Names are different")

        if self.Age == other.Age : print("Ages are same")
        else:
            print("Ages are different")
        
        if self.Height == other.Height : print("Height is same")
        else:
            print("Height is different")
        
        if self.Gender == other.Gender : print("The Gender is the same")
        else:
            print("The gender is different")
        
        

Object_1 = BioMetric_Information("Aman", 15, 165, "Male")
Object_1.data()

#Attributes of the Object can be changed and modified in the following manner.
Object_1.Name = "Rita"
Object_1.Gender = "Female"
Object_1.data()

#Or we could just make up a function to do it for us

Object_1.update_name("McGonagall")
Object_1.data()

Object_2 = BioMetric_Information("Luna", 17, 160, "Female")

Object_1.compare(Object_2) #A Function to compare the 2 objects
