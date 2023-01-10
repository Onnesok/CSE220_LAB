######################################################  Task 1   ###########################################
###### Using array based stack
class Stack:
    stack = []
    pointer = -1
    
    def push(self, element):
        self.stack = self.stack + [element]
        self.pointer += 1
    def peek(self):
        return self.stack[-1]
    def pop(self):
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return val
        
def checkBrackets(string):
    stk = Stack()
    counter_stk = Stack()
    leftBrackets = ["(", "{", "["]
    rightBrackets = [")", "}", "]"]
    count = 1
    for i in string:
        if i in leftBrackets:
            stk.push(i)
            counter_stk.push(count)
        if i in rightBrackets:
            if stk.pointer == -1:
                print("This expression is NOT correct.")
                print(f"Error at character #{count}. '{i}'-not opened.")
                return
            else:
                validity = False
                n = stk.pop()
                c = counter_stk.pop()
                if n == "(" and i == ")":
                    validity  = True
                elif n == "{" and i == "}":
                    validity = True
                elif n == "[" and i == "]":
                    validity = True
                else:
                    validity = False
                    
                if validity != True:
                    print("This expression is not correct")
                    print(f"Error at character #{c}. '{n}'- not closed.")
                    return
        count += 1   
        
    if stk.pointer == -1:
        print("This expression is correct")
        return
    else:
        print("This expression is not correct")
        while stk.pointer != -1:
            a = stk.pop()
            print(f"Error at #char. '{a}'- not closed.")
            print(count)
            stk.pointer -= 1
        return
a = input()
checkBrackets(a)



############################################################ Task 2  #############################################
##### Using linked list based stack
class Node:
    def __init__(self, val, n):
        self.value = val
        self.next = n
        
class Stack:
    head = None
    pointer = -1
    
    def push(self, value):
        if self.head == None:
            self.head = Node(value, None)
            self.pointer += 1
        else:
            n = Node(value, None)
            n.next = self.head
            self.head = n
            self.pointer += 1 
            
    def peek(self):
        return (self.head.value)
    
    def pop(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.pointer -= 1
        return temp.value
   
        
def checkBrackets(string):
    stk = Stack()
    counter_stk = Stack()
    leftBrackets = ["(", "{", "["]
    rightBrackets = [")", "}", "]"]
    count = 1
    for i in string:
        if i in leftBrackets:
            stk.push(i)
            counter_stk.push(count)
        if i in rightBrackets:
            if stk.pointer == -1:
                print("This expression is NOT correct.")
                print(f"Error at character #{count}. '{i}'-not opened.")
                return
            else:
                validity = False
                n = stk.pop()
                c = counter_stk.pop()
                if n == "(" and i == ")":
                    validity  = True
                elif n == "{" and i == "}":
                    validity = True
                elif n == "[" and i == "]":
                    validity = True
                else:
                    validity = False
                    
                if validity != True:
                    print("This expression is NOT correct.")
                    print(f"Error at character #{c}. '{n}'-closed.")
                    return
        count += 1   
        
    if stk.pointer == -1:
        print("This expression is correct.")
        return
    else:
        print("This expression is NOT correct.")
        while stk.pointer != -1:
            a = stk.pop()
            print(f"Error at #char. '{a}'- not closed.")
            print(count)
            stk.pointer -= 1
        return
    
a = input()
checkBrackets(a)