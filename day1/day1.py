import common
import re


def turn(dial, lrnn):
    regex_pattern = r"([A-Za-z])(\d*)"
    match = re.match(regex_pattern, lrnn)

    if match:
        lr = match.group(1)
        number = int(match.group(2))
        number = -number if lr == 'L' else number
        newdial = (dial + number) % 100

        return newdial
def day1(lines,startdial):

    dial = startdial
    zeroes = 0

    for lrnn in lines:
        dial = turn(dial, lrnn)
        #print(f"{lrnn.rstrip()}, {dial}")
        if dial == 0: zeroes += 1

    return zeroes


if __name__ == '__main__':
    lines = common.read_input("input_test")
    print(f"{day1(lines, 50)}")
    lines = common.read_input("input")
    print(f"{day1(lines, 50)}")
