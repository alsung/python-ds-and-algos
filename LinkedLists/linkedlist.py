# the Linked List data structure with implemented methods: 
    # search for key 
    # insert a new node after a specified node
    # delete a node

class Node: 
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        print(self.data)

class LinkedList:
    def __init__(self):
        self.head = Node()

    def search_list(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total+=1
            curr = curr.next
        return total

    def display(self):
        elems = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            elems.append(curr_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        curr_idx = 0
        curr_node = self.head
        while True:
            curr_node = curr_node.next
            if curr_idx == index: return curr_node.data
            curr_idx += 1

    def remove(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        curr_idx = 0
        curr_node = self.head
        while True:
            last_node = curr_node
            curr_node = curr_node.next
            if curr_idx == index:
                last_node.next = curr_node.next
                return
            curr_idx += 1
    

my_list = LinkedList()

my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

my_list.remove(1)

my_list.display()

