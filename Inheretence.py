class road:
    def clear(self):
        print("The road is clear")

    def traffic(self):
        print("The road is traffic")



class car(road):
    def accelerate(self):
        print("The car is going fast ")

    def brake(self):
        print("The car is stoping")

class fast(car):
    pass

class slow(car):
    pass


BMW=fast()
audi=slow()


BMW.traffic()
BMW.brake()

audi.clear()
audi.accelerate()