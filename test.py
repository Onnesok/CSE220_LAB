# # class Node:
# #     def __init__(self, data = None) -> None:
# #         self.data = data
# #         self.next = None

# # class lnkls:
# #     def __init__(self, elm) -> None:
# #         self.head = None

# #         self.elm = elm
# #         if type(self.elm) == Node:
# #             self.head = elm
# #         elif type(self.elm) == list:
# #             itr = Node(elm[0])
# #             self.head = itr
# #             nd = self.head

# #             for i in range(1, len(elm)):
# #                 itr = Node(elm[i])
# #                 nd.next = itr
# #                 nd = itr
# #     def cntNode(self):
# #         itr = self.head
# #         cnt = 0
# #         while itr != None:
# #             itr = itr.next
# #             cnt += 1
# #         self.cnt = cnt
# #         return cnt
# #     def prnt(self):
# #         itr = self.head

# #         while itr != None:
# #            if itr.next != None:
# #                print(itr.data, end = "-->")
# #            else:
# #                print(itr.data)

# #            itr = itr.next

# #     def ndat(self, elm):
# #         itr = self.head
# #         cnt = 0
# #         while itr != None:
# #             itr = itr.next
# #             cnt += 1
# #             if itr == elm:
# #                 print("Node at idx = ", cnt)
# #                 break
# #         if cnt > self.cnt-1:
# #             print(False)


# # elm = [1, 2, 50, 5, 10]

# # x = lnkls(elm)
# # print("count = ", x.cntNode())
# # x.prnt()
# # x.ndat(10)


# #####################################################


# # class stack:
# #     stack = []
# #     pointer = -1

# #     def push(self, element):
# #         self.stack = self.stack + [element]
# #         self.pointer += 1
# #     def peek(self):
# #         return self.stack[-1]
# #     def pop(self):
# #         val = self.stack[-1]
# #         self.stack = self.stack[:-1]
# #         self.pointer = -1
# #         return val

# # def checkbrackets(string):
# #     stk = stack()
# #     counter_stk = stack()
# #     leftbrc = ['(', '{', '[']
# #     rightbrc = [')', '}', ']']
# #     count = 1
# #     for i in string:
# #         if i in leftbrc:
# #             stk.push(i)
# #             counter_stk.push(count)
# #         if i in rightbrc:
# #             if stk.pointer == -1:
# #                 print("not correct")
# #                 print(f"error at character {count}. {i} not opened")
# #                 return
# #             else:
# #                 validity = False
# #                 n = stk.pop()
# #                 c=counter_stk.pop()
# #                 if n == "(" and i == ")":
# #                     validity = True
# #                 elif n == "{" and i == "}":
# #                     validity = True
# #                 elif n =="[" and i == "]":
# #                     validity = True
# #                 else:
# #                     validity = False
# #                 if validity == False:
# #                     print("expression not correct")
# #                     print(f"error at {c}. {n} not closed ")
# #         count += 1
# #     if stk.pointer == -1:
# #         print("correct")
# #         return
# #     else:
# #         print("not correct")

# #     while stk.pointer != -1:
# #         a = stk.pop
# #         print("error")
# #         print(count)
# #         stk.pointer = -1
# #     return

# # a = input()
# # checkbrackets(a)

# class stkk:
#     stk = [-1]*3
#     pointer = -1
#     def push(self, val):
#         if self.pointer == len(self.stk) - 1:
#             print("No space")
#         else:
#             self.pointer += 1
#             self.stk[self.pointer] = val
#     def pop(self):
#         if self.pointer == -1:
#             print("cant pop")
#         else:
#             val = self.stk[self.pointer]
#             self.stk[self.pointer] = -1
#             self.pointer -= 1
#             return val
#     def peek(self):
#         if self.pointer == -1:
#             print("no element")
#         else:
#             print(self.stk[self.pointer])

# # a = stack()
# # a.push(5)
# # a.push(6)
# # a.push(7)
# # print(a.pop())
# # a.pop()
# # a.peek()

# class stack:
#     stk = []*500
#     pointer = -1
#     def push(self, val):
#         self.stk = self.stk + [val]
#         self.pointer += 1
#     def pop(self):
#         val = self.stk[-1]
#         self.stk = self.stk[:-1]
#         self.pointer -= 1
#         return val
#     def peek(self):
#         return self.stack[-1]

