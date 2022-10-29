class Student:

    School = "Aman's School of Knowledge"

    def __init__(self, m1, m2, m3):
        self.Marks_1 = m1
        self.Marks_2 = m2
        self.Marks_3 = m3

    def average(self):
        Average = self.Marks_1 + self.Marks_2 + self.Marks_3 / 3
        print(Average)

    #Method to get the marks, and It's soooo convinient to use functions :)                        
    def getting_the_marks(self):
        return self.Marks_1, self.Marks_2, self.Marks_3

#The Name of some of my friends lol!(Sorry!, I can't add all of 'em)
Mr_Johannes_Kepler = Student(78, 89, 85)
Mr_The_Big_Boi = Student(77, 80, 87)
Mr_President_Evil = Student(86, 93, 90)
Mr_Nitishk = Student(84, 90, 95)
Mr_Adi = Student(85, 87, 90)

print(Mr_Johannes_Kepler.average())
print(Mr_The_Big_Boi.average())
print(Mr_President_Evil.average())
print(Mr_Nitishk.average())
print(Mr_Adi.average())

print(Mr_Johannes_Kepler.getting_the_marks())