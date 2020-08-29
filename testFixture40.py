import pytest

@pytest.fixture()
def setup():
    print("Running before each method as it is a Fixture method")

def testMethod14(setup):
    print("Printing the data from the test Method1")

def testMethod25(setup):
    print("Printing the data from the test Method2")
