# Integer Index

This is a small project, but an interesting problem to solve.

I wanted to figure out how to index an integer without converting the number into another type. 
It seemed simple on the outside, but turned out to be a bit more interesting.

## How It Works

I knew that any number `% 10` would give me the last digit of any number.

```
1234 % 10 == 4
45678 % 10 == 8
2 % 10 == 2
```

Using this, I could divide the number by 10 over and over, then use `% 10` to get the digit

```
# Extract the 3rd Digit:
12345 // 10 == 1234
1234 // 10 == 123
123 % 10 == 3

# Extract the 1st Digit:
3496 // 10 == 349
349 // 10 == 34
34 // 10 == 3
3 % 10 == 3
```

The problem is that dividing by 10, as shown above, goes from right to left, where index goes from left to right.
Because of this, I need a way to invert the index to how many times I want to divide by 10.
I can do this by taking the absolute value of the index provided plus 1, minus the amount of digits in the number.
(The number of digits is found by taking the ceiling of log10(n))

```
# Example: Get number of times to divide by 10 to get the first digit
num = 12345
index = 0

digits = math.ceil(math.log10(num)) # digits == 5

place = abs(index + 1 - digits) # place == 4
```

Now that we have how many times we must divide by ten, we can get the digit we want!
Here’s a few of my test cases written out to show the process step by step:

Test 1: Expecting 3
```
num = 12345
index = 2

digits = math.ceil(math.log10(num)) # digits == 5, math.ceil(math.log10(12345))

if (index > digits): # if (2 > 5) 
    return -1 # not reached

times_to_divide = abs(index + 1 - digits) # times_to_divide == 2, abs(2 + 1 - 5)

return (num // 10 ** times_to_divide) % 10 # return 3, return (12345 // 10 ** 2) % 10
```

Test 2: Expecting 5
```
num = 54321
index = 0

digits = math.ceil(math.log10(num)) # digits == 5, math.ceil(math.log10(54321))

if (index > digits): # if (0 > 5) 
    return -1 # not reached

times_to_divide = abs(index + 1 - digits) # times_to_divide == 4, abs(0 + 1 - 5)

return (num // 10 ** times_to_divide) % 10 # return 5, return (54321 // 10 ** 4) % 10
```

Test 3: Expecting 7
```
num = 349857345
index = 5

digits = math.ceil(math.log10(num)) # digits == 9, math.ceil(math.log10(349857345))

if (index > digits): # if (5 > 9) 
    return -1 # not reached

times_to_divide = abs(index + 1 - digits) # times_to_divide == 3, abs(5 + 1 - 9)

return (num // 10 ** times_to_divide) % 10 # return 7, return (349857345 // 10 ** 3) % 10
```

Test 4: Expecting -1
```
num = 10
index = 5

digits = math.ceil(math.log10(num)) # digits == 2, math.ceil(math.log10(10))

if (index > digits): # if (5 > 2) 
    return -1 # reached
```
