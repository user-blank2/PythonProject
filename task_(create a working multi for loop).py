class r:
    def __init__(self,start,stop,step):
        self.start=start
        self.stop=stop
        self.step=step

    def __iter__(self):
        return iterator(self.start,self.stop,self.step)


class iterator:
    def __init__(self,start,stop,step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start>self.stop:
            raise StopIteration

        val=self.start
        self.start+=1
        return val



for i in r(1,5,1):
    print(f"THE loop st {i}")
    for j in r(2,8,1):
        print(j)

