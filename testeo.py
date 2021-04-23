import unittest
import to_test as subject


class testMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(subject.add(1,2),3)
        self.assertEqual(subject.add(1,4),5)
    def test_times(self):
        self.assertEqual(subject.times(100, 10),1000)

if __name__ == '__main__':
    unittest.main()