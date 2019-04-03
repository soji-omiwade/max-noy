import singly_linked_list as sll
from node import Node

class CircularLinkedList(sll.SinglyLinkedList):
    """
        usage: just some clean insert and delete implementations

    """
    def __init__(self):
        self.tail = None
        super().__init__()
        
    def search(self, key = None):
        u, v = self.parent_search(key)
        if v is self.head:
            u = self.tail
        return u, v
        
    def get_last(self):
        return self.tail
        
    def insert(self, key):
        self.parent_insert(key)
        if self.tail is None: #must be the head. i.e., first time
            self.head.next = self.head
            self.tail = self.head
        else:
            self.tail.next = self.head

    def delete(self, key):
        old_head = self.head
        old_tail = self.tail
        prev_v, v = self.parent_delete(key)
        if len(self) != 0:
            if v is old_head:
                self.tail.next = self.head
            #prev_v cant be None. that wud be old_head case, in which case
            #prev_v wouldn't be used
            elif v is old_tail: 
                self.tail = prev_v
        return prev_v, v
        
    def append(self, key):
        v = Node(key)
        v.next = self.head
        self.tail.next = v
        self.tail = v
        self._len += 1