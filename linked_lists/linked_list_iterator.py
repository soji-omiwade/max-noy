class LinkedListIterator():
    """An instance of this iterator can be used lists.
    
    Both noncircular and circular linked lists. next is implemented
    with two cases (the two expressions in the if. 
    2nd expression in if is how you stop iteration for circular linked list
    first expression stops iteration for noncircular lists; or both lists
    when the list is empty.
    """

    def __init__(self, head):
        self.curr = self.list_head = head
        self.past_the_head = False #can't be passed the head to begin :)
        
    def __next__(self):
        if not self.curr or \
            (self.past_the_head and self.curr is self.list_head):
            raise StopIteration
        else:
            hold = self.curr
            self.curr = self.curr.next
            self.past_the_head = True
            return hold
