from xunit import xunit
from numerical_derivative import numerical_derivative
import numpy as np

class TestNumericalDerivative(xunit.TestCase):
    def test_square(self):
        # f(x) = x^2
        actual = numerical_derivative(lambda x: x**2, 3)
        expect = 6

        assert np.isclose(actual, expect), f"""actual: {actual}
expect: {expect}"""


    def test_sin(self):
        # f(x) = sin(x)
        actual = numerical_derivative(np.sin, 0)
        expect = 1
        assert np.isclose(actual, expect), f"""actual: {actual}
expect: {expect}"""
         

result = xunit.TestResult()

suite = xunit.TestSuite()
suite.add(TestNumericalDerivative('test_square'))
suite.add(TestNumericalDerivative('test_sin'))

suite.run(result)

print(result.detail())
print(result.summary())
