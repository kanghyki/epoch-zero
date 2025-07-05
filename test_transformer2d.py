from xunit import xunit
from transformer2d import *

class TestGeoTransformation(xunit.TestCase):
    def setup(self):
        self.t2d = Transformer2D()

    def test_rotate(self):
        self.t2d.rotate()
        pass

    def test_scale(self):
        self.t2d.scale()
        pass

    def test_translate(self):
        self.t2d.translate()
        pass

result = xunit.TestResult()
suite = xunit.TestSuite()
suite.add(TestGeoTransformation('test_rotate'))
suite.add(TestGeoTransformation('test_scale'))
suite.add(TestGeoTransformation('test_translate'))
suite.run(result)

print(result.detail())
print(result.summary())
