"""
even number up to 100
"""

import time
import numpy as np

start_t = time.time()

for i in range(0, 101, 2):
    print(i)

end_t = time.time()
time_elapsed = end_t - start_t
print(f"Time take: {time_elapsed}")

start_t = time.time()
even_num = np.linspace(0, 100, 51, dtype=int)
print(even_num)
end_t = time.time()
time_elapsed = end_t - start_t
print(f"Time take: {time_elapsed}")
