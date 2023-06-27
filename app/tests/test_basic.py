#TO DELETE WHEN FIRST REAL UNIT TEST WILL BE CREATED
import unittest

class BasicTest(unittest.TestCase) : 
    def test_real_add(self) : 
        self.assertEqual(1+1, 2)
        
        
    # def test_false_add(self) : 
    #     self.assertEqual(1+1,3)
        
        
    if __name__ == "__main__":
        unittest.main()