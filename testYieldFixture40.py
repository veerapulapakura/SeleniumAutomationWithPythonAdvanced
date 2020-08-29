import pytest

@pytest.yield_fixture()
def setup():
    print("")
    print("")
    print("Running before each method as it is a Fixture method")
    print("")
    yield
    print("Running after each method as it is a Fixture method")
    print("")

def testMethod1(setup):
    print("Printing the data test Method1")
    print("")

def testMethod2(setup):
    print("Printing the data Method2")
    print("")
