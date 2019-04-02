import unittest
import circular_linked_list as cll
from test_singly_linked_list_methods import TestLinkedListMethods

class TestCircularLinkedListMethods(TestLinkedListMethods):
    def setUp(self):
        self.l = cll.CircularLinkedList()
        for i in range(5):
            self.l.insert(i)

    def test_search_head(self):
        """
            3. test for head, where prev is None if singly_linked_list
                and tail if circular_linked_list.
        """
        findKey = len(self.l)-1
        u,v = self.l.search(findKey)
        self.assertEqual((u.key, v.key), (0, findKey))

    def test_tail(self):
        self.assertEqual(self.l.tail.key, 0)
        
    def test_get_tail(self):
        self.assertEqual(self.l.get_last().key, 0)
        
    def test_append(self):
        self.l.append(len(self.l))
        self.assertEqual(self.l.head.key, len(self.l)-2)
        self.assertEqual(self.l.tail.key, len(self.l)-1)
        
if __name__ == '__main__':
    unittest.main()
