import unittest
from selenium import webdriver

class TestingAsserts34(unittest.TestCase):
    def test_First(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")
        driver.get("https://www.google.co.uk/")
        print("Opening google website")
        titleofthePage = driver.title
        print(titleofthePage)
        driver.close()
        #Asserting the code
        self.assertFalse(titleofthePage == "Google")

if __name__=="__main__":
    unittest.main()



