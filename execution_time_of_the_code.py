import time

def timer(func):                                                       #func=add
    def cal_time(*args,**kwargs):                                      #create new func to add to the base func (this gets all the arguments from base function here 1,2)
        st=time.time()
        res = func(*args,**kwargs)                                     #calls the add func and store their result in res
        end=time.time()
        tot_time=end-st
        print(f"The code execution time : {tot_time:.05f}")
        return res


    return cal_time #add=cal_time

@timer
def add(a,b):
   return a+b

result=add(1,2)
print(result)
