from random import randint
import singly_linked_list as sll
from importlib import reload
reload(sll)

def delete_all(l, from_front):
    while not l.empty():
        if from_front:
            delete_first(l)
        else:
            delete_last(l)
            
def delete_first(l):
    if len(l) == 0:
        print('nothing deleted; list empty')
        return
    print(l.delete(l.head).key)
    
#todo: get reid of head (i like it private)
#instead use iterator.    
def delete_last(l):
    if len(l) == 0:
        print('nothing deleted; list empty')
        return
    u = l.head
    while u != None:
        prev = u
        u = u.next
    #if len(l) == 1 or more, no prob
    print(l.delete(prev).key)

def print_all(l):
    for u in l:
        print(u.key, end=' ')
    print()
"""
usage: 
"""
if __name__ != 'singly_linked_list':
    l = sll.SinglyLinkedList()
    # delete_all(l, True)
    # delete_all(l, False)
    for i in range(5):
        key = randint(0,9)
        print(key, end=' ')
        l.insert(key)
    print_all(l)
    # delete_all(l, True)
    # for i in range(5):
        # l.insert(random(0,10))
    # print_all(l)
    # delete_all(l, False)
    # for i in range(5):
        # l.insert(random(0,10))
    # print_all(l)
    
