class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = node()

    def add (self ,data):
       
        new_node = node(data)
        # cheak if self.head data is empty if so make its data equal to new node 
        if self.head.data == None:
            self.head.data = new_node

        #if not empty have a copy of head make head.data equal to new_node and make the new head.data.next equal to the copy of the previous head.data  
        else:
            cur = self.head 
            self.head.data = new_node
            new_node.next = cur.data 

        # next check if head.next is filled if so return
        if self.head.next:
            return 1
        
        # else if empty fill head.next with new_node from the first instance of the add function  seeing a this will only happen once in the add function
        else:
            self.head.next = new_node
            return 1


#     def pop(self):
#         if self.head.next:
#             #get next node then make that the first node 
#             self.head = self.head.next 
#             return 1
#         self.head = node()

#     def length(self):
#         cur = self.head
#         append = 0
#         while cur:
#             append+=1
#             cur = cur.next
#         return append

#     def display(self):
#         elements = []
#         cur = self.head
#         while cur:
#             elements.append(cur.data)
#             cur = cur.next
#         return elements
    
#     def index(self, data):
#         index = 0
#         cur = self.head
#         if data > self.length():
#             print("Error 'index' out of range at ",data )

#         while True:
#             if data == index:
#                 return cur.data
#             cur = cur.next
#             index +=1 


# stack = Stack()
# stack.add(1)
# stack.add(2)
# stack.add(3)
# print(stack.display())
# stack.pop()
# print(stack.display())
# print(stack.length())
# print(stack.index(0))


# #add pop length display index all work