"""Most of the function names here are self-explanatory

This script was written to test the linked list implementations, but now 
I reserve such testing to python's unittest
"""
from time import sleep
from random import randint
import singly_linked_list as sll
import circular_linked_list as cll

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
    print(l.delete(l.head.key)[1].key, 'deleted')
    
def delete_last(l):
    if len(l) == 0:
        print('nothing to delete; list empty')
        return
    v = l.getLast()
    print(l.delete(v.key)[1].key)

def print_all(l, stall=1):
    counter = 0
    reset_counter = 0
    for u in l:
        print(u.key, end=' ', flush = True)
        counter += 1
        sleep(stall)
        # if counter == 5:
            # counter = 0
            # delete_first(l)
            # reset_counter += 1
            # print()
        # if reset_counter == 5:
            # break
    print()
    
if __name__ != 'singly_linked_list':
    # l = sll.SinglyLinkedList()
    l = cll.CircularLinkedList()
    # delete_all(l, True)
    # delete_all(l, False)
    for i in range(5):
        key = randint(0,99)
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
    
