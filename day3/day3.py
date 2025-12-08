import common
def get_max_joltage(bank: str):
    firstdigit = max(bank[0:len(bank) - 1])
    indexfirstdigit = bank.index(firstdigit)
    lastdigit = max(bank[indexfirstdigit + 1:])
    return int(firstdigit+lastdigit)

"""
Try finding max joltage by brute force. Works for test input.
Doomed to fail with actual input, too many combinations!
"""
def get_max_joltage2_bf(bank: str):
    from itertools import combinations
    bankdigits = len(bank)
    maxbank = 0

    for indices in combinations(range(bankdigits), 12):
        subbank = ''.join(bank[i] for i in indices)
        if int(subbank) > maxbank: maxbank = int(subbank)

    return int(maxbank)



def get_max_joltage2(bank):
    """
    Find the maximum k-digit number by selecting k digits from number_str
    while preserving their relative order.

    Time complexity: O(n) where n = len(number_str)
    """
    n = len(bank)
    if n < 12:
        return None

    stack = []
    to_remove = n - 12  # How many digits we need to remove

    for digit in bank:
        # While we can still remove digits and current digit is greater than last in stack
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    # If we didn't remove enough digits (in case of non-decreasing sequence)
    # Remove from the end
    result = ''.join(stack[:12])
    return int(result)

def get_total_joltage(banks: str, part = 1):
    total_joltage = 0
    for bank in banks:
        if part == 1: max_joltage = get_max_joltage(bank.rstrip())
        else: max_joltage = get_max_joltage2(bank.rstrip())
        #print(f"{bank}: {max_joltage}")
        total_joltage += max_joltage

    return total_joltage

def day3(input: str,part=1):
    banks = common.read_input(input)
    if part == 1: return get_total_joltage(banks)
    if part == 2: return get_total_joltage(banks, 2)

    #if part == 2: return addup_invalids2(lines)
    return -1

if __name__ == '__main__':
    print(f"{day3('input_test')}")
    print(f"{day3('input_test', 2)}")
    print(f"{day3('input')}")
    print(f"{day3('input', 2)}")


