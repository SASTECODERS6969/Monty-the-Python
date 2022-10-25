#Creating a class Laptop
class Laptop:
    #This is the Init function, which is A function which is automatically executed when the Object is formed
    def __init__(self, RAM, CPU, BL):
        self.RAM = RAM
        self.CPU = CPU
        self.BL = BL
   #Method to print the configuration of the Laptop
    def configuration(self):
        Configuration = {
            "RAM" : self.RAM,
            "CPU" : self.CPU,
            "Battery Life (In Hours)" : self.BL
        }
        print(Configuration)

#Object Creation
HP = Laptop(16, 'i9', 30) #It's necessary to add the required data in while creating the object
#Calling the function which the Object has
HP.configuration()


        
        


