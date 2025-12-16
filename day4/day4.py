import common
from typing import List


class Grid:

    def __init__(self, lines: List[str]):
        self.grid = [list(line) for line in lines]

    def to_string(self):
        return str(self.grid)

    def count_adjacent_rolls(self, row, col):

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        count = 0

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0]):
                if self.grid[new_row][new_col] == "@":
                    count += 1

        return count

    def count_accessible_rolls(self, remove=False):
        count = 0
        for ir, row in enumerate(self.grid):
            for ic, col in enumerate(row):
                if col == "@":
                    adjacent_rolls = self.count_adjacent_rolls(ir, ic)
                    if adjacent_rolls < 4:
                        count += 1
                        if remove: self.grid[ir][ic] = "x"

        return count

    def remove_rolls(self):
        removed = 0

        while True:
            count = self.count_accessible_rolls(True)
            if count > 0: removed += count
            else: break

        return removed




def day4(input: str, part=1):
    lines = common.read_input(input)
    grid = Grid(lines)
    if part == 1: return grid.count_accessible_rolls()
    if part == 2: return grid.remove_rolls()

    return -1


if __name__ == '__main__':
    print(f"{day4('input_test')}")
    print(f"{day4('input_test', 2)}")
    print(f"{day4('input')}")
    print(f"{day4('input', 2)}")
