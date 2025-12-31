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

    def get_grand_total(self):
            return sum(self.answers)

class Day6_2():
    def __init__(self, input: str):
        self.lines = read_input(input)
        self.operators = self.lines[-1]
        self.ioperstart = [i for i, c in enumerate(self.operators) if c in "+*"]

        self.numbers = []
        self.ndigits = len(self.lines) - 1
        for ic, c in enumerate(self.lines[0]):
            number = ""
            for i in range(len(self.lines) - 1):
                digit = self.lines[i][ic]

                if digit.isdigit():
                    number += digit
            self.numbers.append(number)

        self.answers = []
        inumber = 0

        for operator in self.operators.split():
            answer = {'+': 0, '*': 1}[operator]
            while True:
                if self.numbers[inumber].isdecimal():
                    answer = {
                        '+': answer + int(self.numbers[inumber]),
                        '*': answer * int(self.numbers[inumber])
                    }[operator]
                inumber += 1
                if inumber >= len(self.numbers): break
                if self.numbers[inumber] == '': break

            self.answers.append(answer)

    def get_grand_total(self):
        return sum(self.answers)






if __name__ == '__main__':
    day6 = Day6("input_test")
    print(f"{day6.get_grand_total()}")
    day6 = Day6("input")
    print(f"{day6.get_grand_total()}")
    day6_2 = Day6_2("input_test")
    print(f"{day6_2.get_grand_total()}")
    day6_2 = Day6_2("input")
    print(f"{day6_2.get_grand_total()}")
