from xunit import xunit
from transformer2d import *

class TestGeoTransformation(xunit.TestCase):
    def setup(self):
        self.t2d = Transformer2D()

    def test_rotate(self):
        vectors = [
            ((1, 0), (0, 1)),
            ((3, 0), (0, 3)),
            ((5, 0), (0, 5)),
            ((5, 2), (-2, 5))
        ]

        for input, expect in vectors:
            vec = np.array(input)
            actual = self.t2d.rotate(vec, 90.0)
            expect = np.array(expect)

            assert np.allclose(actual, expect), 'rotate error'

    def test_scale(self):
        vec = np.array([1,2])

        actual = self.t2d.scale(vec, 2.0)
        expect = np.array([2, 4])

        assert np.array_equal(actual, expect), "scale error"

    def test_translate(self):
        vec = np.array([1, 2])
        offset = np.array([1.5, 3.2])

        actual = self.t2d.translate(vec, offset)
        expect = np.array([2.5, 5.2])

        assert np.array_equal(actual, expect), "translate error"

    def test_transform(self):
        vec = np.array([1, 0])

        actual = self.t2d.transform(vec, rotation=90, scale=(2, 2), translation=(1, 1))
        print(type(actual))
        # [0,1] -> [0,2] -> [1,3]
        expect = np.array([1, 3])
        assert np.array_equal(actual, expect), f"""actual: {actual}
expect: {expect}"""

result = xunit.TestResult()
suite = xunit.TestSuite()
suite.add(TestGeoTransformation('test_rotate'))
suite.add(TestGeoTransformation('test_scale'))
suite.add(TestGeoTransformation('test_translate'))
suite.add(TestGeoTransformation('test_transform'))
suite.run(result)

print(result.detail())
print(result.summary())
