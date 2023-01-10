class Node:
  def __init__(self, e, n, p):
    self.element = e
    self.next = n
    self.prev = p


#####################################################################################
##########################  2nd class    ############################################
#####################################################################################

class DoublyList:
  
  def __init__(self, a):
  #  Design the constructor based on data type of a. If 'a' is built in python list then
  #  Creates a linked list using the values from the given array.
    self.head = None
    # To Do
    node = None
    self.tail = None

    for i in range(len(a)):
      new_node = Node(a[i], None, None)

      if self.head == None:
       self.head = new_node
       node = new_node
      else:
        node.next = new_node
        new_node.prev = node
        node = node.next

      self.tail = new_node 


  
  # Counts the number of Nodes in the list
  def countNode(self):
    # To Do
    node = self.head
    cnt = 0

    while node != None:
      cnt+= 1
      node = node.next

    return cnt  
  # prints the elements in the list
  def forwardprint(self):
    # To Do
    node = self.head

    while node != None:
      if node.next == None:
        print(node.element)
      else:
        print(node.element, end=", ")

      node = node.next

  # prints the elements in the list backward
  def backwardprint(self):
    # To Do
    node = self.tail

    while node != None:
      if node.prev == None:
        print(node.element)
      else:
        print(node.element, end = ", ")

      node = node.prev

  # returns the reference of the at the given index. For invalid index return None.
  def nodeAt(self, idx):
    # To Do
    node = self.head

    for i in range(idx):
      node = node.next
    return node
  
  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    # To Do
    node = self.head
    cnt = 0

    while node.element != elem:
      cnt += 1
      if node.next == None:
        cnt = -1
        return cnt
      node = node.next

    return cnt

  # inserts containing the given element at the given index Check validity of index. 
  def insert(self, elem, idx):
    # To Do
    if idx < 0 or idx > self.countNode():
      return None
    
    new_node = Node(elem, None, None)
    if idx == 0:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    
    elif idx == self.countNode():
      prev = self.nodeAt(idx-1)
      new_node.prev = prev
      prev.next = new_node
      self.tail = new_node
    else:
      prev = self.nodeAt(idx-1)
      next_node = self.nodeAt(idx)
      new_node.next = next_node
      new_node.prev = prev
      prev.next = new_node
      next_node.prev = new_node


  # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
  def remove(self, idx):
    # To Do
    if idx < 0 or idx > self.countNode():
      return None
    
    elif idx == 0:
      new_node = self.head
      next_node = new_node.next
      self.head = next_node
      next_node.prev = None
      return str(new_node.element)

    elif idx == self.countNode()-1:
      new_node = self.nodeAt(idx)
      prev = new_node.prev
      prev.next = None
      self.tail = prev
      new_node.prev = None

      return str(new_node.element)

    else:
      new_node = self.nodeAt(idx)
      next_node =  new_node.next
      prev = new_node.prev
      prev.next = next_node 
      next_node.prev = prev
      new_node.prev = None
      new_node.next = None
      return str(new_node.element)


#########################################################################################################
#####################################  Driver code  #####################################################
#########################################################################################################

print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array

h1.forwardprint() # This should print: 10,20,30,40. 
h1.backwardprint() # This should print: 40,30,20,10. 
print(h1.countNode()) # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that 
#doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.  

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40. 
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.  
h2.backwardprint() # This should print: 40,30,95,20,10,85.  

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75. 
h2.backwardprint() # This should print: 75,40,30,95,20,10,85. 


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.  

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.  
h3.backwardprint() # This should print: 70,60,50,40,30,20.  
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.  
h3.backwardprint() # This should print: 70,60,40,30,20.  
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60. 
h3.backwardprint() # This should print: 60,40,30,20.