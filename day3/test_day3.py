import pytest

import day3
def test_get_max_joltage():
    assert day3.get_max_joltage("987654321111111") == 98
    assert day3.get_max_joltage("811111111111119") == 89
    assert day3.get_max_joltage("234234234234278") == 78
    assert day3.get_max_joltage("818181911112111") == 92

def test_get_max_joltage2():
    assert day3.get_max_joltage2("987654321111111") == 987654321111
    assert day3.get_max_joltage2("811111111111119") == 811111111119
    assert day3.get_max_joltage2("234234234234278") == 434234234278
    assert day3.get_max_joltage2("818181911112111") == 888911112111
def test_day3():
    assert day3.day3("input_test") == 357
    assert day3.day3("input_test", 2) == 3121910778619
    assert day3.day3("input") == 17524
    assert day3.day3("input", 2) == 173848577117276