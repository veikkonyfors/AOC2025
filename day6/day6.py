from common import read_input

class Day6():
    def __init__(self, input: str):
        self.lines = read_input(input)
        self.operands = []
        for line in self.lines[:-1]:
            numbers = list(map(int, line.split()))
            self.operands.append(numbers)

        self.operators = self.lines[-1].split()

        self.answers = []
        for ioperator, operator in enumerate(self.operators):
            answer = {'+': 0, '*': 1}[operator]
            for ioperand in range(len(self.operands)):
                answer = {
                    '+': answer + self.operands[ioperand][ioperator],
                    '*': answer * self.operands[ioperand][ioperator]
                }[operator]
            self.answers.append(answer)

    def get_grand_total(self, part=1):
        if part == 1:
            return sum(self.answers)
        if part == 2:
            return 2


if __name__ == '__main__':
    day6 = Day6("input_test")
    print(f"{day6.get_grand_total()}")
    print(f"{day6.get_grand_total(2)}")
    day6 = Day6("input")
    print(f"{day6.get_grand_total()}")
    print(f"{day6.get_grand_total(2)}")
