from common import read_stripped_input

class Day7():
    def __init__(self, input: str):
        self.lines = read_stripped_input(input)
        self.chartable = [list(line) for line in self.lines]



    def traverse_and_count(self):
        splits = 0
        for irow, row in enumerate(self.chartable[:-1]):
            for ic, c in enumerate(row):
                if c == 'S':
                    if self.chartable[irow + 1][ic] in ".S":  self.chartable[irow + 1][ic] = 'S' # Could have been switched to S by previous actions
                    else:
                        self.chartable[irow + 1][ic - 1] = 'S'
                        self.chartable[irow + 1][ic + 1] = 'S'
                        splits += 1

        return splits

if __name__ == '__main__':
    day7 = Day7("input_test")
    count = day7.traverse_and_count()
    print(f"{count}")
    day7 = Day7("input")
    count = day7.traverse_and_count()
    print(f"{count}")

