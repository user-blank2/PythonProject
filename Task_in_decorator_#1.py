def add_border(func):
    def add_new_design():
        print("***************")
        func()
        print("***************")
    return add_new_design



@add_border
def greeting():
    print("Hello There")


greeting()

