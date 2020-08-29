import unittest
from selenium import webdriver



class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("test_search")

    @unittest.skip("Skipping this one too")
    def test_advanced_search(self):
        print("test_advanced_search")

    @unittest.skipIf(1==1, "Skippig because condition i True , 1 is equal to 1")
    def test_prepaid_search(self):
        print("test_prepaid_search")


    def test_postpaid_search(self):
        print("test_postpaid_search")

if __name__=="__main__":
    unittest.main()
