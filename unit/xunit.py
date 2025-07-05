class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        self.name = name
        self.wasRun = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = True

    def run(self):
        method = getattr(self, self.name)
        method()

test = WasRun("testMethod")
assert test.wasRun == None
test.run()
assert test.wasRun == True
