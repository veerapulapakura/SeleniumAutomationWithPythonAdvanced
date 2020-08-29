import unittest

class PaymentTest(unittest.TestCase):
    def test_PaymentDoller(self):
        print("This is the test_PaymentDoller function")
        self.assertTrue(True)

    def test_PaymentPound(self):
        print("This is the test_PaymentPound function")
        self.assertTrue(True)

    def test_PaymentEuro(self):
        print("This is the test_PaymentEuro function")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()
