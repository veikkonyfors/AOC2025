import pytest
import common
import day4

def test_grid():
    lines = common.read_input("input_test")
    grid = day4.Grid(lines)
    assert grid.to_string() == \
        "[['.', '.', '@', '@', '.', '@', '@', '@', '@', '.', '\\n'], ['@', '@', '@', '.', '@', '.', '@', '.', '@', "\
        "'@', '\\n'], ['@', '@', '@', '@', '@', '.', '@', '.', '@', '@', '\\n'], ['@', '.', '@', '@', '@', '@', '.', "\
        "'.', '@', '.', '\\n'], ['@', '@', '.', '@', '@', '@', '@', '.', '@', '@', '\\n'], ['.', '@', '@', '@', '@', "\
        "'@', '@', '@', '.', '@', '\\n'], ['.', '@', '.', '@', '.', '@', '.', '@', '@', '@', '\\n'], ['@', '.', '@', "\
        "'@', '@', '.', '@', '@', '@', '@', '\\n'], ['.', '@', '@', '@', '@', '@', '@', '@', '@', '.', '\\n'], ['@', "\
        "'.', '@', '.', '@', '@', '@', '.', '@', '.', '\\n']]"
    assert grid.count_adjacent_rolls(0,0) == 2
    assert grid.count_adjacent_rolls(1, 1) == 6
    assert grid.count_adjacent_rolls(9, 9) == 2
    assert  grid.count_accessible_rolls() == 13

    lines = common.read_input("input")
    grid = day4.Grid(lines)
    assert grid.count_accessible_rolls() == 1409
    
def test_day4():
    assert day4.day4("input_test") == 13
    assert day4.day4("input_test", 2) == 43
    assert day4.day4("input") == 1409
    assert day4.day4("input", 2) == 8366