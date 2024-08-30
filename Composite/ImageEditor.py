from Graphic import Dot, Circle, CompoundGraphic

class ImageEditor:

    def __init__(self):
        self.all = CompoundGraphic()

    def load(self):
        self.all.add(Dot(1,2))
        self.all.add(Circle(5, 3, 10))
    def group_selected(self, components):
        group = CompoundGraphic()
        for component in components:
            group.add(component)
            self.all.remove(component)
        self.all.add(group)
        self.all.draw()


if __name__ == '__main__':
    editor = ImageEditor()
    editor.load()
    editor.group_selected(editor.all.children)