import unittest

class PaymentTestTwo(unittest.TestCase):
    def test_PaymentDollerTwo(self):
        print("This is the test_PaymentDoller function")
        self.assertTrue(True)

    def test_PaymentPoundTwo(self):
        print("This is the test_PaymentPound function")
        self.assertTrue(True)

    def test_PaymentEuroTwo(self):
        print("This is the test_PaymentEuro function")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()