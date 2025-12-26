import pytest
from typing import List

import day5
from common import read_input

@pytest.fixture(scope="session")
def parsed_lines():
  lines = read_input("input_test")
  idx = lines.index("\n")
  fresh_lines = lines[:idx]
  available_lines = lines[idx + 1:]
  available_ids = [int(line) for line in available_lines]
  return lines, fresh_lines, available_lines, available_ids

# pytest fixtures used due part1 was done in colab, which allowed parameters to be passed for disctinct tests.
# And in Colab I drifted to paraneterized tests as didn't know they don't work in pycharm.
# In pycharm, parameter has to be a fixture.
@pytest.fixture
def lines(parsed_lines):
    return parsed_lines[0]
@pytest.fixture
def fresh_lines(parsed_lines):
    return parsed_lines[1]

@pytest.fixture
def available_ids(parsed_lines):
    return parsed_lines[3]


def test_count_fresh_ids2(fresh_lines: List[str]):

  fresh = day5.Fresh(["3-5", "10-14", "11-13"]) #
  assert fresh.count_fresh_ids2() == 8

  fresh = day5.Fresh(["3-5", "10-14", "16-20", "12-18"]) #
  assert fresh.count_fresh_ids2() == 14

  fresh = day5.Fresh(fresh_lines)
  assert fresh.count_fresh_ids2() == 14

  fresh = day5.Fresh(["110940853542246-11840832133943"]) # 110940853542246-11840832133943 = 99100021408303
  assert fresh.count_fresh_ids2() == 0

  fresh = day5.Fresh(["3-5"]) #
  assert fresh.count_fresh_ids2() == 3

  fresh = day5.Fresh(["3-5", "10-14"]) #
  assert fresh.count_fresh_ids2() == 8




def test_fresh(fresh_lines: List[str], available_ids):

  fresh = day5.Fresh(fresh_lines)
  #print(repr(f"fresh: {sorted(fresh.fresh_set)}"))
  assert sorted(fresh.fresh_set) == [(3, 5), (10, 14), (12, 18), (16, 20)]

  fresh = day5.Fresh(["110940853542246-11840832133943"])
  #print(repr(f"fresh: {fresh.fresh_set}"))
  assert fresh.fresh_set == set()

  fresh = day5.Fresh(["213205509444883-217326119178383"])
  #print(repr(f"fresh: {fresh.fresh_set}"))
  assert fresh.fresh_set == {(213205509444883, 217326119178383)}

  fresh = day5.Fresh(fresh_lines)
  count = fresh.count_fresh_ids(available_ids)
  print(repr(f"count: {count}"))
  assert count == 3

  lines = read_input("input")
  idx = lines.index("\n")
  fresh_lines = lines[:idx]
  available_lines = lines[idx+1:]
  available_ids = [int(line) for line in available_lines]
  fresh = day5.Fresh(fresh_lines)
  count = fresh.count_fresh_ids(available_ids)
  print(repr(f"count: {count}"))
  assert count == 623


def test_ingredients(lines: List[str]):
  #print(f"{lines}")
  assert lines  == ['3-5\n', '10-14\n', '16-20\n', '12-18\n', '\n', '1\n', '5\n', '8\n', '11\n', '17\n', '32\n']

  idx = lines.index("\n")
  fresh = lines[:idx]
  available = lines[idx+1:]

  assert fresh == ['3-5\n', '10-14\n', '16-20\n', '12-18\n']
  assert available == ['1\n', '5\n', '8\n', '11\n', '17\n', '32\n']

if __name__ == '__main__':
  print("Run all day5 tests")
