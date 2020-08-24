import unittest
from selenium import webdriver

class TestingWeb(unittest.TestCase):
    def test_First(self):
        self.driver=webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")
        self.driver.get("https://www.eenadu.net/")
        print("Opening Eenadu website")
        self.driver.close()

    def test_Second(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")
        self.driver.get("https://www.google.co.uk/https://www.eenadu.net/")
        print("Opening Google website")
        self.driver.close()

if __name__=="__main__":
    unittest.main()



