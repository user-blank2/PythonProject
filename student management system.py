class Student:
    count = 0  # Class variable

    def __init__(self, name, age):   # Instance method
        self.name = name
        self.age = age
        Student.count += 1

    @staticmethod
    def validity(name, age):
        return f"{name} is accepted" if age >= 5 else f"{name} is rejected"

    @classmethod
    def pnt_count(cls):
        return f"The total number of students: {cls.count}"

    def display_info(self):  # Instance method
        return f"Name: {self.name}, Age: {self.age}"


# Creating objects (instances)
student1 = Student("Alice", 5)
student2 = Student("Deepak", 6)

# Using instance methods
print(student1.display_info())
print(student2.display_info())

# Using class method
print(Student.pnt_count())      # Option 1
print(student1.pnt_count())     # Option 2 (both work)

# Using static method
print(Student.validity("Alice", 5))
print(Student.validity("Deepak", 6))









"""
class Student:
    count=0  #class variable




    def __init__(self,name,age):   #instance variable
        self.name=name
        self.age=age
        Student.count+=1


    @staticmethod
    def validity(name , age):
        return f"{name} is accepted" if age<=5 else f"{name} is rejected"



    @classmethod
    def pnt_count(cls):
        return f"The total no.of Students : {Student.count}"




student1 = Student("Alice",5)
student2 = Student("Deepak",6)

print(Student.pnt_count())
print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)


print(Student.validity("Alice",5))

Student_validity =Student.validity("Deepak",6)
print(Student_validity)

"""


