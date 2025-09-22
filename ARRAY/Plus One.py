def plusOne(digit):
    for i in range(len(digit) - 1, -1, -1):
        if digit[i] == 9:   # <-- use == for comparison
            digit[i] = 0
        else:
            digit[i] = digit[i] + 1
            return digit
    return [1] + digit
