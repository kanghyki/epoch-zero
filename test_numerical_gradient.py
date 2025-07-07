from xunit import xunit
from numerical_gradient import *

class TestClass(xunit.TestCase):
    def test_something(self):
        pass

result = xunit.TestResult()
suite = xunit.TestSuite()

suite.add(TestClass('test_something'))

suite.run(result)
print(result.detail())
print(result.summary())
