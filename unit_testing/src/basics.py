""" Example driver program. """


import logging
import sys


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)


def good_adder(a: float, b:float):
    #logging.info("running my good adder")
    return a + b


def bad_adder(a: float, b: float):
    # this adder method will probably never fail
    # but will definitely produce unexpected results
    #logging.info("running my bad adder")
    return a + b + 1


if __name__ == "__main__":
    logger.info("starting run of basics")

    x, y = 40, 2
    print(f"adding {x} and {y}")
    print(f"good adder: {good_adder(x, y)}")
    print(f"bad adder: {bad_adder(x, y)}")

    logger.info("completed basics")