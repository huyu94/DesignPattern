from TreeFactory import TreeFactory
from Tree import Tree
class Forest:
    def __init__(self):
        self.trees = []

    def plantTree(self, x, y, name, color, texture):
        type = TreeFactory.getTreeType(name, color, texture)
        tree = Tree(x,y,type)
        self.trees.append(tree)

    def draw(self,canvas):
        for tree in self.trees:
            tree.draw(canvas)