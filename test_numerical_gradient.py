from xunit import xunit
from numerical_gradient import *
import numpy as np

class TestNumericalGradient(xunit.TestCase):
    def setup(self):
        def f(v):
            x, y = v
            return x**2 + y**2
        self.f = f


    # f(3.0001, 4.0) = (3.0001)^2 + (4.0)^2 = 9.00060001 + 16 = 25.00060001
    # 𝑓(2.9999, 4.0) = (2.9999)^2 + (4.0)^2 = 8.99940001 + 16 = 24.99940001
    # 25.00060001−24.99940001       0.0012
    # -----------------------  =  ----------- = 6.0
    #      2 * 0.0001               0.0002
    def test_partial_derivative(self):
        data = np.array([3.0, 4.0])

        actual = partial_derivative(self.f, data, 0)

        expect = 6.0
        assert np.allclose(actual, expect), f"""actual: {actual}
expect: {expect}
"""
        pass

    def test_gradient(self):
        data = np.array([3.0, 4.0])

        actual = numerical_gradient(self.f, data)

        expect = np.array([6.0, 8.0])
        assert np.allclose(actual, expect), f"""actual: {actual}
expect: {expect}
"""

    def test_gradient_descent(self):
        epoch = 100
        rate = 0.1
        data = np.array([3.0, 4.0])

        for _ in range(epoch):
            grad = numerical_gradient(self.f, data)
            data = data - grad * rate
            print(data)

        expect = np.array([0.0, 0.0])
        assert np.allclose(data, expect), f"""actual: {data}
expect: {expect}
"""


result = xunit.TestResult()
suite = xunit.TestSuite()

suite.add(TestNumericalGradient('test_partial_derivative'))
suite.add(TestNumericalGradient('test_gradient'))
suite.add(TestNumericalGradient('test_gradient_descent'))

suite.run(result)
print(result.detail())
print(result.summary())
