"""
100 doors in a row initially closed
100 passes
    first: visit every door & toggle state
    second: every seond door
    third: every third
    continue until only visit the 100th door
    which doors are open & which are closed after last pass
"""

# 1. represent state
doors = [False] * 101  # ignore index 0 & match index of the door


# one pass
for i in range(1, 101):
    doors[i] = not doors[i]

# use nested for loop
passes = 1

while passes < 101:
    for i in range(1, 101, passes):
        doors[i] = not doors[i]

    passes += 1

for i in range(1, 101):
    if doors[i]:
        print(i)
