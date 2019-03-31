import node
from importlib import reload as r
import linked_list_iterator
r(linked_list_iterator)
from linked_list_iterator import LinkedListIterator


class SinglyLinkedList():
    
    def parent_insert(self, key):
        self.__insert(key)
    
    def parent_delete(self, key):
        return self.__delete(key)
        
    def parent_search(self, key):
        return self.__search(key)
        
    def __init__(self):
        self._len = 0
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)
        
    def __len__(self):
        return self._len
        
    def insert(self, k):
        if self._len != 0:
            u = node.Node(k)
            u.next = self.head
            self.head = u
        else: 
            self.head = node.Node(k)
        self._len += 1

    __insert = insert # b4 execution, __insert becomes __SinglyLinkedList_insert   

    def search(self, key):  
        u = None
        for v in self: 
            if (key and v.key == key) or \
            (not key and v.next in (None, self.head)):
                break
            u = v
        else:
            u, v = None, None
        return u,v
        
    __search = search
    
    def delete(self, key):
        
        u,v = self.search(key)
        #element to delete doesn't exist in the list
        if v is None:
            return None, None
            
        if v is self.head:
            self.head = v.next
            self._len -= 1
            return None, v

        u.next = v.next
        self._len -= 1
        return u, v

    __delete = delete
            