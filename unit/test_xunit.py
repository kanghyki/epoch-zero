from xunit import *

######################################
#       Test Classes                 #
######################################

class WasRun(TestCase):
    def __init__(self, name):
        self.name = name
        self.wasRun = None
        self.wasSetUp = None
        TestCase.__init__(self, name)

    def test_method(self):
        self.wasRun = True
        self.log = self.log + "test_method "

    def test_broken_method(self):
        raise Exception

    def setup(self):
        self.wasRun = None
        self.wasSetUp = True
        self.log = "setup "

    def teardown(self):
        self.log = self.log + "teardown "

class TestCaseTest(TestCase):
    def test_template_method(self):
        test = WasRun("test_method")
        result = TestResult()
        test.run(result)
        assert("setup test_method teardown " == test.log)

    def test_result(self):
        test = WasRun("test_method")
        result = TestResult()
        test.run(result)
        assert("1 run, 0 failed" == result.summary())

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = TestResult()
        test.run(result)
        assert("1 run, 1 failed" == result.summary())

    def test_failed_resultFormatting(self):
        result = TestResult()
        result.test_started('class', 'method')
        result.test_failed()
        assert("1 run, 1 failed" == result.summary())

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        result = TestResult()
        suite.run(result)
        assert("2 run, 1 failed" == result.summary())

    def test_broken_teardown(self):
        test = TestBrokenTearDown("test_method")
        result = TestResult()
        test.run(result)
        assert("1 run, 0 failed, TearDown was broken" == result.summary())
        assert("teardown broken!\n" == result.error_msg())

    def test_broken_setup(self):
        test = TestBrokenSetUp("test_method")
        result = TestResult()
        test.run(result)
        assert("1 run, 1 failed, SetUp was broken" == result.summary())
        assert("setup broken!\n" == result.error_msg())

    def test_result_detail(self):
        result = TestResult()
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        suite.run(result)

        assert("4 run, 1 failed" == result.summary())
        assert('''[  pass  ] WasRun > test_method
[  pass  ] WasRun > test_method
[  pass  ] WasRun > test_method
[ failed ] WasRun > test_broken_method
''' == result.detail())

class TestBrokenTearDown(TestCase):
    def teardown(self):
        raise Exception('teardown broken!')

    def test_method(self):
        pass

class TestBrokenSetUp(TestCase):
    def setup(self):
        raise Exception('setup broken!')

    def test_method(self):
        pass

suite = TestSuite()

suite.add(TestCaseTest("test_template_method"))
suite.add(TestCaseTest("test_result"))
suite.add(TestCaseTest("test_failed_resultFormatting"))
suite.add(TestCaseTest("test_failed_result"))
suite.add(TestCaseTest("test_suite"))
suite.add(TestCaseTest("test_broken_teardown"))
suite.add(TestCaseTest("test_broken_setup"))
suite.add(TestCaseTest("test_result_detail"))

result = TestResult()
suite.run(result)
print(result.detail())
print(result.summary())
