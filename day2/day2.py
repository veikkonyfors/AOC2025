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

    def get_invalids(self):
        invalids = []

        for i in range(int(self.start), int(self.end)+1):
            s = str(i)
            mid = len(s) // 2
            firsthalf = s[0:mid]
            secondhalf = s[mid:]
            if firsthalf == secondhalf: invalids.append(int(s))

        return invalids

    def to_string(self):
        return self.start + "-" + self.end

def addup_invalids(lines):
    ranges = get_ranges(lines)
    addup = 0
    for range in ranges:
        idrange = IdRange(range)
        invalids = idrange.get_invalids()
        addup += sum(invalids)

    return addup


if __name__ == '__main__':
    lines = common.read_input("input_test")


