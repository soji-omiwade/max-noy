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
        
    def __init__(self):
        print('initializing some instance from a SinglyLinkedList class ...')
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
    """
    if key is not found, return None
    otherwise, return the node previous
    """
    def _search_for_prev(self, key):
        u = self.head
        while u is not None:
            if u.key is key:
                break
            prev = u
            u = u.next
        return prev

    def search(self, key=None, search_for_last = False):
    
        print('searching for ', key, '...')
        prev = None
        for v in self: 
            if (not search_for_last and v.key == key) or \
            (search_for_last and v.next in (None, self.head)):
                break
            prev = v
        else:
            v = None
        if v is not None:
            print('search found it: ', v.key)
        return prev,v
        
    def delete(self, key):
        
        prev,v = self.search(key)
        #element to delete doesn't exist in the list
        if v is None:
            return None, None
            
        if v is self.head:
            self.head = v.next
            self._len -= 1
            return None, v
        """
        now v can never be the head, where prev is undefined
        specifically, now we can say prev is None only if 
        the element to delete doesn't exist: if the element 
        did exist, it would have a prev!
        UPDATE: nope. STOP. now search already determined whehter
        it existed or not and returned if it didn't. 
        hence prev must exist.
        """
        prev.next = v.next
        self._len -= 1
        return prev, v
        
    __delete = delete
            