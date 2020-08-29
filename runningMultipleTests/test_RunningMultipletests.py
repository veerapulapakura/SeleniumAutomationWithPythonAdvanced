import pytest

@pytest.yield_fixture()
def setup():
    print("")

    print("Running before each method as it is a Fixture method")

    yield
    print("Running after each method as it is a Fixture method")


def testMethod(setup):
    print("Printing the data from the test Method1")


def testMethod20(setup):
    print("Printing the data from the test Method2")

