"""Test name-matching regular expression."""
import re

import pytest


# vvv ADD YOUR PATTERN HERE vvv #
pattern = r"[(][?]{0,1}[^:.<=!]{2}[^()]*[)]"
# ^^^ ADD YOUR PATTERN HERE ^^^ #
#raise NotImplementedError("Add your pattern to the test file.")


def my_func(pattern, string):
    lst = []
    iter = re.finditer(pattern, string)
    for i in iter:
        lst.append(i.group(0))
    return lst


test_cases= [
('''(?:[ˆ@]+.[ˆ@]+)@(?p<name>[ˆ@]+)''', ['(?p<name>[ˆ@]+)']),
('''(?<=te(st|ch))''', ['(st|ch)']),
('''([ˆ@]+)@(?:[ˆ@]+.[ˆ@]+)''',['([ˆ@]+)']),
('''geeks(?=[a-z])''', []),
('''(?P<first_name>\w+) (?P<last_name>\w+)(?!\D{3,4})''', ['(?P<first_name>\w+)','(?P<last_name>\w+)']), #test cases with 2 example
('''(?<=te(st|ch))''', ['(st|ch)'])
]


@pytest.mark.parametrize("string,matches", test_cases)
def test_finding_gerand(string, matches):
    """Test whether pattern correctly matches or does not match input."""
    assert (my_func(pattern, string)) == matches



