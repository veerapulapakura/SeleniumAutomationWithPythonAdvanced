import unittest
from Package1.TC_RunningTestSuites28_2 import LoginTestTwo
from Package1.TC_RunningTestSuites38 import LoginTest

from Package2.TC_Payments import PaymentTest
from Package2.TC_PaymentsTwo import PaymentTestTwo

#In the above we have imported the python classes from package, .Py file then classname
# Get all the tests from the imported classes
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTestTwo)
tc2=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentTestTwo)

#Creating Test suites

sanitytests=unittest.TestSuite([tc1,tc2])
funtionaltest=unittest.TestSuite([tc3,tc4])
unittest.TextTestRunner(verbosity=2).run(funtionaltest)  # gives more details of all logs



