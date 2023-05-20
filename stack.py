class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = node()

    def add (self ,data):
       
        new_node = node(data)
        if self.head.data == None:
            self.head = new_node

        else:
            cur = self.head 
            self.head = new_node
            new_node.next = cur 

        return 1

    def pop(self):
        if self.head.next:
            #get next node then make that the first node 
            self.head = self.head.next 
            return 1
        self.head = node()

    def length(self):
        cur = self.head
        append = 0
        while cur:
            append+=1
            cur = cur.next
        return append

    def display(self):
        elements = []
        cur = self.head
        while cur:
            elements.append(cur.data)
            cur = cur.next
        return elements
    
    def index(self, data):
        index = 0
        cur = self.head
        if data > self.length():
            print("Error 'index' out of range at ",data )

        while True:
            if data == index:
                return cur.data
            cur = cur.next
            index +=1 


stack = Stack()
stack.add(1)
stack.add(2)
stack.add(3)
print(stack.display())
stack.pop()
print(stack.display())
print(stack.length())
print(stack.index(0))


#add pop length display  