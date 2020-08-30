import unittest
from selenium import webdriver
import HtmlTestRunner

class TestingWebReports(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")
        cls.driver.maximize_window()
        print("Driver is getting started")

    def test_First(self):
        self.driver.get("https://www.google.co.uk/")
        self.assertEqual("Google", self.driver.title,"Google is not the correct one")


    def test_Second(self):
        self.driver.get("https://www.linkedin.com/feed/")
        self.assertNotEqual("Google", self.driver.title, "Google is not the correct one")
# unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\User\\PycharmProjects\\SeleniumWithPython\\Reports"))

    @classmethod
    def tearDown(cls):
        print("Driver is getting closed")
        print("my name is manogna")


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\SeleniumWithPython\\Reports"))



