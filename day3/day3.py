import common
def get_max_joltage(banks: str):
    firstdigit = max(banks[0:len(banks) - 1])
    indexfirstdigit = banks.index(firstdigit)
    lastdigit = max(banks[indexfirstdigit+1:])
    return int(firstdigit+lastdigit)

def get_total_joltage(banks: str):
    total_joltage = 0
    for bank in banks:
        max_joltage = get_max_joltage(bank.rstrip())
        total_joltage += max_joltage

    return total_joltage

def day3(input: str,part=1):
    banks = common.read_input(input)
    if part == 1: return get_total_joltage(banks)

    #if part == 2: return addup_invalids2(lines)
    return -1

if __name__ == '__main__':
    print(f"{day3('input_test')}")
    print(f"{day3('input')}")


