import unittest
def isEven(n):
    if n % 2 == 0:
       return True
    else:
       return False
class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertTrue(isEven(2))
    def testThree(self):
        self.assertFalse(isEven(3))

if __name__ == '__main__':
    unittest.main()