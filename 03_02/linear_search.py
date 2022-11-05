def linear_search(data, target):
    # n = len(data)
    # found = -1

    # for i in range(n):
    #     if data[i] == target:
    #         found = 1
    #         return i

    # return found
    # use enumerate
    for idx, val in enumerate(data):
        if val == target:
            return idx
    return -1


data = [4, 5, 2, 7, 1, 8]
target = 1
result = linear_search(data, target)
if result == -1:
    print("Item not found.")
else:
    print(f"Item found at position {result}.")
