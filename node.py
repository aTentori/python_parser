
class TreeNode:

    def __init__(self, sourceLine):
        self.data = ""
        self.sourceLine = sourceLine
        self.parent = None
        self.children = []

    def get_source_line(self):
        return self.sourceLine

    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def add_child(self, node):
        self.children.append(node)
