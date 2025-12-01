def palindrome_array(arr):
    for num in arr:
        s = str(num)
        if s != s[::-1]:  # check if string is not equal to its reverse
            return False
    return True