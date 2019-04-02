class LinkedListIterator():
    """
        an instance of this iterator can be used to go through 
        regular and circular linked lists
    """

    def __init__(self, head):
        self.curr = self.list_head = head
        self.past_the_head = False #can't be passed the head to begin :)
        
    def __next__(self):
        """
        2nd expression in if is how you stop iteration for circular linked list
        """
        if not self.curr or \
            (self.past_the_head and self.curr is self.list_head):
            raise StopIteration
        else:
            hold = self.curr
            self.curr = self.curr.next
            self.past_the_head = True
            return hold
