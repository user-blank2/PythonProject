from abc import ABC ,abstractmethod

class shape(ABC):

    @abstractmethod

    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.radius**2

class triangle(shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side ** 2
shapes=circle(2)

shapes2=triangle(8)
print(shapes2.side)
print(shapes.area())


