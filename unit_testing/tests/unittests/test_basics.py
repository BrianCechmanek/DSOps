""" Unittest testing suite for basics """


import logging
import unittest
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

class TestBasicMethods(unittest.TestCase):

    def test_good_adder(self):
        x, y, eps = 40., 2.0, 1e-5
        res = good_adder(a=40., b=2.0)

        self.assertLessEqual(res, x+y+eps)
        self.assertGreaterEqual(res, x+y-eps)
        self.assertAlmostEqual(res, x+y+eps, places=3, msg=None, delta=None)
        logging.info("basic unittest, good_adder passed")

    def test_bad_adder(self):
        x, y, eps = 40., 2.0, 1e-5
        res = bad_adder(a=40., b=2.0)

        self.assertLessEqual(res, x+y+eps)
        self.assertGreaterEqual(res, x+y-eps)
        self.assertAlmostEqual(res, x+y+eps, places=3, msg=None, delta=None)
        logging.info("basic unittest, bad_adder passed")


if __name__ == 'unittest.__main__':
    unittest.main()