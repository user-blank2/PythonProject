class common:
    def __init__(self,section,is_alive):
        self.section=section
        self.is_alive=is_alive

class class1(common):
    def __init__(self,section,is_alive,gender):
            super().__init__(section,is_alive)
            self.gender=gender

class class2(common):
    def __init__(self,section,is_alive,toppers):
        super().__init__(section,is_alive)
        self.toppers=toppers

list0=class1("A",True,"M")


list2=class2("B",True,32)


print(list0.section,list0.is_alive,list0.gender)
print(list2.section,list2.is_alive,list2.toppers)