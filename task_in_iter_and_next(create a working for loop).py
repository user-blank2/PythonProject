class ForLoop:
    def __init__(self,start,stop,step):
        self.start=start
        self.stop=stop
        self.step=step
        self.it=0

    def __iter__(self):
            self.it=self.start
            return self

    def __next__(self):
        if self.step>0:
            if self.it>self.stop:
                raise StopIteration

            val=self.it
            self.it+=self.step
            return val

        else:
            if self.it<=self.stop:
                raise StopIteration

            val=self.it
            self.it+=self.step
            return val


For=ForLoop(10,1,-1)

for i in For:
    print(i)