# def checkbrc(string):
#     stk = stack()
#     counter_stk = stack()
#     leftBrackets = ["(", "{", "["]
#     rightBrackets = [")", "}", "]"]
#     count = 1
#     for i in string:
#         if i in leftBrackets:
#             stk.push(i)
#             counter_stk.push(count)
#         if i in rightBrackets:
#             if stk.pointer == -1:
#                 print("not correct")
#                 print(f"error at{count}. {i} not opened")
#             else:
#                 validity = False
#                 n = stk.pop()
#                 c=counter_stk.pop()
#                 if n=="(" and i==")":
#                     validity = True
#                 elif n=="{" and i == "}":
#                     validity = True
#                 elif n== "[" and i == "]":
#                     validity = True
#                 else:
#                     validity = False

#                 if validity == False:
#                     print("not correct")
#                     print(f"error at{count}. {i} not closed")
#         count += 1

#     if stk.pointer == -1:
#         print("correct")
#         return
#     else:
#         print("not correct")
#         while stk.pointer != -1:
#             a = stk.pop()
#             print(f"Error at #char. '{a}'- not closed.")
#             print(count)
#             stk.pointer -= 1
#         return

# # a = input()
# # checkbrc(a)


# class Node:
#     def __init__(self, data, n = None) -> None:
#         self.data = data
#         self.next = n

# class stc:
#     head = None
#     pointer = -1

#     def push(self, data):
#         if self.head == None:
#             self.head = Node(data, None)
#             self.pointer += 1
#         else:
#             n = Node(data, None)
#             n.next = self.head
#             self.head = n
#             self.pointer += 1
#     def peek(self):
#         return self.head.data
#     def pop(self):
#         temp = self.head
#         if temp.next != None:
#             self.head = self.head.next
#             temp.next = None
#             self.pointer -= 1
#             return temp.data
#         else:
#             print("cant pop")

# a = stc()
# a.push(5)
# a.push(10)
# a.push(15)
# print(a.peek())
# a.pop()
# a.pop()
# a.pop()
# a.pop()



###############################   Recurssion   ###############################

def fact(n):
    if n ==1:
        return 1
    else:
        return (n*fact(n-1))

def fibonacci(nth):
    if nth <= 1:
        return 1
    else:
        return fibonacci(nth - 1) + fibonacci(nth - 2)

# print(fibonacci(6))

#   0 1 1 2 3 5 8 13

def array(arr, size, idx = 0):
    if idx == size:
        return None
    else:
        print(arr[idx])
        return array(arr, size, idx = idx + 1)

x = [1,5,8,-5,2]
# print(array(x, len(x), 0))

def binary(n):
    a = n%2
    if n < 2:
        return str(a)
    else:
        n = n//2
        return binary(n) + str(a)

class Node:
    def __init__(self, data, n = None) -> None:
        self.data  = data
        self.n = n
class sm:
    tsum = None

class lnkls:
    def __init__(self) -> None:
        pass




class Node:
  def __init__(self, element, n):
    self.element = element
    self.next = n

class LinkedList:
  def __init__(self, a):
    self.head = None
    if type(a) == list:
      for i in range(0,len(a)):
        newNode = Node(a[i],None)
        if (self.head == None):
          self.head = newNode
          tail = newNode
        else:
          tail.next = newNode
          tail = newNode
    if type(a)==Node:
      self.head = a
      
  def hash(self):
    head = self.head
    t = head
    ls = []
    hs = ["-1"]*5
    while t != None:
        print(t.element)
        ls.append(t.element)
        t = t.next
    e=0
    size = 0
    nxt = 0
    summ = 0
    while size < 5:
        if hs[nxt] == "-1":
            summ = summ + ls[e]
            #print(summ)
            idx = (((3*summ)%5)+nxt)%5
            hs[idx] = ls[e]
            e += 1
            size += 1
            nxt = 0
        else:
            nxt += 1

    for i in range(len(hs)):
        print(f"idx {i} and val {hs[i]}")

  def reverseList(self,h):
    if h == None:
        return
    else:
        self.reverseList(h.next)
        print(h.element)

#3*(sum of digits)


a = [10,20,30,40, 50]
h1 = LinkedList(a)
h1.hash()
# h1.reverseList(h1.head)