# Unit Testing for DS, ML, & AI Research  

Tutorial on Pytest for ML Research. 

Presented for [NeuroCog Computing Lab](https://cs.uwaterloo.ca/~jorchard/uw/NeuroCog.html), 23 June 2021 

Presenters: Evengalia Kryoneriti, Brian Cechmanek

Time: 10-12 minutes including questions

# Why to (Unit) Test

Skip this if you're familiar with they whys of (unit) testing. 

Unit testing allows you to:

* organise expectations (!) 
* catch unexpected behaviour
* catch expected behaviour 

Organising expectations is setting out with a plan for what your function is meant to do. What are the inputs and outputs going to be? Will you accept variable input types? Should your output always be signed, within some range, or some particular data type? 

Catching unexpected behaviour is the obvious goal of testing. Once you know what your function should do, you'll want it to avoid providing incorrect outputs. But it is absolutely pragmatic to check that incorrect outputs don't slip though (though, of course it is impracticable to think of and implement all possible edge cases). If you are parsing a standard +1 10-digit phone number, and it contains a letter, this should be captured. 

Lastly, catching expected behaviour will hopefully follow. Does your method output what you organised ahead of time? If you are parsing a +1 10-digit phone number, do you output a `str`, or an `int`? 

If the distinction between catching unexpected behaviour versus expected is unclear, consider your TP/FP/TN/FN situations. 

For DS, ML, and AI, the only addition to this mental model is that you are now testing with ideas of probability, uncertainty, and often massive data inputs. 


# When to Test (and TDD)

In the planning of your development, testing can help set a roadmap. If you know where you want to end up (a fully passing test suite), you can work your way back through implementing each class/function. 

In the running of your scripts/programs, testing can help you with be confident that things are executing accurately/correctly. 

In updating your code, pre-existing tests can help ensure that no breaking changes occur. 

This has lead to a popular process called [Test Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development).

# Unittest

Unittest is python's [built-in tesing library](https://docs.python.org/3/library/unittest.html#module-unittest). I do not know of any scale usage of unittest, over pytest (below). That said, it does have a couple noteable pros: 

* guaranteed available as part of Python standard library
* Flexible test-case execution: run arbitrary sets of tests

## Example cases

see: `/unit_testing/src/basics.py`,  `/unit_testing/tests/unittest/test_basics.py`  

Here a "good" adder method and a "bad" adder method are created. Both will run and return a summation - and more importantly, it is extremely unlikely that either method will ever lead to the program crashing. 

```
/unit_testing/src/ $ python basics.py
adding 40 and 2
2021-06-20 13:39:16,303 - root - INFO - running my good adder
good adder: 42
bad adder: 43
2021-06-20 13:39:16,303 - root - INFO - completed basics
```

This code logic is tested for by asserting that logic outputs as expected for one or more example cases. 

```bash
/unit_testing/src/ $ python -m unittest tests/unittests/test_basics.py
...
======================================================================
FAIL: test_bad_adder (test_basics.TestBasicMethods)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../test_basics.py", line 34, in test_bad_adder
    self.assertLessEqual(res, x+y+eps)
AssertionError: 43.0 not less than or equal to 42.00001

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

# Pytest 

[Pytest](https://docs.pytest.org/en/6.2.x/) is a testing standard for Python. Compared to unittest, it provides:

* simpler test writing syntax
* in general, shorter test suites
* Fixtures, which allow for easier, more comprehensive values testing (.e.g test many values into a calculation function)
* built-in logging 
* test discovery (will find all of your test files within your project)

## Example cases

see: `/unit_testing/src/basics.py`, `/unit_testng/tests/pytests/test_basics.py`  

Here a "good" adder method and a "bad" adder method are created. Both will run and return a summation - and more importantly, it is extremely unlikely that either method will ever lead to the program crashing. 

```
/unit_testing/src/ $ python basics.py
adding 40 and 2
2021-06-20 13:39:16,303 - root - INFO - running my good adder
good adder: 42
bad adder: 43
2021-06-20 13:39:16,303 - root - INFO - completed basics
```

This code logic is tested for by asserting that logic outputs as expected for one or more example cases. 

```bash
# calling `python -m pytest` is required to have src be in python path
# if you call `pytest tests/pytests/test_basics.py you will get an import error
/unit_testing/src/unittest/ $ python -m pytest tests/pytests/test_basics.py 
...
============================================================================= test session starts ==============================================================================
platform darwin -- Python 3.9.2, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/u6070354/Desktop/Brian/research/thesis/DSOps/unit_testing
collected 3 items                                                                                                                                                              

tests/pytests/test_fixtures.py .F.                                                                                                                                       [100%]

=================================================================================== FAILURES ===================================================================================
________________________________________________________________________________ test_bad_adder ________________________________________________________________________________

add_ints = (40, 2), add_floats = (0.1, 0.2), int_result = 42, float_result = 0.30000000000000004

    def test_bad_adder(add_ints, add_floats, int_result, float_result):
>       assert bad_adder(*add_ints) == int_result
E       assert 43 == 42
E        +  where 43 = bad_adder(*(40, 2))

tests/pytests/test_fixtures.py:51: AssertionError
=========================================================================== short test summary info ============================================================================
FAILED tests/pytests/test_fixtures.py::test_bad_adder - assert 43 == 42
========================================================================= 1 failed, 2 passed in 0.11s ==========================================================================
```

## Fixtures 

The real power of pytest (not to suggest unittest doesn't have, see [setup](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp)).

Consider the four (Pytest) stages of a test:

1. Arrange: preparation for the test 
2. Act: singular change of state, the event to test
3. Assert: looking at the result of the state change
4. Cleanup: ensure that other tests aren't influenced by this one

Fixture primarily work on (1): arranging for a test. Test functions request fixtures by declaring them as arguments. Consider a fixture a function that returns some data. Fixtures can:

* Request other fixtures
* Be reused in multiple tests
* Can be requested more than once per test

Readdressing testing the adders in `src/basics.py`, how would it make sense to pass in many values, and to test for various situations? Consider to test both floats and ints:

```python
def test_good_adder():
    x, y = 40, 2
    z, w = 0.1, 0.3
    assert good_adder(x,y) == 42
    assert good_adder(z,w) == 0.3

def test_badadder():
    x, y = 40, 2
    z, w = 0.1, 0.3
    assert bad_adder(x,y) == 42
    assert bad_adder(z,w) == 0.3
```

In standard DYR style, it would be nice to move these variables outside of the individual tests. Which can be done by defining a fixture:

```python
@pytest.fixture
def add_ints():
    return (40, 2)
...
```

Each fixture is then _requested_ by the test method:

```python
def test_good_adder(add_ints, ...):
    ...
```

# Conclusion 

This just brushes the surface of testing, but for many logic/implementation situations, will likely help you cover your bases. The next step would be for more complicated setups, when you may wish to pass a class around.






