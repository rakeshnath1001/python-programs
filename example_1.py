print("✅ File is running...")

class Student:
    #define constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    #define method
    def welcome(self):
        print("welcome student,", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("karan", 97)
s1.welcome()  #method calling
print(s1.get_marks())