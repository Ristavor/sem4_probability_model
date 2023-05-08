import numpy as np
cnt = 0
for i in range(100000):
    samples = np.random.normal(loc=0, scale=3, size=4)
    deviations = np.abs(samples)
    for j in deviations:
        if j <= 3.45:
            cnt += 1
print(cnt / i)
