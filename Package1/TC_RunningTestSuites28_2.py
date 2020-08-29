import unittest

class LoginTestTwo(unittest.TestCase):
    def test_loginFacebookTwo(self):
        print("This is the login function by Facebook")
        self.assertTrue(True)

    def test_loginTwitterTwo(self):
        print("This is the login function by Twitter")
        self.assertTrue(True)

    def test_loginGoogleTwo(self):
        print("This is the login function by Google")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()
