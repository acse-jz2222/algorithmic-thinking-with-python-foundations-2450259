import random


def binary_search(data, target):
    left, right = 0, len(data) - 1

    mid = (left + right) // 2

    while mid > left:
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid
        else:
            right = mid
        mid = (left + right) // 2

    return -1


n = 10
max_val = 100
data = [random.randint(1, max_val) for i in range(n)]
data.sort()
print("Data:", data)
target = int(input("Enter target value: "))
target_pos = binary_search(data, target)
if target_pos == -1:
    print("Your target value is not in the list.")
else:
    print("You target value has been found at index", target_pos)
