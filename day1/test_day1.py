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

