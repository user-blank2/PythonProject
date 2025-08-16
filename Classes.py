class student:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age


student1=student("deepak","M",19)
student2=student("Alice","F",20)

print(student1.name, student2.name,student1.age,student2.age)
