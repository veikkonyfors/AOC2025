from typing import List

from common import read_input


class Fresh():

  def __init__(self, fresh_lines: List[str]):

    self.fresh_set = set()

    for line in fresh_lines:
      start, end = line.split('-')
      #print(start, end)
      if int(start) <= int(end): # Skip start > end ranges
        #print(f"add: start: {start}, end: {end}")
        self.fresh_set.add((int(start),int(end)))
        #print(f"fresh_set in if: {self.fresh_set}")
        self.fresh_list = list(self.fresh_set)
        #print(f"fresh_list: {self.fresh_list}")

    #print(f"fresh_set after init: {self.fresh_set}")

  def __str__(self):
      # Järjestetään setti listaksi ennen tulostusta, jotta se on luettava
      sorted_list = sorted(list(self.fresh_set))
      return f"Fresh(numbers={sorted_list})"

  def to_string(self):
    return str(self.fresh_set)

  def count_fresh_ids(self, available_ids):
    freshones = 0
    for id in available_ids:
      #print(f"id: {id}")
      for ifresh in self.fresh_set:
        #print(f"ifresh: {ifresh}")
        if ifresh[0] <= id <= ifresh[1]:
          freshones += 1
          break
        #print (f"freshones: {freshones}")

    return freshones

  def count_fresh_ids2(self):
    print(f"In: count_fresh_ids2")
    freshones = 0
    print(f"len(self.fresh_set): {len(self.fresh_set)}")
    if len(self.fresh_set) > 1:
      print(f"In: if len(self.fresh_set) > 1:")
      for i, (start, end) in enumerate(self.fresh_list[:-1]):
        # if either is inside the other, remove insider
        # latter inside previous
        if start <= self.fresh_list[i+1][0] and end >= self.fresh_list[i+1][0]:
          #del self.fresh_set[i]
          self.fresh_list.remove(i+1)
        # former inside latter
        elif start >= self.fresh_list[i+1][0] and end <= self.fresh_list[i+1][0]:
          #del self.fresh_set[i+1]
          self.fresh_list.remove(i)

    for r in self.fresh_set:
      freshones += r[1] - r[0] + 1

    return freshones


def day5(input: str, part=1):
    lines = read_input(input)
    idx = lines.index("\n")
    fresh_lines = lines[:idx]
    available_lines = lines[idx+1:]
    available_ids = [int(line) for line in available_lines]

    if part == 1:
      fresh = Fresh(fresh_lines)
      return fresh.count_fresh_ids(available_ids)

    if part == 2:
      fresh = Fresh(fresh_lines, 2)
      return fresh.count_fresh_ids2()


if __name__ == '__main__':
    print(f"{day5('input_test')}")
    print(f"{day5('input')}")
    #print(f"{day4('input_test', 2)}")
    #print(f"{day4('input')}")
    #print(f"{day4('input', 2)}")