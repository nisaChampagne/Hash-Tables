# '''
# Linked List hash table key/value pair
# '''

# SLL  value --pointer-> value --pointer->
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.ref = None 

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key): # private method, shouldnt use outside of class
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key) # hashes whatever out key is


    # def _hash_djb2(self, key):
    #     '''
    #     Hash an arbitrary key using DJB2 hash

    #     OPTIONAL STRETCH: Research and implement DJB2
    #     '''
    #     pass


    def _hash_mod(self, key): # private method, shouldnt use outside of class
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity  # generates index for us

        '''
        we use this because its easier to maintain/ change this way

        if we use the built in hash() we would have to change every line its used in so
        its better to have it in one place and change just that place if its needed

        '''


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        ##### V.1
        # print('Key to insert: ', key)  # returns keys in terminal yay!
        # print('Value to insert: ', value) # returns values in terminal yay!

        # hash_index = self._hash_mod(key)
        # print('index: ', hash_index) # current index

        # if key not in self.storage:
        #     self.storage.append(hash_index)
        #     self.storage[hash_index] = value


        ######## V.2 #######
    
        # find an index using the key
        hash_index = self._hash_mod(key)

        # create a new linked list node using key and value
        new_node = LinkedPair(key, value)

        # traverse the linked list in storage at generated hash_index
        current = self.storage[hash_index]
        # if no list exists, new node becomes the head
        if current is None:
            self.storage[hash_index] = new_node
            return
        prev = None
        while current is not None:
            # if key in list matches given key, overwrite value
            if current.key == key:
                current.value = value
                return
            prev = current
            current = current.ref
        # if reach end of list, append new node
        prev.ref = new_node
        return
        

       

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        ##### V.1
        # hash_index = self._hash_mod(key)
        # if self.storage[hash_index].key:
        #     self.storage[hash_index] = None
        # else: 
        #     print(f"{key} not found")

        ##### V.2

        # find the index using the given key
        hash_index = self._hash_mod(key)

        # traverse the linked list in storage at that hash_index
        previous = None
        current = self.storage[hash_index]
        while current is not None:
            # if key is found, remove node from list
            if current.key == key:
                # if node is head of list, point storage to next value
                if previous is None:
                    self.storage[hash_index] = current.ref
                # otherwise, connect previous node to next node
                else:
                    previous.ref = current.ref
                return
            previous = current
            current = current.ref

        # if key not found, print a warning
        print("Error: key not found")
        return

       



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

    ##### V.1
        # hash_index = self._hash_mod(key)
        # if self.storage[hash_index] is not None:
        #     print(f"key: {key}, value: {self.storage[hash_index]} GOT IT!")
        #     return self.storage[hash_index]
        # else:
        #     print(f"{key} was not found!")
        #     return None

    ##### V.2

        # find the index using the given key
        hash_index = self._hash_mod(key)

        # traverse the linked list at that hash_index in storage until keys match
        current = self.storage[hash_index]
        while current is not None:
            if current.key == key:
                # return value at given key
                return current.value
            current = current.ref

        # if key not found, return None
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

    ##### V.1
        # self.capacity *= 2
        # for key in self.storage:
        #     self._hash(key)

    ##### V.2
    #TODO: double capacity of hashtable
    # rehash all key/value pairs with .insert()
        
        # create a new hash table with double the capacity
        doubled = HashTable(self.capacity * 2)

        # for each linked list in storage
        for i in range(self.capacity):

            #check if there are lists at this index
            if self.storage[i] is not None:

                # for each node in the LL
                current = self.storage[i]
                while current is not None:

                    # insert new k:v pairs into the doubled list
                    doubled.insert(current.key, current.value)
                    current = current.ref
        self.capacity = doubled.capacity
        self.storage = doubled.storage

        return

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    ht.insert('line_4', "look at me")
   
    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht.retrieve('line_4'))
  

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)
   

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
   

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht.retrieve("line_4"))

    print("")
