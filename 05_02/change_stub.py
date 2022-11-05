"""
minimum set of coins
"""


import numpy as np


def make_change(target_amount):
    coin_type = [200, 100, 50, 20, 10, 5, 2, 1]

    change = np.zeros_like(coin_type)

    for i in range(len(coin_type)):
        coin_count = 0
        if target_amount >= coin_type[i]:
            coin_count += int(target_amount / coin_type[i])
            change[i] = coin_count
            target_amount -= coin_count * coin_type[i]

    return coin_type * change


print(make_change(24))  # 3: 20p + 2p + 2p
print(make_change(163))  # 5: £1 + 50p + 10p + 2p + 1p
