

class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        print(f"在画布 {canvas} 上绘制名称为 {self.name}、颜色为 {self.color} 和纹理为 {self.texture} 的树，在坐标({x},{y})处。")


class Tree:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def draw(self, canvas):
        self.type.draw(canvas, self.x, self.y)

