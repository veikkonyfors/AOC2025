import re

import common


def get_ranges(lines):
    ranges = []
    oneline = ""

    for line in lines:
        oneline += line.rstrip()

    ranges = oneline.split(',')

    return ranges


class IdRange:
    def __init__(self, range):
        self.start = range.split('-')[0]
        self.end = range.split('-')[1]

    def is_invalid1(self, i: int):
        s = str(i)
        mid = len(s) // 2
        firsthalf = s[0:mid]
        secondhalf = s[mid:]
        if firsthalf == secondhalf: return True
        return False

    def is_invalid2(self, i: int):
        s = str(i)
        match = re.match(r'^(.+?)\1+$', s)
        if match:
            #print(f"match:{match.group(1)}")
            return True

        return False

    def get_invalids1(self):
        invalids = []

        for i in range(int(self.start), int(self.end)+1):
            if self.is_invalid1(i): invalids.append(i)

        return invalids

    def get_invalids2(self):
        invalids = []

        for i in range(int(self.start), int(self.end)+1):
            if self.is_invalid2(i): invalids.append(i)

        return invalids

    def to_string(self):
        return self.start + "-" + self.end

def addup_invalids1(lines):
    ranges = get_ranges(lines)
    addup = 0
    for range in ranges:
        idrange = IdRange(range)
        invalids = idrange.get_invalids1()
        addup += sum(invalids)

    return addup

def addup_invalids2(lines):
    ranges = get_ranges(lines)
    addup = 0
    for range in ranges:
        idrange = IdRange(range)
        invalids = idrange.get_invalids2()
        addup += sum(invalids)

    return addup

def day2(lines,part=1):
    if part == 1: return addup_invalids1(lines)
    if part == 2: return addup_invalids2(lines)
    return -1



if __name__ == '__main__':
    lines = common.read_input("input_test")
    print(f"{day2(lines)}")
    print(f"{day2(lines,2)}")
    lines = common.read_input("input")
    print(f"{day2(lines)}")
    print(f"{day2(lines,2)}")


