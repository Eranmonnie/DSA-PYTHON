class linear_search:
    def __init__(self, arr) :
        self.arr = arr #so i wont populate the array 

    def add(self,val):
        self.arr.append(val)
        return 0

    def search(self,val):
        x = 0
        while  x < len(self.arr):
            if self.arr[x] == val:
                return x
            else:
                x += 1
        return -1
lin = linear_search([1,2,3,4,5])
print(lin.search(5))