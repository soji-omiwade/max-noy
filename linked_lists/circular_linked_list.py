import singly_linked_list as sll
from node import Node

class CircularLinkedList(sll.SinglyLinkedList):
    """Implements a circular singly linked list.
    
    Instances can insert or delete. 
    Like its parent, inserts are at the head, and delete specifies keys not 
    nodes. append(key) inserts after the tail
    """
    def __init__(self):
    """This class inherits from SinglyLinkedList where a head is initialized.
    
    has a tail, which points to the head. this is what makes the list circular
    """
        self.tail = None
        super().__init__()
        
    def search(self, key = None):
        u, v = self.parent_search(key)
        if v is self.head:
            u = self.tail
        return u, v
        
    def get_last(self):
    """Returns the tail nodes to clients.
    
    Unlike a noncircular linked list which has to iterate to find the last,
    this method can just return the tail instance we anyway must have.
    """
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