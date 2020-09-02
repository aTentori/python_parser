from node import TreeNode


def traverse(node):
    if node:
        print(node.sourceLine)
    if node and len(node.children) > 0:
        for child in root.children:
            traverse(child)

# text being used
file = open("output.txt", "r")

lines = file.readlines()

root = None  # root node for parse tree
index = 0
cursor = None
in_line = False
line_count = 0
child_node = None


for line in lines:  # Build parse tree

    if line.__contains__("{"):
        in_line = True

    if line.__contains__("}"):
        in_line = False
        line_count += 1

    if line.__contains__("function"):
        root = TreeNode(line)

    if root and in_line and line_count < 0:
        root.sourceLine += line  # append to root node if there is an identifier

    # This is where we add the children of the root node
    if in_line and line.__contains__("ID") and line_count > 0 and not child_node:
        child_node = TreeNode(line)

    elif child_node and in_line:
        child_node.sourceLine += line

    if not in_line and root and line_count > 0:
        root.add_child(child_node)


traverse(root)
