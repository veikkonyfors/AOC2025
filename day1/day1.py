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


def day1(lines,startdial,puzz=1):

    dial = startdial
    zeroes = 0

    for lrnn in lines:

        if puzz == 2:
            fullrounds = int(lrnn[1:]) // 100
            zeroes += fullrounds
            remainder = int(lrnn[1:]) % 100
            if lrnn[0] == "L" and dial != 0:
                zeroes += 1 if dial - int(remainder) < 0 else 0
            if lrnn[0] == "R" and dial != 0:
                zeroes += 1 if dial + int(remainder) > 100 else 0

        dial = turn(dial, lrnn)
        if dial == 0: zeroes += 1
        #print(f"{lrnn.rstrip()}, {dial}, {zeroes}")

    return zeroes


if __name__ == '__main__':
    lines = common.read_input("input_test")
    print(f"{day1(lines, 50)}")
    print(f"{day1(lines, 50, 2)}")
    lines = common.read_input("input")
    print(f"{day1(lines, 50)}")
    print(f"{day1(lines, 50, 2)}")
