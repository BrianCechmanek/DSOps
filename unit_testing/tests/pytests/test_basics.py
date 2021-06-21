""" Pytest testing suite for basics. """

import logging
from pytest import approx
import sys

from src.basics import (good_adder,
                      bad_adder)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)


def test_good_adder(rel: float=1e-6):
    x,y,app = 40, 2, 42
    assert good_adder(x, y) == approx(app, rel=rel)

def test_bad_adder(rel: float=1e-6):
    x,y,app = 40, 2, 42
    assert bad_adder(x, y) == approx(app, rel=rel)