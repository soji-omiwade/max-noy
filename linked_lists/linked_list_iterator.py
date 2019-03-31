"""
need to stop the iterating based on list size
otherwise cirular linked list will fail
in which case. i should move this out 
since why have a functionality that dosne't pertain to singly linked alone
when it's also used by cirular
"""
#this is the class that should really move out. no need to move the search out!
class LinkedListIterator():

    def __init__(self, head):
        self.curr = self.list_head = head
        self.iterationStarted = False
        
    def __next__(self):
        if not self.curr or \
            (self.iterationStarted and self.curr is self.list_head):
            raise StopIteration
        else:
            hold = self.curr
            self.curr = self.curr.next
            self.iterationStarted = True
            return hold
