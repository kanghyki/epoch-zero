class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

class WasRun(TestCase):
    def __init__(self, name):
        self.name = name
        self.wasRun = None
        self.wasSetUp = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = True
        self.log = self.log + "testMethod "

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = True
        self.log = "setUp "

    def tearDown(self):
        self.log = self.log + "tearDown "

class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

TestCaseTest("testRunning").run()
TestCaseTest("testTemplateMethod").run()
