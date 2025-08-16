class Iteratable:
    def __init__(self,st,stop,step):
        self.st=st
        self.stop=stop
        self.step=step

    def __iter__(self):
        return iterator(self.st,self.stop,self.step)


class iterator:
    def __init__(self,st,stop,step):
        self.st = st
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.st>self.stop:
            raise StopIteration

        val=self.st
        self.st+=1
        return val


range=Iteratable(1,5,1)

for i in range:
    print(f"LOOP {i}")

    for j in range:
        print(j)

