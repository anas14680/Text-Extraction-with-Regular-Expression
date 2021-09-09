"""Test name-matching regular expression."""
import re

import pytest


# vvv ADD YOUR PATTERN HERE vvv #
pattern = r"\b[a-z]*([aeiou]|y[^aeiouy])[a-z]*ing\b"
# ^^^ ADD YOUR PATTERN HERE ^^^ #
#raise NotImplementedError("Add your pattern to the test file.")


def my_func(pattern, string):
    lst = []
    for i in re.finditer(pattern, string):
        lst.append(i.group(0))
    return lst


test_cases = [
("Harry sings while showering", ['showering']),
("Harry is singing", ['singing']),
("Harry loves to sing.", []),
("Harry is singing and showering at the same time.", ['singing','showering']),
("Oliver is struggling, but she is not giving up.", ['struggling','giving'])
]


@pytest.mark.parametrize("string,matches", test_cases)
def test_finding_gerand(string, matches):
    """Test whether pattern correctly matches or does not match input."""
    assert (my_func(pattern, string)) == matches

