from abc import ABC, abstractmethod
# 组件接口会声明组合中简单和复杂对象的通用操作。

class Graphic(ABC):

    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def draw(self):
        pass

# 叶节点类代表组合的终端对象。叶节点对象中不能包含任何子对象。
class Dot(Graphic):

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print(f"在坐标位置({self.x},{self.y})处绘制一个点。")

class Circle(Dot):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        print(f"在坐标位置({self.x},{self.y})处绘制一个半径为 {self.radius} 的圆。")


# 组合类表示可能包含子项目的复杂组件。
class CompoundGraphic(Graphic):
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def move(self, x, y):
        for child in self.children:
            child.move(x, y)


    def draw(self):
        for child in self.children:
            child.draw()
