
class Binary_search:
    def __init__(self):
        self.arr = [1,2,3,4,5,6] #we asume it is sorted in this situation 

    def search(self, val):

        left = 0
        right = len(self.arr)
        middle = 0

        while (left < right):

            middle = int((left + right)/2)

            if (val > self.arr[middle]):
                left = middle+1
            else:
                right = middle

        if (self.arr[left] == val):
           return left
        else:
           return -1


array = Binary_search()

print(array.search(6))