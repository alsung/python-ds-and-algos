# Implementation of HashSet with chaining data structure in Python from scratch
# no built-in hash table libraries are used

# Supported functions:
#   - add(x): inserts a value x into the HashSet
#   - contains(x): checks whether the value x is present in the Hashset or not
#   - remove(x): removes x from the HashSet. In case the value doesn't exist,
#     do nothing 

# Bucket class:
#   - initializes a list representing a 'bucket' that acts as a linked list for 
#     multiple values under the same hash key
#   - attributes: 
#       - bucket: contains the bucket list of values
#       - length: contains the length of bucket
#   - functions:
#       - update: append item to hashset if doesn't already exist
#       - get: returns True if key is in hashset, else False
#       - remove: removes bucket key entry from bucket list
class Bucket:
    def __init__(self):
        self.bucket = []
        self.length = len(self.bucket)

    def update(self, key):
        found = False
        for i, k in enumerate(self.bucket):
            if key==k:
                self.bucket[i] = key
                found = True
                break
        if not found:
            self.bucket.append(key)

    def get(self, key):
        for k in self.bucket:
            if k == key:
                return True
        return False
    
    def remove(self, key):
        for i, k in enumerate(self.bucket):
            if key == k:
                del self.bucket[i]

# HashSet class:
# includes all functions to initialize hash table of configurable length, 
# add items, remove items, and see if hash table contains a key value. 
#   - attributes
#       - key_space: number of hash table slots
#       - hash_table: list of Bucket class lists for each hash table slot
#   - functions
#       - hash function: key % number of slots
#       - add: uses Bucket class function update() to insert key into list
#       - remove: removes key from hash table w Bucket class remove()
#       - contains: returns True if key is in hash table, else False w 
#         Bucket class get()
#       - display: prints out all contents of hash table in readable manner
class MyHashSet:
    def __init__(self):
        # set size of hashtable
        self.key_space = 20
        self.hash_table = [Bucket() for i in range(self.key_space)]
    
    def add(self, key):
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key)

    def remove(self, key):
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)

    def contains(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def display(self):
        for i in range(len(self.hash_table)):
            print(i, end = " ")
            for j in range(len(self.hash_table[i].bucket)):
                print("-->", end = " ")
                print(self.hash_table[i].bucket[j], end=" ")
            print()

ob = MyHashSet()
ob.add(1)
ob.add(3)
ob.add(62)
ob.add(2334)
ob.add(5)
ob.add(2)
ob.display()
print(ob.contains(1)) # True
print(ob.contains(2)) # False
ob.add(2)
print(ob.contains(2)) # True
ob.remove(2)
print(ob.contains(2)) # False

