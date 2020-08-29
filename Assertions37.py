import unittest

class TestAssertions(unittest.TestCase):
    def testName(self):
        list={"Java","C","Python"}

        self.assertEqual(100,100)
        self.assertNotEqual(10,23)
        self.assertGreater(100,10)
        self.assertGreaterEqual(100,25)
        self.assertLessEqual(100,100)
        self.assertLessEqual(10, 100)
        self.assertLess(100,1236)


if __name__ =="__main__":
    unittest.main()