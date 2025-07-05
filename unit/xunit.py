import traceback

class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0
        self.wasTearDownBroken = False
        self.wasSetUpBroken = False
        self.str_error_msg = ''
        self.failure_indices = []
        self.classNames = []
        self.methodNames = []

    def testStarted(self, className, methodName):
        self.classNames.append(className)
        self.methodNames.append(methodName)
        self.runCount = self.runCount + 1

    def testFailed(self):
        self.failure_indices.append(self.runCount - 1)
        self.failureCount = self.failureCount + 1

    def tearDownBroken(self):
        self.wasTearDownBroken = True

    def setUpBroken(self):
        self.wasSetUpBroken = True

    def summary(self):
        sum = f"{self.runCount} run, {self.failureCount} failed"
        if self.wasSetUpBroken:
            sum = sum + ", SetUp was broken"
        if self.wasTearDownBroken:
            sum = sum + ", TearDown was broken"
        return sum

    def detail(self):
        det = ''
        for i in range(0, self.runCount):
            ret = ''
            if i in self.failure_indices:
                ret = 'failed'
            else:
                ret = 'pass'
            det = det + f"[{ret:^8}] {self.classNames[i]} > {self.methodNames[i]}\n"
        return det;

    def add_error_msg(self, e):
        self.str_error_msg = self.str_error_msg + str(e) + '\n'

    def error_msg(self):
        return self.str_error_msg

class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, result):
        result.testStarted(self.__class__.__name__, self.name)
        try:
            try:
                self.setUp()
            except Exception as e:
                result.setUpBroken()
                # fmt = traceback.format_exc()
                result.add_error_msg(e)
                raise

            method = getattr(self, self.name)
            method()

        except:
            result.testFailed()

        try:
            self.tearDown()
        except Exception as e:
            result.tearDownBroken()
            # fmt = traceback.format_exc()
            result.add_error_msg(e)

######################################
#       Test Classes                 #
######################################

class WasRun(TestCase):
    def __init__(self, name):
        self.name = name
        self.wasRun = None
        self.wasSetUp = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = True
        self.log = self.log + "testMethod "

    def testBrokenMethod(self):
        raise Exception

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = True
        self.log = "setUp "

    def tearDown(self):
        self.log = self.log + "tearDown "

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        result = TestResult()
        test.run(result)
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = TestResult()
        test.run(result)
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = TestResult()
        test.run(result)
        assert("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted('class', 'method')
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert("2 run, 1 failed" == result.summary())

    def testBrokenTearDown(self):
        test = TestBrokenTearDown("testMethod")
        result = TestResult()
        test.run(result)
        assert("1 run, 0 failed, TearDown was broken" == result.summary())
        assert("teardown broken!\n" == result.error_msg())

    def testBrokenSetUp(self):
        test = TestBrokenSetUp("testMethod")
        result = TestResult()
        test.run(result)
        assert("1 run, 1 failed, SetUp was broken" == result.summary())
        assert("setup broken!\n" == result.error_msg())

    def testResultDetail(self):
        result = TestResult()
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(result)

        assert("4 run, 1 failed" == result.summary())
        assert('''[  pass  ] WasRun > testMethod
[  pass  ] WasRun > testMethod
[  pass  ] WasRun > testMethod
[ failed ] WasRun > testBrokenMethod
''' == result.detail())

class TestBrokenTearDown(TestCase):
    def tearDown(self):
        raise Exception('teardown broken!')

    def testMethod(self):
        pass

class TestBrokenSetUp(TestCase):
    def setUp(self):
        raise Exception('setup broken!')

    def testMethod(self):
        pass

suite = TestSuite()

suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSuite"))
suite.add(TestCaseTest("testBrokenTearDown"))
suite.add(TestCaseTest("testBrokenSetUp"))
suite.add(TestCaseTest("testResultDetail"))

result = TestResult()
suite.run(result)
print(result.detail())
print(result.summary())
