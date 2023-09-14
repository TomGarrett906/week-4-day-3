from Node import Node                                     

class LinkedList:

  def __init__(self, head_value):
    self.head = Node(head_value)

  def __repr__(self):
    # output =  f'<LinkedList: '
    # for node in self:
    #   output += f'{node.value} -> '
    # return output.rstrip(' -> ')
    return f'<LinkedList: {" -> ".join(node.value for node in self)}>'
  
  def __iter__(self):
    current_node = self.head
    while current_node.right:
      yield current_node
      current_node = current_node.right
    yield current_node
  
  def append_node(self, value):
    current_node = self.head
    while current_node.right:
      current_node = current_node.right
    current_node.right = Node(value)

  def insert(self, neighbor, value):
    for node in self:
      if node.value == neighbor:
        next_node = node.right
        node.right = Node(value)
        node.right.right = next_node
        return
    print(f'{neighbor} not in LinkedList')

  def update_head(self, value):
    old_head = self.head
    self.head = Node(value)
    self.head.right = old_head
    # new_head = Node(value)
    # new_head.right = self.head
    # self.head = new_head

  def search(self, value):
    for node in self:
      if node.value == value:
        return node
    return False
  
  def get_tail(self):
    for node in self:
      pass
    return node

  def remove(self, value):
    if self.head.value == value:
        self.head = self.head.right
        return
    for node in self:
        if node.right and node.right.value == value:
            node.right = node.right.right
            return

linkedlist = LinkedList('Monday')
linkedlist.append_node('Tuesday')
linkedlist.append_node('Wednesday')
linkedlist.append_node('Friday')

# print(linkedlist.search('Monday'))
# print(linkedlist.search('Friday'))

# print(linkedlist.head.right)

linkedlist.insert('Wednesday', 'Thursday')
print(linkedlist)
# linkedlist.insert('Saturday', 'Sunday')

# linkedlist.update_head('Sunday')

# for node in linkedlist:
  # print(node)
  # print(linkedlist.search(node.value))

# print(linkedlist.get_tail())


'''

    First we import our node from our node file, then we define our class for our linked list.  Next out __init__ helps set up the initial value for our head node.  Then our __repr__ is there to set up our string return, and iterates through our list to print that out  in the format we instruct it to.  To even make out Linked List iterate we need to set up our __iter__ method, which we just give a simple instruction to keep looking to the right, or next node, to step through.  With our append method we keep stepping to the right until we get to the end of our list, then add that new node as the new tail.  For the insert method we tell it to interate through the list, right, until that node == to the neighbor variable we made, then it knows to place that node next to neigherber, to the right of it.  In the update_head method the reassign our current head (now the old head) to the next node to the right, making them == each other.  That makes room to define a new head == to what the previous head was.  The search method steps through until it finds a specific node amd return that value. The get_tail just iterates through to the end then returns the last node.  Last our remove method, checks to see, starting with the head and iterates till it finds a specific value, when that value is found, that specific node is updated and made == to the next node to the right of it. Becasue were dealing with nodes we dont need to shift the rest of the nodes over since thay all have their own address if you will.'''
