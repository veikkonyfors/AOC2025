import pytest
import day1

def test_turnok():
    assert day1.turn(1, "L2") == 99
    assert day1.turn(1, "L101") == 0
    assert day1.turn(26, "L101") == 25
    assert day1.turn(43, "L743") == 0
    assert day1.turn(1, "L99") == 2
    assert day1.turn(1, "L1") == 0
    assert day1.turn(99, "R2") == 1

def test_day1():
    assert day1.day1(["L743"], 43, 2) == 8
    assert day1.day1(["r4"], 96, 2) == 1
    assert day1.day1(["L5"], 0, 2) == 0
    assert day1.day1(["L1"],1) == 1
    assert day1.day1(["L701"], 2, 2) == 8


