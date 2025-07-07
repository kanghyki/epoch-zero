#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./generate.sh <name>"
  exit 1
fi

NAME="$1"

if [ ! -f "${NAME}.py" ]; then
  touch "${NAME}.py"
  echo "Created: ${NAME}.py"
else
  echo "Skipped: ${NAME}.py already exists"
fi

if [ ! -f "plot_${NAME}.py" ]; then
  touch "plot_${NAME}.py"
  echo "Created: plot_${NAME}.py"
else
  echo "Skipped: plot_${NAME}.py already exists"
fi

if [ ! -f "test_${NAME}.py" ]; then
  cat <<EOF > "test_${NAME}.py"
from xunit import xunit
from ${NAME} import *

class TestClass(xunit.TestCase):
    def test_something(self):
        pass

result = xunit.TestResult()
suite = xunit.TestSuite()

suite.add(TestClass('test_something'))

suite.run(result)
print(result.detail())
print(result.summary())
EOF
  echo "Created: test_${NAME}.py"
else
  echo "Skipped: test_${NAME}.py already exists"
fi
