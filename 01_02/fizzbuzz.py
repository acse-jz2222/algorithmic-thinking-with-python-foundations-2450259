"""
game for two or more players
take in turn to count from 1 to 100,
    multiple of 3 -> "fizz"
    multiple of 5 -> "buzz"
    mutiple of both 3 & 5 -> "fizz, buzz"
"""

# use modular
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz, buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
