""" Integration Test Runner"""

import logging
import pytest

import sys

# from src.app import ()
# from src.process import ()
# from src.train import ()
# from src.validate import ()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)


def unit_test_1():
    raise NotImplementedError


def unit_test_2():
    raise NotImplementedError


# can run pytest -m "not integtest" for only the unit tests, pytest -m integtest
@pytest.mark.integtest
def integration_test():
    raise NotImplementedError
