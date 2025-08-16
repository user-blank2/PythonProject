class List:
    def __init__(self,lst,start_pos):
        print("This is a indexing class")
        self.lst=lst
        self.start_index=0
        self.start_pos=start_pos

    def __iter__(self):
        self.start_index=self.start_pos
        return self


    def __next__(self):
        if self.start_index >= len(self.lst):
            raise StopIteration

        val=self.lst[self.start_index]
        self.start_index+=1
        return val


Lists=List(["apple","banana","orange","mango"],1)


for i in Lists:
    print(i)

    for j in Lists:
        print(j)