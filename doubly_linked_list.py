class node:
    def __init__(self,data=None):
        self.first = None
        self.data = data
        self.next = None
#we will never inretact with this calss outside the linked list class 

class double_linked_list:
    def __init__(self):
        self.head = None

    #appends to the end of the linked list
    def append(self, data):
        
        

        if self.head == None:
            new_node = node(data)
            self.head = new_node
            new_node.first = None
            
        else:
            cur = self.head
            new_node = node(data)
            while cur.next !=None:
                cur = cur.next
            cur.next = new_node
            new_node.first = cur
            new_node.next = None
            
    #get lenght of linked list 
    def length(self):
        cur = self.head
        append = 0
        while cur.next != None:
            cur = cur.next
            append+=1
        return append
    
    #displays al the data in linked list
    def display(self):
        elements = []
        cur = self.head
        while cur:
            elements.append(cur.data)
            cur = cur.next
        return elements

    # finds list with index
    def getIndex(self, val):
        valindex = 0
        cur = self.head
        if val>= self.length():
            print ("Error : 'getindex' Index out of range") 
            return
         
        while True:
            if valindex == val:
                return cur.data
            cur = cur.next
            valindex +=1

    def remove(self, val):
        eraseindex = 0
        cur = self.head
        if val>= self.length():
            print ("Error 'erase' index out of range")
            return 
        while True:
            #store last node 
            curnode = cur
            #traverse to the node to delete 
            nextnode = cur.next

            if eraseindex == val:

                #if deleting last node 
                if curnode.next == None:
                    curnode.first.next = None
                    return 1
                
                #if we are deleting the first node 
                if curnode.first == None:
                    self.head = nextnode
                    return 1
                
                #that previous nodes end will now be equal to the next of the curr.next initiated which is the next object
                curnode.first.next = nextnode
                nextnode.first = curnode
            
            eraseindex+=1

     #add an append at index function    
      

list = double_linked_list()
list.append('feranmi')
list.append('ajkjlnklnala')
list.append('ajala')
list.append('ajala')
list.append('ajala')
list.append('eranmonnie')
print(list.length())
print(list.display())
print(list.getIndex(1))
list.remove(1)
print(list.display())

#  remove index one step out of place 





    
