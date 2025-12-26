from typing import List

from common import read_input


class Fresh():

  def __init__(self, fresh_lines: List[str]):

    self.fresh_set = set()

    for line in fresh_lines:
      start, end = line.split('-')
      if int(start) <= int(end): # Skip start > end ranges
        self.fresh_set.add((int(start),int(end)))

    self.fresh_list = list(self.fresh_set)

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
      if not self.fresh_list:
          return 0

      self.fresh_list.sort(key=lambda x: x[0])

      merged = [self.fresh_list[0]]

      for current in self.fresh_list[1:]:
          prev_start, prev_end = merged[-1]
          current_start, current_end = current

          if current_start <= prev_end:
              merged[-1] = (prev_start, max(prev_end, current_end))
          else:
              merged.append(current)

      freshones = 0
      for r in merged:
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
      fresh = Fresh(fresh_lines)
      return fresh.count_fresh_ids2()


if __name__ == '__main__':
    print(f"{day5('input_test')}")
    print(f"{day5('input')}")
    print(f"{day5('input_test', 2)}")
    print(f"{day5('input', 2)}")
