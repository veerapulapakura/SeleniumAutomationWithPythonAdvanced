import unittest
from selenium import webdriver

def setUpModule():
        print("This is setUpModule")


def tearDownModule():
    print("This is tearDownModule")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("This is set up method")

    @classmethod
    def tearDown(self):
        print("This is tearDown method")
        print("")

    @classmethod
    def setUpClass(cls):
        print("This is set up  class runs at the beginning of all the tests ")

    @classmethod
    def tearDownClass(cls):
        print("This is tearDown class runs at the of all the tests")


    def test_search(self):
        print("test_search")

    def test_advanced_search(self):
        print("test_advanced_search")

    def test_prepaid_search(self):
        print("test_prepaid_search")


    def test_postpaid_search(self):
        print("test_postpaid_search")

if __name__=="__main__":
    unittest.main()
