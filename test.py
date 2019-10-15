from solution import split_array 
import unittest

class SolutionTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(split_array([ 1, 3, 3, 4, 5 ]), True)

    def test2(self):
        self.assertEqual(split_array([ 2, 4, 5, 6 ]), False)

    def test3(self):
        self.assertEqual(split_array([1, 2, 3]), True)
        
    def test4(self):
        self.assertEqual(split_array([1,3,3,4,13,-2]), True)

    def test5(self):
        self.assertEqual(split_array([6,6,8,8,3,2,1]), True)

    def test6(self):
        self.assertEqual(split_array([4,8,1,0,5,0]), True)

    def test7(self):
        self.assertEqual(split_array([10,  20 , 30 , 5 , 40 , 50 , 40 , 15]), True)

    def test8(self):
        self.assertEqual(split_array([4,8,7,15,20,90,8,4,8,3,3,1,10,-1]), True)

if __name__ == '__main__':
    unittest.main()
