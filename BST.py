from Node import Node

class BinarySearchTree:

  def __init__(self, root_value):
    self.root = Node(root_value)

  def __repr__(self):
    return f'<BST: {self.root}'
  
  def add_node(self, value, current_node=None):
    if not current_node:
      current_node = self.root
    if value > current_node.value:
      if current_node.right:
        self.add_node(value, current_node.right)
      else:
        current_node.right = Node(value)
    elif value < current_node.value:
      if current_node.left:
        self.add_node(value, current_node.left)
      else:
        current_node.left = Node(value)

  def search(self, value, current_node=None):
    if not current_node:
      current_node = self.root
    if value > current_node.value:
      if current_node.right:
        return self.search(value, current_node.right)
    elif value < current_node.value:
      if current_node.left:
        return self.search(value, current_node.left)
    else:
      return current_node
    print(f'Node: {value} not found')
    return False

  def get_min(self):
    current_node = self.root
    while current_node.left:
      current_node = current_node.left
    return current_node
  
  def get_max(self, current_node = None):
    if not current_node:
      current_node = self.root
    if current_node.right:
      return self.get_max(current_node.right)
    return current_node
  
  def print_sorted(self, current_node = None):
    if not current_node: 
      current_node = self.root
    if current_node.left:
      self.print_sorted(current_node.left)
    print(current_node.value)
    if current_node.right:
      self.print_sorted(current_node.right)

  def print_sorted_reverse(self, current_node = None):
    if not current_node: 
      current_node = self.root
    if current_node.right:
      self.print_sorted_reverse(current_node.right)
    print(current_node.value)
    if current_node.left:
      self.print_sorted_reverse(current_node.left)
      

bst = BinarySearchTree(100)
bst.add_node(125)
bst.add_node(130)
bst.add_node(115)
bst.add_node(50)
bst.add_node(25)
bst.add_node(75)
bst.add_node(110)
bst.add_node(120)
# print(bst.search(75), 'test search')

print(bst.get_min())
print(bst.get_max())


bst.print_sorted_reverse()
bst.print_sorted()

# print(bst.root.right.right)
# print(bst.root.right.left)
# print(bst.root.left.right)

'''
    For our Binary Search Tree, instead of iterating to the right, we iterate by either forking left or right, comparing less or more. The same pretty much goes for out import, class, __init__, and __repr__ .  Except this time for BST we consider the head as our root.  We don't need the __iter__ method because we set up an algorithm the handles tha for up, by simplly moving to the right if the value is greater, or to the left if the value is smaller.  Instead of iterating thorugh a list we a traversing through a tree.  For our add_node we check where to add to our tree by starting with our current node, weather if it is ==, or is lesser, or is greater.  We check if not first becuase we cannot have duplicates in out BST. We traverse through our tree until we get to no more nodes to compare if it's less than or more than, then that node has found its spot.  For our search we follow the same process until we reach the node that IS our current node, because we cannot have duplicates it won't add and we can return that value.  If that value is not in our tree it will traverse through until there are more forks to compare and we can return false or none.  Get min we simply look all the wway to the left of the tree and return that node.  Get max we just keep looking right till we can't any more, then return that node. Next is our in order Print_sorted method. We start checking current node with the root, then the next node if it's less or more to sort it's place in the tree. Usually finding its place in between the traversal from going left or right, less or more.  Finally for the print_sorted_reverse method we set it to take the same instructions as our print_sorted, exceot its flipped and we step right where we used to step left, and step left where we used to step right.  I think it important for me to state that actually we are checking if the current is or in not the node we are comparing it with.
'''