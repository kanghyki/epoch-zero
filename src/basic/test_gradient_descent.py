from xunit import xunit
from gradient_descent import *

def f1(x):  # 기본 함수
    return x[0]**2 + x[1]**2

class TestClass(xunit.TestCase):
    def test_converges_to_minimum(self):
        init = np.array([3.0, 4.0])
        path = gradient_descent(f1, init, lr=0.1, steps=50)
        actual = path[-1]
        expect = np.array([0.0, 0.0])

        assert np.isclose(actual, expect, atol=1e-2).all(), f"""actual: {actual}
expect: {expect}"""

result = xunit.TestResult()
suite = xunit.TestSuite()

suite.add(TestClass('test_converges_to_minimum'))

suite.run(result)
print(result.detail())
print(result.summary())
