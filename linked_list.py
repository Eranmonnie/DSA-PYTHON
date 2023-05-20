class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
#we will never inretact with this calss outside the linked list class 

class linked_list:
    def __init__(self):
        self.head = node()

    #appends to the end of the linked list
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next !=None:
            cur = cur.next
        cur.next = new_node

    #gat lenght of linked list 
    def length(self):
        cur = self.head
        append = 0
        while cur.next != None:
            append+=1
            cur = cur.next
        return append
    
    #displays al the data in linked list
    def display(self):
        elements = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)
        return elements

    # finds list with index
    def getIndex(self, val):
        valindex = 0
        cur = self.head
        if val>= self.length():
            print ("Error : 'getindex' Index out of range") 
            return
         
        while True:
            cur = cur.next
            if valindex == val:
                return cur.data
            valindex +=1

    def remove(self, val):
        eraseindex = 0
        cur = self.head
        if val>= self.length():
            print ("Error 'erase' index out of range")
            return 1
        
        while True:
            #store last node 
            lastnode = cur
            #traverse to the node to delete 
            cur = cur.next
            
            #if we are deleting the first node s
            if lastnode.next == None:
                lastnode.next = cur
                return 1
            
            if eraseindex == val:
                #if youre trying to remove the node at the end which has a next of none 
                if cur.next == None:
                     lastnode.next = None
                     return 1
                
                #that previous nodes end will now be equal to the next of the curr.next initiated which is the next object
                lastnode.next = cur.next
                return 1  
            
            eraseindex+=1

     #add an append at index function    
      

list = linked_list()
list.append('feranmi')
list.append('ajala')
list.append('ayo')
list.append(';dj')
list.append('ajkwenfklala')
print(list.length())
print(list.display())
list.remove(2)
print(list.display())


#data in a linked list can be acdessed via recursion also  

    
