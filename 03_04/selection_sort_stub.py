def find_min(xs):
    min_idx = 0

    for i in range(len(xs)):
        if xs[i] < xs[min_idx]:
            min_idx = i

    return min_idx


def selection_sort(xs):
    for i in range(len(xs)-1):
        temp = xs[i]
        min_idx = find_min(xs[i:]) + i
        xs[i] = xs[min_idx]
        xs[min_idx] = temp

    return xs


xs = [3, 2, 1, 5, 4]
print(xs)
selection_sort(xs)
print(xs)

# A nice Pythonic way to check  a list is sorted
# without relying on using Python's own sorting methods to compare.
print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))
