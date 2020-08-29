import unittest

class LoginTest(unittest.TestCase):
    def test_loginFacebook(self):
        print("This is the login function by Facebook")
        self.assertTrue(True)

    def test_loginTwitter(self):
        print("This is the login function by Twitter")
        self.assertTrue(True)

    def test_loginGoogle(self):
        print("This is the login function by Google")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()
