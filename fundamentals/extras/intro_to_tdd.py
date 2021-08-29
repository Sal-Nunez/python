import unittest

def reverseList(list):
    for x in range(int(len(list)/2)):
        list[x], list[len(list) - 1 - x] = list[len(list) - 1 - x], list[x]
    return list

class ReverseListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])
    def testTwo(self):
        self.assertEqual(reverseList([1, 5, 6, 7, 8, 4]), [4, 8, 7, 6, 5, 1])
    def testThree(self):
        self.assertEqual(reverseList(['jack', 'john', 'jill', 'jenny']), ['jenny', 'jill', 'john', 'jack'])
    def testFour(self):
        self.assertEqual(reverseList([500, 30, 250, 1000, 2.5, 3]), [3, 2.5, 1000, 250, 30, 500])



if __name__ == '__main__':
    unittest.main()