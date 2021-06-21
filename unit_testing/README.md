# Testing for ML Research

Tutorial on Pytest for ML Research. 

Presented for [NeuroCog Computing Lab](https://cs.uwaterloo.ca/~jorchard/uw/NeuroCog.html), 23 June 2021. 

Presenters: Evengalia Kryoneriti, Brian Cechmanek


# Outline


# Why to Test

# When to Test 

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
good adder: 43
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
good adder: 43
2021-06-20 13:39:16,303 - root - INFO - completed basics
```

This code logic is tested for by asserting that logic outputs as expected for one or more example cases. 

```bash
# calling `python -m pytest` is required to have src be in python path
# if you call `pytest tests/pytests/test_basics.py you will get an import error
/unit_testing/src/unittest/ $ python -m pytest tests/pytests/test_basics.py 
...
======================================================================== test session starts ========================================================================
platform darwin -- Python 3.9.2, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/u6070354/Desktop/Brian/research/thesis/tutorials/unit_testing
collected 2 items                                                                                                                                                   

tests/pytests/test_basics.py .F                                                                                                                               [100%]

============================================================================= FAILURES ==============================================================================
__________________________________________________________________________ test_bad_adder ___________________________________________________________________________

rel = 1e-06

    def test_bad_adder(rel: float=1e-6):
        x,y,app = 40, 2, 42
>       assert bad_adder(x, y) == approx(app, rel=rel)
E       assert 43 == 42 ± 4.2e-05
E        +  where 43 = bad_adder(40, 2)
E        +  and   42 ± 4.2e-05 = approx(42, rel=1e-06)

tests/pytests/test_basics.py:28: AssertionError
====================================================================== short test summary info ======================================================================
FAILED tests/pytests/test_basics.py::test_bad_adder - assert 43 == 42 ± 4.2e-05
==================================================================== 1 failed, 1 passed in 0.14s ====================================================================
```

## Fixtures 

The real power of pytest. 

