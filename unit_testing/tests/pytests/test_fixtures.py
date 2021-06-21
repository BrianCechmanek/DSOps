""" More advanced pytest, via fixtures """

import logging
import pytest

import sys

from src.basics import good_adder, bad_adder


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)


@pytest.fixture
def add_ints():
    return (40, 2)


@pytest.fixture
def add_floats():
    return (0.1, 0.2)


@pytest.fixture
def int_result():
    return 42


@pytest.fixture
def float_result():
    # let's make an example of why to check within epsilon
    # try 0.30000000000000009 . or 3.0
    return 0.30000000000000004


def test_good_adder(add_ints, add_floats, int_result, float_result):
    assert good_adder(*add_ints) == int_result
    assert good_adder(*add_floats) == float_result
    logging.info("good adder passed fixtures")


def test_bad_adder(add_ints, add_floats, int_result, float_result):
    assert bad_adder(*add_ints) == int_result
    assert bad_adder(*add_floats) == float_result
    logging.info("bad adder passed fixtures")


### How does this extend to a LOT of checks?


@pytest.fixture
def add_many_ints():
    return zip(range(10), range(10)[::-1])


def test_good_adder_alot(add_many_ints):
    for x, y in add_many_ints:
        assert good_adder(x, y) == x + y