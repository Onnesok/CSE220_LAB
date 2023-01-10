def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

#print(factorial(3))

def fbnc(n):
    if n <= 1:
        return 1
    else:
        return fbnc(n-1) + fbnc(n-2)

#print(fbnc(5))

def arr(ar, size, i = 0):
    if i == size-1:
        return ar[i]
    while i < size:
        print(ar[i])
        return arr(ar, size, i =i + 1)

#print(arr([1,2,3,8,9,5], 6, 0))

def pw(b, p):
    if p == 1:
        return b
    else:
        return b * pw(b, p = p-1)
    
#print(pw(3,3))

def bn(decimal):
    if decimal < 2:
        return str(decimal % 2)
    else:
        return  str(bn(decimal = decimal // 2)) + str(decimal % 2)

#print(bn(3))

import math

class tsum:
    summ = None

class Node:
    def __init__(self, e, n = None) -> None:
        self.element = e
        self.next = n

def push(head, data):
    if not head:
        return Node(data)
    
    new = Node(data)
    new.next = head
    head = new
    
    return head

def sumofNode(head, s):
    if not head:
        return
    
    sumofNode(head.next, s)
    s.tsum += head.element
    
def sumof(head):
    s = tsum()
    s.tsum = 0
    
    sumofNode(head, s)
    return s.tsum

# head = None

# head = push(head, 1)
# head = push(head, 2)
# head = push(head, 3)
# head = push(head, 5)
# head = push(head, 4)
# print("Sum of Nodes = ", sumof(head))


class lnk:
    def __init__(self, a) -> None:
        self.head = None
        if type(a) == list:
            if self.head == None:
                self.head = Node(a[0], None)
                h = self.head
            
            for i in range(1, len(a)):
                temp = Node(a[i], None)
                h.next = temp
                h = temp
        elif type(a) == Node:
            self.head =a
            
    def rev(self, head):
        if head == None:
            return
        self.rev(head.next)
        print(head.element)
            
# a = [10,20,30,40]
# h1 = lnk(a)
# (h1.rev(h1.head))
