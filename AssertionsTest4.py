import unittest

class TestAssertions(unittest.TestCase):
    def testName(self):
        list={"Java","C","Python"}
        #self.assertIn("Java",list)
        #self.assertIn("Javaa", list)
        self.assertNotIn("Javaa", list)

if __name__ =="__main__":
    unittest.main()