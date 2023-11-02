from django.test import SimpleTestCase

from app import utils


class RemoveDuplicateTest(SimpleTestCase):
    def test_distinct_str_input_none(self):
        input = None
        expect = ''
        actual = utils.distinct_str(input)
        self.assertEqual(actual, expect)

    def test_distinct_str_input_blank_return_empty(self):
        input = '    '
        expect = ''
        actual = utils.distinct_str(input)
        self.assertEqual(actual, expect)

    def test_distinct_str(self):
        input = 'aabbcddcacbcd'
        expect = 'abcd'
        actual = utils.distinct_str(input)
        self.assertEqual(actual, expect)

    def test_distinct_str_has_space(self):
        input = 'aa bbcd dcacbcd'
        expect = 'abcd'
        actual = utils.distinct_str(input)
        self.assertEqual(actual, expect)
