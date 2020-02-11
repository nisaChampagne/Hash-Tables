class DynamicArray:
    def __init_(self, capacity=8): # 32 bytes?
        self.count = 0  # how much is currently used  / in use
        self.capacity = capacity # how much is currently allocated / total space
        self.storage = [None] * self.capacity

    def __str__(self):

        return f"Capacity: {self.capacity}  Storage: {self.storage}"

    # need to know where and what we are putting in array
    def insert(self, index, value): # to specific index anywhere
        if self.count == self.capacity:
            self.resize()
            return

        # shift everything to the right
        ############## start at end, stop at index and go -1 each time
        for i in range(self.count, index, -1):

            ###look to the left, copy it over, until we get to the index, then we can insert our value
            self.storage[i] = self.storage[i  - 1]

        # insert value
        self.storage[index] = value
        self.count += 1

    def append(self,value): # adds to end
        if self.count == self.capacity:
            self.resize()
            return

        self.insert(self.count, value)

    def resize(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage # would make it empty and erase everything
        ## ^ changes the pointer 
        ## deallocates the old one that we arent using anymore
        ## old storage becomes garbage
        

    def replace(self, index, value):
        self.storage[index] = value

    def add_to_front(self, value):
        self.insert(0, value)
        

'''

python list is a dynamic array

'''