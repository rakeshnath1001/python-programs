# create student class that takes name & marks of 3 subjects as arguments in constructor. Then create method to print the average.

class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks= marks

    #creating method
    def get_avg(self):
       avg = sum(self.marks)/ len(self.marks)
       print("hi",self.name, "your avg score is:",avg)

        
s1=Student("rakesh", [97,98,99])
s1.get_avg()

        
