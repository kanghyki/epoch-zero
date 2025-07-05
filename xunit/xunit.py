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
        self.run_count = 0
        self.was_tear_down_broken = False
        self.was_setup_broken = False
        self.str_error_msg = ''
        self.failure_indices = []
        self.class_names = []
        self.method_names = []

    def test_started(self, className, methodName):
        self.class_names.append(className)
        self.method_names.append(methodName)
        self.run_count = self.run_count + 1

    def test_failed(self):
        self.failure_indices.append(self.run_count - 1)

    def teardown_broken(self):
        self.was_tear_down_broken = True

    def setup_broken(self):
        self.was_setup_broken = True

    def summary(self):
        sum = f"{self.run_count} run, {len(self.failure_indices)} failed"
        if self.was_setup_broken:
            sum = sum + ", SetUp was broken"
        if self.was_tear_down_broken:
            sum = sum + ", TearDown was broken"
        return sum

    def detail(self):
        det = ''
        for i in range(0, self.run_count):
            ret = ''
            if i in self.failure_indices:
                ret = 'failed'
            else:
                ret = 'pass'
            det = det + f"[{ret:^8}] {self.class_names[i]} > {self.method_names[i]}\n"
        return det;

class TestCase:
    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def teardown(self):
        pass

    def run(self, result):
        result.test_started(self.__class__.__name__, self.name)
        try:
            try:
                self.setup()
            except Exception as e:
                result.setup_broken()
                fmt = traceback.format_exc()
                print(f"{self.__class__.__name__} > {self.name}\n", fmt)
                raise

            method = getattr(self, self.name)
            method()

        except:
            result.test_failed()

        try:
            self.teardown()
        except Exception as e:
            result.teardown_broken()
            fmt = traceback.format_exc()
            print(f"{self.__class__.__name__} > {self.name}\n", fmt)
