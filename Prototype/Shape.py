from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def clone(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def clone(self):
        return Rectangle(self.x, self.y, self.width, self.height)

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def clone(self):
        return Circle(self.x, self.y, self.radius)

class Application():
    def __init__(self):
        self.shapes = []
        circle = Circle(10, 10, 20)
        self.shapes.append(circle)

        another_circle = circle.clone()
        self.shapes.append(another_circle)

        rec = Rectangle(10, 10, 20, 20)
        self.shapes.append(rec)

    def businessLogic(self):
        shapesCopy = list()
        for shape in self.shapes:
            shapesCopy.append(shape.clone())

    
