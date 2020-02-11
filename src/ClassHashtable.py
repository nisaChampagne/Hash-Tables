# '''
# Linked List hash table key/value pair
# '''

# SLL  value --pointer-> value --pointer->
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pointer = None # changed to pointer for preference

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

        ######## MINE
        # print('Key to insert: ', key)  # returns keys in terminal yay!
        # print('Value to insert: ', value) # returns values in terminal yay!

        # hash_index = self._hash_mod(key)
        # print('index: ', hash_index) # current index

        # if key not in self.storage:
        #     self.storage.append(hash_index)
        #     self.storage[hash_index] = value



        index = self._hash_mod(key)
        if self.storage[index] is not None:
            print(f"WARNING: COLLISION HAS OCCURRED AT {index}")
        else:
            self.storage[index] = (key,value) # tuple # will replace with LinkedPair eventually
        return

        '''
        class notes:
            * index = self._hash_mod(key)
            * if self.storage[index] is not None:
                print(f"WARNING: COLLISION HAS OCCURRED AT {index}")
                return
            * else:
                self.storage[index] = value
            * return



        '''


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # hash_index = self._hash_mod(key)
        # if self.storage[hash_index].key:
        #     self.storage[hash_index] = None
        # else: 
        #     print(f"{key} not found")


        index = self._hash_mod(key)
        if self.storage[index] is not None:
            if self.storage[index][0] == key:
                self.storage[index] = None
            else:
                print(f"WARNING: COLLISION HAS OCCURRED AT {index}")
        else:
            print(f"{index} not found")
        return



        '''


        '''


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # hash_index = self._hash_mod(key)
        # if self.storage[hash_index] is not None:
        #     print(f"key: {key}, value: {self.storage[hash_index]} GOT IT!")
        #     return self.storage[hash_index]
        # else:
        #     print(f"{key} was not found!")
        #     return None
            
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            if self.storage[index][0] == key:
                return self.storage[index][1]
            else:
                print(f"WARNING: COLLISION HAS OCCURRED AT {index}")
        else:
            return None
        return


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # self.capacity *= 2
        # for key in self.storage:
        #     self._hash(key)


        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for item in old_storage:
            self.insert(item[0], item[1])


if __name__ == "__main__":

    ht = HashTable(2)

    ht.insert('key1', 'hello')
    ht.insert('key2', 'goodbye')

    print(ht.storage)

    ht.remove("key1")

    ht.insert('this', "oops")

    print(ht.storage)

    ht.retrieve('key3')

    # ht = HashTable(2)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
