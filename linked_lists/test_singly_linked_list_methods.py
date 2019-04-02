import unittest
import singly_linked_list as sll

class TestLinkedListMethods(unittest.TestCase):
    def setUp(self):
        self.l = sll.SinglyLinkedList()
        for i in range(5):
            self.l.insert(i)
   
    def test_len_on_insert(self):
        old_size = len(self.l)
        self.l.insert(42)
        self.assertEqual(len(self.l), old_size + 1)

    def len_on_delete_test(self, index):
        old_size = len(self.l)
        self.l.delete(len(self.l)-1)
        self.assertEqual(len(self.l), old_size - 1)
        
    def test_len_on_delete_all_sides(self):
        self.len_on_delete_test(int(len(self.l)/2))
        self.len_on_delete_test(0)
        self.len_on_delete_test(len(self.l))
        self.len_on_delete_test(10)
    
    def test_search_middle(self):
        """
            1. test middle element is found; 
        """
        findKey = int(len(self.l)/2)
        u,v = self.l.search(findKey)
        self.assertEqual((u.key, v.key),(findKey+1, findKey))
        
    def test_search_non_existent(self):
        """
            2. test for element that doesn't exist
            3. test for head, where prev is None if singly_linked_list
                and tail if circular_linked_list.
        """
    
        u,v = self.l.search(len(self.l))
        self.assertEqual((u, v), (None, None))

    def test_search_head(self):
        """
            3. test for head, where prev is None if singly_linked_list
                and tail if circular_linked_list.
        """
        findKey = len(self.l)-1
        u, v = self.l.search(findKey)
        self.assertEqual((u, v.key), (None, findKey))
        
    #todo
    # def test_insert_non_existent_element(self):
        # pass
        
if __name__ == '__main__':
    unittest.main()

