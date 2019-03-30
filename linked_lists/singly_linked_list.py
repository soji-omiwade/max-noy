import node

class Boo():
    def __init__(self, head):
        self.pooh = head
    def __next__(self):
        if not self.pooh:
            raise StopIteration
        else:
            v = self.pooh
            self.pooh = self.pooh.next
            return v
def search(key):
    print('her it is sucker' + str(key))
    exit()
class SinglyLinkedList():
    
    def __init__(self):
        print('creating a SinglyLinkedList instance ...')
        self._len = 0
        self.head = None

    def __iter__(self):
        return Boo(self.head)
        
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
        
    def search(self, key):
        prev = None
        for v in self:
            if v.key == key:
                break
            prev = v
        else:
            v = None
        if v is not None:
            print('search: ' + str(v.key))
        return prev,v
        
    def delete(self, key):
        
        prev,v = self.search(key)
        #element to delete doesn't exist in the list
        if v is None:
            return None
            
        if v is self.head:
            self.head = v.next
            self._len -= 1
            return v
        """
        now v can never be the head, where prev is undefined
        specifically, now we can say prev is None only if 
        the element to delete doesn't exist: if the element 
        did exist, it would have a prev!
        UPDATE: nope. STOP. now search already determined whehter
        it existed or not and returned if it didn't. 
        hence prev must exist.
        """
        v = prev.next
        prev.next = v.next
        self._len -=1
        return v
            