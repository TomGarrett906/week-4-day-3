class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return f'<Node: {self.value}>'

# node = Node('Monday')

# print(node)

# node2 = Node('Tuesday')

# node.right = node2

# print(node, node.right)

# node3 = Node('Wednesday')

# node2.right = node3

# print(node, node.right.right)

# node4 = Node('Thursday')

# node3.right = node4

# print(node, node.right.right.right)

# node5 = Node('Friday')

# node4.right = node5

# print(node, node.right.right.right.right)

# node6 = Node('Saturday')

# node5.right = node6

# print(node, node.right.right.right.right.right)

# node7 = Node('Sunday')

# node6.right = node7

# print(node, node.right.right.right.right.right.right)

# node7.right = node