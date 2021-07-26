import math

def getDigit(num, index):
    digits = math.ceil(math.log10(num))

    if (index > digits):
        return -1

    place = abs(index + 1 - digits)

    return (num // 10 ** place) % 10

while True:
    numInput = int(input("num: "))
    indexInput = int(input("index: "))
    print(getDigit(numInput, indexInput))

def test():
    test1 = getDigit(12345, 2)
    test2 = getDigit(54321, 0)
    test3 = getDigit(349857345, 5)
    test4 = getDigit(10, 5)
    if (test1 == 3):
        print("pass")
    else: 
        print(test1)
    if (test2 == 5):
        print("pass")
    else: 
        print(test2)
    if (test3 == 7):
        print("pass")
    else: 
        print(test3)
    if (test4 == -1):
        print("pass")
    else: 
        print(getDigit(10, 5) )

test()
