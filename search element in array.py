# Step 1: Read input
N, X = map(int, input().split())      # N = size of list, X = number to search
A = list(map(int, input().split()))   # Read N numbers into list A

# Step 2 & 3: Search for X
found = False
for num in A:
    if num == X:
        found = True
        break  # Stop searching once we find X

# Step 4: Output result
if found:
    print("YES")
else:
    print("NO")
