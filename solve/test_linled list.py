class Node:
    def __init__(self, e, n = None) -> None:
        self.element = e
        self.next = n
        

# class lnk:
#     def __init__(self, a) -> None:
#         self.head  = None
#         self.a = a
        
#         if type(a) == list:
#             self.head = Node(a[0], None)
#             h = self.head
            
#             for i in range(1, len(a)):
#                 t = Node(a[i], None)
#                 h.next = t
#                 h=t
#         elif type(a) == Node:
#             self.head = a
            
#     def pr(self):
#         h = self.head
        
#         while h.next != None:
#             print(h.element)
#             h = h.next
#         print(h.element)


# x = [1,3,8,9,12]
# a = lnk(x)
# a.pr()


class lnk:
        def __init__(self, a) -> None:
             self.a = a
             self.head = None
             
             if type(a) == list:
                 if self.head == None:
                     self.head = Node(a[0], None)
                     h = self.head
                 for i in range(1, len(a)):
                    t = Node(a[i], None)
                    h.next = t
                    h = t
             elif type(a) == Node:
                 self.head = a
                 
        def pr(self):
            h = self.head
            while h != None:
                if h != None:
                    print(h.element)
                h = h.next
            #print(h.element)
            
        def dl(self, idx):
            h = self.head
            if idx < 0 or idx >= len(self.a):
                print(None)
            elif idx == 0:
                h = h.next
                self.head = h
            elif idx == len(self.a) - 1:
                while h.next != None:
                    prev = h
                    h = h.next
                prev.next = None
            else:
                i = 0
                while i != idx:
                    prev = h
                    h = h.next
                    i+= 1
                prev.next = h.next
                prev = h.next  
                
        def insrt(self, idx, elem):
            h = self.head
            if idx < 0 or idx >= len(self.a):
                print("Not possible")
            elif idx == 0:
                temp = self.head
                new = Node(elem, None)
                self.head = new
                h = self.head
                h.next = temp
            else:
                i = 0
                while i != idx:
                    prev = h
                    h = h.next
                    i+=1
                prev.next = Node(elem, None)
                prev = prev.next
                prev.next = h
                      
        

x = [1,3,8,9,12]
a = lnk(x)
a.pr()
idx = 4
a.dl(idx)
print("delted")
a.pr()
print("insrt")
a.insrt(3, -1)
a.pr()

# Test