arr = [1, 2, 1, 5, 1]

largest = arr[0]
second_largest = arr[0]

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num < largest:
        second_largest = num

print(second_largest)
