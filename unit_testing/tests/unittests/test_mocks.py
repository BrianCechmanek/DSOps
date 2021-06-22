""" Unittest testing suite for mocks """


import logging
import unittest
import sys

from datetime import datetime
from src.mocks import Calendar
from unittest.mock import Mock

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

class TestCalendars(unittest.TestCase):

    def test_is_weekday(self):
        calendar = Calendar()
        # Mock datetime to control today's date
        date = Mock()

        # Mock .today() to return Monday (0)
        date.day.return_value = 0
        # Test Monday is a weekday
        assert calendar.is_weekday(date)
        # Mock .today() to return Saturday
        date.day.return_value = 5
        # Test Saturday is not a weekday
        assert not calendar.is_weekday(date)
        logging.info("mocks unittest, is_weekday passed")


    def test_is_leap_year(self):
        calendar = Calendar()
        date = Mock()

        date.year.side_effect = [2000, 2013, '2222']
        assert calendar.is_leap_year(date)
        assert not calendar.is_leap_year(date)
        with self.assertRaises(TypeError) as context:
            calendar.is_leap_year(date)
        self.assertTrue('not integer' in str(context.exception))

if __name__ == 'unittest.__main__':
    unittest.main()


