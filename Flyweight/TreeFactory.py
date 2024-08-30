from Tree import TreeType
class TreeFactory():
    tree_types = {}
    @staticmethod
    def getTreeType(name, color, texture):
        type = TreeFactory.tree_types.get(name, None)
        if type is None:
            type = TreeType(name, color, texture)
            TreeFactory.tree_types[name] = type
        return type


