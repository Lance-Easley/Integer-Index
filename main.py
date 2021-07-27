import math

def getDigit(num, index):
    # Get number of digits in num
    digits = math.ceil(math.log10(num))

    # Throw -1 if index is out of bounds
    if (index > digits):
        return -1

    # Invert index to number of places to divide off
    times_to_divide = abs(index + 1 - digits)

    # Divide and return
    return (num // 10 ** times_to_divide) % 10

# Trial code
while True:
    numInput = int(input("num: "))
    indexInput = int(input("index: "))
    print(getDigit(numInput, indexInput))

# Test code
def test():
    test1 = getDigit(12345, 2)
    test2 = getDigit(54321, 0)
    test3 = getDigit(349857345, 5)
    test4 = getDigit(10, 5)
    assert test1 == 3
    assert test2 == 5
    assert test3 == 7
    assert test4 == -1

test()
