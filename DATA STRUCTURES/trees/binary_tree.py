class binaryTree:
    def __init__(self, data):
        self.left = None
        self.right= None
        self.data = data

    def insert(self, data):

        if (self.data):
            if data < self.data:
                if self.left == None:
                    self.left = binaryTree(data)
                else:
                    self.left.insert(data)
            elif(data > self.data):
                if (self.right == None):
                    self.right = binaryTree(data)
                else:
                    self.right.insert(data)
        
        else:
            self.data = data 
            
     
    def printTree(self):
        if (self.left):
            self.left.printTree()

        print(self.data)

        if (self.right):
            self.right.printTree()



x = binaryTree(19)
x.insert(1)
x.insert(11)
x.insert(20)
x.insert(100)
x.printTree()